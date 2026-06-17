<div align="center">

# 🍷 CineMind — Inteligência Artificial Aplicada ao Cinema

<p align="center">
  <strong>Uma plataforma web imersiva de recomendação inteligente e curadoria de experiências cinematográficas movida a IA.</strong>
</p>

---

### 💻 Navegação Rápida
[Funcionalidades](#-funcionalidades-principais) • [Arquitetura e Design](#-identidade-visual-e-design) • [Diferenciais Técnicos](#-diferenciais-de-engenharia) • [Instalação](#-instalação-e-execução-local)

</div>

---

## 🎭 Sobre o Projeto

O **CineMind** é uma aplicação completa desenvolvida para solucionar a fadiga de escolha do usuário na hora de assistir a um filme ou série. Utilizando processamento de linguagem natural e engenharia de prompt avançada, o sistema interpreta o estado emocional e o contexto do usuário para entregar recomendações extremamente refinadas e personalizadas.

---

## 🎨 Identidade Visual e Design

A interface foi projetada milimetricamente para refletir o requinte e a penumbra das salas de cinema tradicionais, equilibrando estética e usabilidade através de uma paleta de cores restrita:

<div align="center">

| Componente | Tom de Cor | Código Hexadecimal | Aplicação em Tela |
| :--- | :--- | :--- | :--- |
| **Topbar & Painéis** | 🍷 Vinho Profundo | `#2b0000` a `#3d0a0a` | Navbar superior e divisores de seção |
| **Destaques** | 🟡 Dourado / Âmbar | `#f39c12` | Botões de ação principal, badges e focus |
| **Cards de Resposta** | 🤍 Creme / Marfim | `#f5f0e8` | Fundo do bloco de texto gerado pela IA para leitura límpida |
| **Background** | ⚫ Preto Cinematográfico | `#080808` | Fundo geral do ecossistema para imersão na penumbra |
| **Elementos de Apoio** | 🌑 Azul Escuro Discreto | `#111827` | Inputs secundários, caixas de diálogo e botões flutuantes |

</div>

---

## 🚀 Funcionalidades Principais

*   🧠 **Busca Semântica Baseada em Humor:** O usuário descreve livremente como se sente ou o que deseja assistir (por digitação ou voz), e a inteligência artificial mapeia o catálogo semanticamente para encontrar a obra perfeita.
*   🎙️ **Interface de Voz Nativa:** Integração com a API de *Web Speech Recognition* para permitir comandos e buscas por áudio diretamente através do navegador.
*   🍿 **Geração de Combos Temáticos:** Além do filme ou série, o sistema analisa a atmosfera do título para sugerir acompanhamentos, lanches e bebidas ideais para a sessão.
*   🎯 **Feedback Loop Ativo:** Mecanismo incorporado na seção *"Não era bem isso"*, permitindo que o usuário insira observações adicionais para reajustar e refinar a recomendação em tempo real.
*   🏆 **Painel de Controle e Coleções:** Módulos persistentes para salvar Histórico de Sessão, Títulos Favoritados e Assistidos, alimentando um ranking dinâmico de popularidade pessoal via `localStorage`.

---

## 💎 Diferenciais de Engenharia (Foco em Recrutamento)

Para profissionais técnicos e recrutadores que avaliam este repositório, o código destaca competências sólidas em desenvolvimento de software:

1.  **Segurança Avançada (Anti-XSS):** Toda inserção dinâmica de texto no histórico e nos cards passa por um processo de sanitização e escape estrito de caracteres (`escapeHtml`), blindando o frontend contra injeções maliciosas.
2.  **Sincronização Atômica de Estado:** O fluxo de favoritos e marcações limpa e revalida os estados locais do navegador a cada requisição, impedindo falhas de interface e persistência fantasma (*Card Ghosting*).
3.  **Acessibilidade Web Nativa:** Arquitetura construída com tags semânticas, atributos `aria-*` para leitores de tela, respeito às preferências de movimento reduzido do sistema operacional (`prefers-reduced-motion`) e integração imediata com o ecossistema VLibras.
4.  **Engenharia de Prompt e Otimização:** Orquestração assíncrona baseada em `Async/Await` conectada ao Google Gemini, garantindo respostas estruturadas sob requisições de streaming de texto de alta velocidade.

---

## 📦 Instalação e Execução Local

1. Clone o repositório para sua máquina:
```bash
   git clone [https://github.com/SEU-USUARIO/CineMind.git](https://github.com/SEU-USUARIO/CineMind.git)
   cd CineMind
