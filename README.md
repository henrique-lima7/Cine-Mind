<div align="center">
  <img src="https://img.shields.io/badge/Release-Premium_v2.0-f39c12?style=for-the-badge&logo=probot&logoColor=0a0c10" alt="CineMind Version">
  <img src="https://img.shields.io/badge/UI/UX-Cinematic_Premium-e74c3c?style=for-the-badge" alt="UI/UX Cinematic">
  <img src="https://img.shields.io/badge/AI--Integrated-Google_Gemini-00439C?style=for-the-badge&logo=google-gemini&logoColor=white" alt="AI Integrated">

  <br><br>

  <h1>🎬 Cine<span>Mind</span> — Sua IA do Cinema</h1>
  
  <p align="center">
    <strong>Uma aplicação web imersiva de recomendação inteligente e experiências cinematográficas movida a Inteligência Artificial.</strong>
  </p>

  <p align="center">
    <a href="#-funcionalidades-chave">Funcionalidades</a> •
    <a href="#-tecnologias-e-arquitetura">Tecnologias</a> •
    <a href="#-diferenciais-de-engenharia-de-software">Diferenciais Técnicos</a> •
    <a href="#-como-rodar-o-projeto">Como Rodar</a>
  </p>
</div>

---

## 🎭 Sobre o CineMind

O **CineMind** transforma a cansativa tarefa de escolher o próximo filme em uma experiência de cinema interativa em casa. Esqueça os filtros tradicionais e mecânicos: a plataforma foi desenvolvida para entender o **humor, os sentimentos e o contexto** do usuário expressos em linguagem natural através de texto ou voz, devolvendo indicações personalizadas integradas ao catálogo.

A interface foi projetada milimetricamente para simular a penumbra e a sofisticação de uma sala de cinema premium, alternando dinamicamente entre efeitos de iluminação ambiente digital (*ambient glow*), vinhetas e um efeito interativo de máquina de escrever (*typewriter*) que dá vida às respostas da IA.

---

## 🚀 Funcionalidades-Chave

* 🧠 **Busca Semântica por Humor:** O usuário dita o que quer assistir em linguagem natural (ex: *"Quero um suspense psicológico que exploda minha mente e tenha um final surpreendente"*).
* 🎙️ **Interface de Voz Nativa:** Integração com a API de *Web Speech Recognition* para comandos e buscas por voz diretamente no navegador.
* 🥤🍟 **Gerador Inteligente de Combos:** Sugestões dinâmicas de petiscos, lanches e bebidas que combinam perfeitamente com a atmosfera do filme ou série recomendada.
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
* **Vanilla JavaScript (ES6+):** * Arquitetura assíncrona baseada em `Async/Await` e manipulação precisa do DOM.
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
