# PRD - Proof of Remote Desktop

> ⚠️ **Aviso Legal**: Este projeto foi criado exclusivamente para fins educacionais e de estudo em segurança ofensiva. O uso indevido desta ferramenta pode ser ilegal e é de total responsabilidade do usuário.

## 💡 Sobre o Projeto

**PRD** (Proof of Remote Desktop) é um executável desenvolvido como parte dos meus estudos em segurança ofensiva. Seu objetivo é simular uma abordagem de captura de tela remota utilizando o programa [RustDesk](https://rustdesk.com/), uma alternativa de código aberto para acesso remoto a desktops.

Ao ser executado, o PRD realiza as seguintes ações de forma extremamente rápida:

1. Baixa e executa o RustDesk;
2. Captura imediatamente a tela da "vítima";
3. Oculta a janela do RustDesk;
4. Envia a imagem capturada para um grupo privado no Telegram, onde o "atacante" pode visualizar;
5. Mantém o processo ativo, aguardando tentativa de conexão.

Essa prova de conceito visa demonstrar como uma simples execução local pode fornecer informações visuais suficientes para facilitar uma futura conexão remota ao dispositivo da vítima.

## ⚠️ Limitação Atual

Atualmente, **a vítima ainda precisa aceitar manualmente a solicitação de conexão no RustDesk**. Essa é uma limitação conhecida e será trabalhada em futuras versões para tornar o processo mais automatizado.

## 🧪 Finalidade

Este projeto **não deve ser usado contra terceiros sem autorização explícita**. Ele foi criado para fins de:

- Estudo e aprendizado sobre vetores de ataque remoto;
- Entendimento de comportamento de ferramentas legítimas em cenários ofensivos;
- Demonstração de provas de conceito em ambientes controlados.

## 📌 Requisitos

- Sistema Windows
- Conexão com a internet
- Token de bot e ID de grupo do Telegram para envio da imagem

## 🚧 Melhorias Futuras

- Eliminar a necessidade de aceite manual;
- Embutir o RustDesk no executável para reduzir dependências externas;
- Tornar o processo mais modular e adaptável para simulações.

---

**Autor:** Pavax  
**Licença:** Apenas para uso educacional
