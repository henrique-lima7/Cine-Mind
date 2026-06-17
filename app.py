import os
import json
import random
import time
from threading import Lock
from google import genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Configuração do arquivo Top 10 Global ─────────────────────────────────────
TOP10_FILE = "top10_global.json"

# Lock para impedir que duas requisições simultâneas leiam e gravem o
# top10_global.json ao mesmo tempo (evita corrupção/perda de votos)
contagem_lock = Lock()

# ── Lê a API key do .env manualmente ──────────────────────────────────────────
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_env = os.path.join(pasta_atual, '.env')

minha_chave = None
with open(caminho_env, 'r', encoding='utf-8') as f:
    for linha in f:
        if linha.startswith("GEMINI_API_KEY="):
            minha_chave = linha.split("=")[1].strip()

client = genai.Client(api_key=minha_chave)

# ── Carrega o catálogo de filmes com as plataformas inclusas ─────────────────
caminho_json = os.path.join(pasta_atual, 'filmes.json')
with open(caminho_json, 'r', encoding='utf-8') as arquivo:
    catalogo_filmes = json.load(arquivo)


# ── Funções Auxiliares para o Top 10 Global ───────────────────────────────────
def carregar_contagem():
    if os.path.exists(TOP10_FILE):
        with open(TOP10_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_contagem(dados):
    with open(TOP10_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False)


# ── Função Auxiliar de Retentativa Melhorada ──────────────────────────────────
def gerar_conteudo_com_tentativas(prompt, max_tentativas=3):
    for tentativa in range(max_tentativas):
        try:
            # Usando o gemini-2.5-flash estável
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text
        except Exception as e:
            # Imprime o erro real no terminal do PyCharm para você saber o diagnóstico exato
            print(f"⚠️ Tentativa {tentativa + 1} falhou. Motivo: {e}")

            # Se for a última tentativa, entrega o aviso amigável para a interface
            if tentativa == max_tentativas - 1:
                return f"❌ Nossos servidores estão um pouco lentos agora. Pode tentar novamente em alguns segundos?"

            # Se não for a última, aguarda um tempo progressivo (backoff sutil) e tenta de novo
            time.sleep(2)


# ── ROTA 1: Página principal ──────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')


# ── ROTA 2: Recomendação por busca de texto ───────────────────────────────────
@app.route('/recomendar', methods=['POST'])
def recomendar():
    dados = request.get_json()
    pedido_usuario = dados.get('pedido', '')

    prompt = f"""
    Você é o sistema de recomendação do CineMind, uma plataforma de cinema premium.
    Catálogo disponível:
    {catalogo_filmes}

    Pedido do usuário: "{pedido_usuario}"

    Sua tarefa:
    1. Escolha a melhor opção do catálogo que se encaixe no pedido.
    2. Identifique exatamente a lista contida em 'onde_assistir' para esse filme.
    3. Explique de forma calorosa e envolvente por que esse título combina com o pedido.

    Formate a resposta EXATAMENTE assim (mantenha os termos exatos para o sistema mapear):
    **🎬 RECOMENDAÇÃO CINEMIND**
    [Nome do Filme/Série] ([Tipo] - [Gênero])
    **Onde assistir:** [Escreva aqui as plataformas separadas por vírgula exatamente como no JSON]

    **Por que você vai amar?**
    [Duas ou três frases que convencem o usuário a assistir, relacionando com o pedido dele]
    """

    texto_resposta = gerar_conteudo_com_tentativas(prompt)
    return jsonify({"recomendacao": texto_resposta})


# ── ROTA 3: Modo Surpresa ─────────────────────────────────────────────────────
@app.route('/surpresa', methods=['POST'])
def surpresa():
    escolha_aleatoria = random.choice(catalogo_filmes)

    prompt = f"""
    Você é o apresentador mestre do CineMind. Sorteamos este título para o usuário:
    {escolha_aleatoria}

    Apresente esse título de forma empolgante e irresistível.

    Formate a resposta EXATAMENTE assim:
    **🎲 A ROLETA ESCOLHEU...**
    [Nome do Filme/Série] ([Tipo] - [Gênero])
    **Onde assistir:** [Escreva aqui as plataformas separadas por vírgula exatamente como no JSON]

    **🔥 Por que você PRECISA assistir agora?**
    [Apresentação ultra empolgante sobre o título]
    """

    texto_resposta = gerar_conteudo_com_tentativas(prompt)
    return jsonify({"recomendacao": texto_resposta})


# ── ROTA 4: Gera apenas o combo de lanche para um filme já recomendado ────────
@app.route('/combo', methods=['POST'])
def combo():
    dados = request.get_json()
    titulo = dados.get('titulo', 'um filme')

    prompt = f"""
    Você é o chef curador de experiências do CineMind.
    O usuário vai assistir: "{titulo}"

    Crie um combo de lanche PERSONALIZADO, criativo e irresistível que combine
    perfeitamente com o clima desse título.

    Formate EXATAMENTE assim:
    **🍿 COMBO PERFEITO PARA ESTE FILME**

    **🥤 Bebida**
    [Sugestão de bebida com justificativa]

    **🍔 Petisco Principal**
    [Sugestão de petisco com justificativa]

    **🍫 Finalizador**
    [Uma sobremesa ou guloseima para fechar]
    """

    texto_resposta = gerar_conteudo_com_tentativas(prompt)
    return jsonify({"combo": texto_resposta})


# ── ROTA 5: Gera combo para um filme que o usuário já escolheu ────────────────
@app.route('/montar-combo', methods=['POST'])
def montar_combo():
    dados = request.get_json()
    filme_escolhido = dados.get('filme', '')

    prompt = f"""
    Você é o chef curador de experiências do CineMind.
    O usuário já escolheu assistir por conta própria: "{filme_escolhido}"

    Crie um combo de lanche temático personalizado para essa produção.

    Formate EXATAMENTE assim:
    **🍿 COMBO ESPECIAL PARA "{filme_escolhido}"**

    **🥤 Bebida**
    [Sugestão com justificativa]

    **🍔 Petisco Principal**
    [Sugestão com justificativa]

    **🍫 Finalizador**
    [Sobremesa ou guloseima temática]

    **💡 Dica do Chef CineMind**
    [Uma dica especial de como preparar o ambiente para a sessão]
    """

    texto_resposta = gerar_conteudo_com_tentativas(prompt)
    return jsonify({"combo": texto_resposta})


# ── ROTA 6: Favoritar / Desfavoritar Título (Persistência Global) ─────────────
@app.route("/favoritar", methods=["POST"])
def favoritar():
    body = request.get_json()
    titulo = body.get("titulo")
    acao = body.get("acao")

    if not titulo:
        return jsonify({"erro": "titulo obrigatório"}), 400

    with contagem_lock:
        contagem = carregar_contagem()
        atual = contagem.get(titulo, 0)
        contagem[titulo] = atual + 1 if acao == "add" else max(0, atual - 1)
        salvar_contagem(contagem)
        total = contagem[titulo]

    return jsonify({"ok": True, "total": total})


# ── ROTA 7: Listar o Top 10 Global baseado nas interações de todos ────────────
@app.route("/top10-global", methods=["GET"])
def top10_global():
    with contagem_lock:
        contagem = carregar_contagem()
    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)[:10]
    return jsonify({"top10": [{"titulo": t, "favoritos": c} for t, c in ranking if c > 0]})


if __name__ == '__main__':
    app.run(debug=True)