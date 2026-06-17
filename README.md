<div align="center">
  <!-- Badges com as Cores Exatas do Site (Vinho, Âmbar e Preto) -->
  <img src="https://img.shields.io/badge/Release-Premium_v2.0-f39c12?style=for-the-badge&logo=probot&logoColor=1f0505" alt="CineMind Version">
  <img src="https://img.shields.io/badge/Ambiente-Velvet_Wine_&_Gold-4a1212?style=for-the-badge" alt="UI Velvet Wine">
  <img src="https://img.shields.io/badge/AI--Integrated-Google_Gemini-11151c?style=for-the-badge&logo=google-gemini&logoColor=f5f5f5" alt="AI Integrated">

  <br><br>

  <!-- Título Principal com a Identidade CineMind -->
  <h1>🎬 Cine<span>Mind</span> — Sua IA do Cinema</h1>
  
  <p align="center">
    <strong>Uma aplicação web imersiva de recomendação inteligente e curadoria de lanches movida a Inteligência Artificial.</strong>
  </p>

  <p align="center">
    <a href="#-funcionalidades-chave">Funcionalidades</a> •
    <a href="#-identidade-visual-premium">Design Imersivo</a> •
    <a href="#-tecnologias-e-arquitetura">Tecnologias</a> •
    <a href="#-diferenciais-de-engenharia-de-software">Diferenciais Técnicos</a>
  </p>
</div>

---

## 🎭 Sobre o CineMind

O **CineMind** transforma o dilema de escolher o próximo filme em uma experiência de imersão completa. O software compreende o humor, os sentimentos e os desejos do usuário transmitidos em linguagem natural (por digitação ou voz) e realiza uma busca semântica inteligente no catálogo para entregar o título ideal.

### 🎨 Identidade Visual Premium (Fidelidade de Interface)
Inspirado na atmosfera requintada das salas de cinema e grandes teatros, o design da interface conta com:
* **Navbar em Vinho Profundo:** Uma barra superior sólida em tom veludo que organiza elegantemente o fluxo de navegação e as contagens dinâmicas.
* **Penumbra Computacional:** Telas escuras e texturizadas com gradientes pretos e cinza-carvão que reduzem a fadiga ocular e focam o olhar na tela.
* **Luzes de Arandela Digitais:** Pontos de iluminação âmbar difusa nos cantos que simulam os refletores laterais de uma sala real antes do filme começar.
* **Cards de Leitura em Creme/Marfim:** Bloco de contraste projetado na cor marfim para garantir uma legibilidade perfeita, clara e polida das respostas da IA.

---

## 🚀 Funcionalidades-Chave

* 🧠 **Busca Semântica por Humor:** O usuário dita o que quer assistir em linguagem natural (ex: *"Quero uma série do estilo The Night Of"*).
* 🎙️ **Interface de Voz Nativa:** Integração com a API de *Web Speech Recognition* para comandos e buscas por voz diretamente no navegador.
* 🍿🍔 **Gerador Inteligente de Combos:** Sugestões dinâmicas de petiscos, lanches e bebidas que combinam perfeitamente com a atmosfera do filme ou série recomendada.
* 🎲 **Surpreenda-me:** Algoritmo de curadoria rápida para usuários indecisos.
* 🎯 **Feedback Loop Ativo:** Sistema de re-ajuste de recomendação caso o usuário queira refinar o resultado (botão *"Não era bem isso"*), permitindo engajamento contínuo com a IA.
* 🏆 **Top 10 & Coleções:** Painel de controle persistente contendo Histórico da Sessão, Favoritos, Títulos Assistidos e um Ranking dinâmico de popularidade pessoal.
* ☀️/🌙 **Dual-Theme Imersivo:** Modo Escuro inspirado no veludo e penumbra das grandes telas e Modo Claro sofisticado baseado em tons marfim e dourado.

---

## 🛠️ Tecnologias e Arquitetura

O projeto foi construído focando em performance, zero dependências externas desnecessárias (*Vanilla Client*) e alta manutenibilidade de código:

### Frontend (Client-Side)
* **HTML5 Semântico:** Estruturação limpa focada em SEO e acessibilidade (regras de `role`, `aria-label` e estados de acessibilidade).
* **CSS3 Avançado (Tokens & Variables):** Arquitetura CSS baseada em Design Tokens (`:root`), animações complexas (`cubic-bezier`), responsividade fluida (`clamp`) e transições de tema centralizadas.
* **Vanilla JavaScript (ES6+):** 
    * Arquitetura assíncrona baseada em `Async/Await` e manipulação precisa do DOM.
    * Otimizações de performance (uso de `MutationObserver` para injeção de eventos em elementos dinâmicos).
    * Gerenciamento de estados locais persistidos via `localStorage` (padrão *Repository* encapsulado no objeto `Store`).

### Backend & Integrações (Server-Side)
* **Python / PyCharm:** Ambiente modularizado de desenvolvimento.
* **Google Gemini API:** Integração de Large Language Models (LLMs) para análise de contexto, busca semântica no catálogo e geração de lanches temáticos.
* **Acessibilidade Universal:** Inclusão nativa do ecossistema **VLibras** para tradução automática em tempo real para Língua Brasileira de Sinais.

---

## 💎 Diferenciais de Engenharia de Software (Para Recrutadores)

Se você está avaliando este repositório para uma vaga técnica, aqui estão alguns padrões arquiteturais e boas práticas implementados no código:

1.  **Prevenção de Falhas de Segurança (XSS):** Todo dado renderizado dinamicamente no histórico ou em modais passa por uma função sanitizadora estrita de escape (`escapeHtml`), neutralizando injeções maliciosas.
2.  **Sincronização Atômica de Estado:** O sistema de curtidas e histórico limpa e re-valida estados locais a cada nova requisição para impedir o vazamento de dados de um card (*Card Ghosting*) para o outro.
3.  **Performance & UX (Auto-Scroll Fluido):** O efeito de *typewriter* calcula dinamicamente o tamanho do texto para acelerar a velocidade em respostas longas e realiza um *auto-scroll* suave ao final da página utilizando `scrollIntoView`, garantindo que o usuário nunca perda o foco da leitura.
4.  **Respeito às Preferências do Sistema:** O código monitora a API `prefers-reduced-motion` do sistema operacional para desativar animações pesadas para usuários que necessitam de acessibilidade visual, além de verificar o `prefers-color-scheme` para carregar o tema padrão do usuário.

---

## 📦 Como Rodar o Projeto Localmente

1. **Clone o repositório:**
```bash
   git clone [https://github.com/SEU-USUARIO/CineMind.git](https://github.com/SEU-USUARIO/CineMind.git)
   cd CineMind
