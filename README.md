Conversor DDS
Um aplicativo web para conversão de arquivos DDS para formatos populares como PNG, JPEG, BMP, TIFF, entre outros. Desenvolvido com Flask e Pillow, possui uma interface inspirada no estilo terminal, fácil de usar e personalizável.

🛠️ Tecnologias Utilizadas
Python 3.8+: Linguagem principal do projeto.
Flask: Framework web leve e eficiente.
Pillow: Biblioteca poderosa para manipulação de imagens.
HTML, CSS e JavaScript: Interface moderna e responsiva.
🚀 Recursos
Conversão de arquivos DDS para múltiplos formatos:
.bmp, .dib, .eps, .gif, .icns, .ico, .im, .jpeg, .jpg, .j2k, .jpx, .mpo, .pcx, .png, .ppm, .sgi, .spider, .tiff, .webp, .xbm.
Sem armazenamento em disco: Todos os arquivos são processados diretamente na memória.
Interface estilizada com barra de progresso e efeito Matrix.
Configuração simples e rápida.
📋 Pré-requisitos
Python 3.8+ instalado.
Pip para gerenciar dependências.
📦 Instalação e Execução
1️⃣ Clone o Repositório:
bash
Copiar
Editar
git clone https://github.com/seu-usuario/conversor-dds.git
cd conversor-dds
2️⃣ Crie e Ative um Ambiente Virtual (opcional):
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3️⃣ Instale as Dependências:
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Execute o Servidor Flask:
bash
Copiar
Editar
python app.py
5️⃣ Acesse no Navegador:
arduino
Copiar
Editar
http://127.0.0.1:5000
🖼️ Interface do Usuário
Tela Inicial
Formulário simples para upload de arquivos DDS.
Seleção de formatos de saída em uma lista suspensa.
Barra de progresso animada para feedback visual.
🔄 Fluxo de Conversão
O usuário faz upload de um arquivo DDS.
Seleciona o formato de saída desejado.
O arquivo é processado na memória e oferecido para download.
⚡ Formatos Suportados
Os seguintes formatos de saída estão disponíveis:

.bmp, .dib, .eps, .gif, .icns, .ico, .im, .jpeg, .jpg, .j2k, .jpx, .mpo, .pcx, .png, .ppm, .sgi, .spider, .tiff, .webp, .xbm.
📂 Estrutura do Projeto
php
Copiar
Editar
conversor-dds/
├── static/
│   ├── css/
│   │   └── style.css        # Estilos da aplicação
│   ├── js/
│   │   └── matrix.js        # Script para efeito Matrix
├── templates/
│   └── index.html           # Página principal
├── app.py                   # Backend principal em Flask
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação
⚠️ Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

📫 Contato
Desenvolvido por Seu Nome. Para dúvidas ou sugestões, sinta-se à vontade para entrar em contato ou abrir uma issue.
