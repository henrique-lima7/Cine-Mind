# CineMind — Inteligência Artificial Aplicada ao Cinema

Uma aplicação web imersiva para recomendação inteligente de filmes e curadoria de experiências cinematográficas, movida a Large Language Models (LLMs).

---

## Identidade Visual e Atmosfera

O projeto foi desenvolvido sob uma paleta de cores estrita que simula a sofisticação e a penumbra de uma sala de cinema premium, garantindo alta legibilidade e imersão.

| Elemento de Interface | Cor Predominante | Código Hexadecimal |
| :--- | :--- | :--- |
| **Painéis e Navbar** | Vinho Profundo | `#2d0a0a` |
| **Destaques e Micro-interações** | Dourado / Âmbar | `#f39c12` |
| **Cards de Resposta (Fundo)** | Creme / Marfim | `#f5f0e8` |
| **Background Geral** | Preto Cinematográfico | `#080808` |
| **Componentes de Sistema** | Azul Escuro Discreto | `#111827` |

---

## Funcionalidades Principais

### Busca Semântica por Humor
O sistema processa requisições complexas em linguagem natural através de texto ou áudio, interpretando sentimentos, analogias e contextos para buscar o título ideal no catálogo.

### Sugestão de Acompanhamentos (Combos)
Além da recomendação do título, a inteligência artificial analisa o gênero e o tom da obra para sugerir um combo personalizado de lanches, petiscos e bebidas.

### Loops de Refinamento (Feedback Ativo)
Caso a indicação inicial não atenda às expectativas, a interface oferece um fluxo de re-análise, permitindo que o usuário insira novas observações e guie o algoritmo para um resultado mais preciso.

### Persistência de Dados Locais
Gerenciamento de coleções pessoais estruturado em camadas para Histórico de Sessão, Títulos Favoritados e Assistidos, organizando um Top 10 automatizado de popularidade sem a necessidade de autenticação externa.

---

## Engenharia e Arquitetura de Software

O ecossistema foi projetado de forma modular, priorizando a performance do lado do cliente (Client-Side) e o processamento assíncrono no servidor.

*   **Frontend Modular (Vanilla JS):** Desenvolvimento limpo, livre de frameworks pesados, utilizando manipulação cirúrgica do DOM, escuta de eventos via MutationObserver e armazenamento em repositório local.
*   **Acessibilidade e Padrões Web:** Interface estruturada com marcações semânticas estritas, respeito a preferências de movimento reduzido do sistema operacional e integração nativa com o VLibras.
*   **Camada de Segurança (Anti-XSS):** Sanitização estrita de todas as strings injetadas dinamicamente na tela através de métodos de escape de caracteres, anulando brechas de injeção maliciosa.
*   **Orquestração de LLMs:** Integração assíncrona com a API do Google Gemini, utilizando engenharia de prompt estruturada para garantir respostas padronizadas e mapeamento correto de streaming de texto.

---

## Instalação e Execução Local

1. Clone este repositório para o seu ambiente local:
```bash
   git clone [https://github.com/SEU-USUARIO/CineMind.git](https://github.com/SEU-USUARIO/CineMind.git)
   cd CineMind
