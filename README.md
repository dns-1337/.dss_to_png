<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor DDS</title>
    <style>
        /* Estilo global */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }

        header {
            background: #333;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }

        header p {
            font-size: 1rem;
            margin: 0.5rem 0 0;
        }

        main {
            max-width: 800px;
            margin: 2rem auto;
            padding: 1rem;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        main h2 {
            margin-top: 1.5rem;
            color: #444;
        }

        main ul {
            list-style: none;
            padding: 0;
        }

        main ul li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #ddd;
        }

        main ul li:last-child {
            border-bottom: none;
        }

        pre {
            background: #f4f4f4;
            padding: 1rem;
            border-left: 4px solid #333;
            overflow-x: auto;
        }

        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            font-weight: bold;
        }

        footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Conversor DDS</h1>
        <p>Um aplicativo web simples para converter arquivos DDS para formatos populares.</p>
    </header>

    <main>
        <section>
            <h2>Recursos</h2>
            <ul>
                <li>Conversão de arquivos DDS para formatos populares como PNG, JPEG, BMP, TIFF, e outros.</li>
                <li>Interface moderna inspirada no estilo terminal.</li>
                <li>Não utiliza armazenamento em disco — tudo é processado na memória.</li>
                <li>Fácil de configurar e usar.</li>
            </ul>
        </section>

        <section>
            <h2>Como Usar</h2>
            <ol>
                <li>Clone o repositório:
                    <pre><code>git clone https://github.com/seu-usuario/conversor-dds.git</code></pre>
                </li>
                <li>Instale as dependências:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li>Inicie o servidor:
                    <pre><code>python app.py</code></pre>
                </li>
                <li>Acesse no navegador:
                    <pre><code>http://127.0.0.1:5000</code></pre>
                </li>
            </ol>
        </section>

        <section>
            <h2>Formatos Suportados</h2>
            <p>O aplicativo suporta os seguintes formatos de saída:</p>
            <ul>
                <li>.bmp</li>
                <li>.dib</li>
                <li>.eps</li>
                <li>.gif</li>
                <li>.icns</li>
                <li>.ico</li>
                <li>.im</li>
                <li>.jpeg</li>
                <li>.jpg</li>
                <li>.j2k</li>
                <li>.jpx</li>
                <li>.mpo</li>
                <li>.pcx</li>
                <li>.png</li>
                <li>.ppm</li>
                <li>.sgi</li>
                <li>.spider</li>
                <li>.tiff</li>
                <li>.webp</li>
                <li>.xbm</li>
            </ul>
        </section>

        <section>
            <h2>Licença</h2>
            <p>Este projeto está licenciado sob a licença MIT. Consulte o arquivo <code>LICENSE</code> para mais detalhes.</p>
        </section>
    </main>

    <footer>
        <p>Desenvolvido por <a href="https://github.com/seu-usuario" target="_blank">Seu Nome</a>. Código disponível em <a href="https://github.com/seu-usuario/conversor-dds" target="_blank">GitHub</a>.</p>
    </footer>
</body>
</html>
