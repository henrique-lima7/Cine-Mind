# 🎬 CineMind — Sua IA do Cinema Premium

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-3.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/Google%20GenAI-Gemini%202.5%20Flash-orange.svg" alt="Gemini AI">
  <img src="https://img.shields.io/badge/UI%2FUX-Cinematic%20Dark%20%26%20Light-purple.svg" alt="UI/UX Theme">
</p>

O **CineMind** é uma plataforma premium de recomendação de filmes e séries que une o poder da Inteligência Artificial do Google (`gemini-2.5-flash`) a uma experiência de interface rica, imersiva e cinematográfica. 

Diferente de algoritmos de streaming genéricos, o CineMind entende o **humor, os sentimentos e o contexto** do usuário expressados em linguagem natural (texto ou voz) e encontra a obra perfeita dentro de um catálogo curado.

---

## 📸 Demonstração do Projeto

Abaixo você pode conferir o fluxo completo da aplicação e como o design premium foi construído para simular a atmosfera de uma verdadeira sala de cinema:

### 1️⃣ Tela Inicial
Interface escura com efeitos de luz ambiente adaptativa nas bordas, tags rápidas de humor e sistema integrado de busca por texto ou comando de voz nativo.
<p align="center">
  <img src="image_51364f.jpg" width="90%" alt="Tela Inicial do CineMind">
</p>

### 2️⃣ Geração do Filme com IA
O sistema exibe o resultado utilizando um efeito dinâmico de digitação (*typewriter effect*), destaca as plataformas com as cores oficiais das marcas de streaming e adiciona um painel interativo de feedback para refinar a busca.
<p align="center">
  <img src="image_5187e7.jpg" width="90%" alt="Card de Recomendação Gerado pela IA">
</p>

### 3️⃣ Menu do Chef — Combo de Comida
Com um único clique no botão sob demanda, a inteligência artificial analisa o clima específico do filme escolhido e monta um combo gastronômico personalizado com bebida, petisco principal e sobremesa temática.
<p align="center">
  <img src="image_51882b.jpg" width="90%" alt="Sugestão de Combo Temático">
</p>

### 4️⃣ Histórico da Sessão
Acompanhe de forma simples tudo o que a IA gerou para você na aba de histórico local. Os itens salvam o horário relativo da busca e se há um combo atrelado àquela sugestão.
<p align="center">
  <img src="image_518888.jpg" width="90%" alt="Painel de Histórico">
</p>

### 5️⃣ Ranking Top 10 Global
O coração social da plataforma: um painel que exibe dinamicamente os títulos de maior sucesso entre todos que acessam o sistema.
<p align="center">
  <img src="image_518ba9.jpg" width="90%" alt="Painel do Top 10 Global">
</p>

---

## 🏆 Como funciona o algoritmo do Top 10?

O **Top 10** do CineMind opera em tempo real e de forma **totalmente persistente e global**. Ele não se limita apenas ao seu navegador, mas computa as interações coletivas:

* **Contagem Unificada:** Toda vez que qualquer usuário, em qualquer dispositivo, clica em "Favoritar" para salvar um título em sua coleção, o servidor recebe uma requisição e adiciona um voto na base geral do projeto.
* **Dinâmica de Posições (Ranking Vivo):** A lista é reordenada automaticamente a cada nova curtida recebida no backend. 
  > *Exemplo prático:* Se o **Filme A** acumulou um total de **5 curtidas** globais e o **Filme B** alcançar **10 curtidas**, o **Filme B** assume imediatamente a primeira posição do ranking.
* **Segurança concorrente:** Para evitar perdas ou corrupção de votos quando várias pessoas interagem ao mesmo tempo, o backend utiliza um sistema de trava por thread (`threading.Lock`), garantindo que a gravação do arquivo `top10_global.json` aconteça de maneira limpa, estável e segura.

---

## 🔥 Funcionalidades Técnicas Destacadas

* **🧠 Busca Semântica por Humor:** Processamento de linguagem natural que interpreta gírias e sentimentos para mapear o arquivo estruturado de dados.
* **🎙️ Reconhecimento de Voz Nativo:** Integração completa com a API *Web Speech* do próprio navegador para comandos via microfone.
* **🌗 Modo Escuro / Modo Claro:** Transições de opacidade e cores calculadas via propriedades CSS customizadas para manter o conforto visual.
* **💾 Persistência Híbrida:** Uso estratégico de `localStorage` para manter as coleções privadas de cada aparelho e arquivos `JSON` no servidor Flask para a contagem global.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python e Flask.
* **IA:** Google GenAI SDK (Gemini 2.5 Flash).
* **Frontend:** HTML5, CSS3 Avançado (Keyframes, CSS Variables) e JavaScript Puro (Vanilla JS).
* **Acessibilidade:** Plugin oficial VLibras integrado diretamente no documento.

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório:**
```bash
   git clone [https://github.com/SEU-USUARIO/cinemind.git](https://github.com/SEU-USUARIO/cinemind.git)
   cd cinemind
