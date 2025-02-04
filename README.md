<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <header>
        <h1>Loja de Carros - Projeto Django 🚗💻</h1>
        <p><strong>Desenvolvido por:</strong> Kailane Sarah - Projeto criado durante o curso da PyCode BR.</p>
    </header>
    
  <section>
        <h2>🚀 Sobre o Projeto</h2>
        <p>O <strong>Loja de Carros</strong> é um sistema web desenvolvido com Django, permitindo que usuários se cadastrem, façam login/logout e gerenciem anúncios de veículos disponíveis para venda. Para tornar a experiência mais dinâmica, utilizamos a <strong>OpenAI</strong> para gerar descrições automáticas dos carros.</p>
    </section>

  <section>
        <h2>🔹 Funcionalidades</h2>
        <ul>
            <li><strong>Cadastro de Carros:</strong> Adicione veículos com descrições geradas automaticamente pela OpenAI.</li>
            <li><strong>CRUD Completo:</strong> Criação, edição, exclusão e listagem de carros.</li>
            <li><strong>Autenticação de Usuários:</strong> Registro, login e logout.</li>
            <li><strong>Templates Personalizados:</strong> Interface agradável e intuitiva para facilitar a navegação.</li>
        </ul>
    </section>

  <section>
        <h2>📌 Como Configurar o Projeto</h2>
        <h3>🔧 Pré-requisitos</h3>
        <ul>
            <li>Python 3.x</li>
            <li>Django</li>
            <li>Bibliotecas adicionais (listadas em <code>requirements.txt</code>)</li>
        </ul>
        
   <h3>📥 Passos para Instalação</h3>
        <ol>
            <li>Clone este repositório:
                <pre><code>git clone https://github.com/kailanesarah/project-store-car.git</code></pre>
            </li>
            <li>Acesse o diretório do projeto:
                <pre><code>cd project-store-car</code></pre>
            </li>
            <li>Instale as dependências necessárias:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Configure as chaves de acesso no arquivo <strong>.env</strong>:
                <pre><code>
                DJANGO_SECRET_KEY='sua_secret_key_aqui'
                DB_NAME='nome_do_banco'
                DB_USER='usuario_do_banco'
                DB_PASSWORD='senha_do_banco'
                </code></pre>
            </li>
            <li>Realize as migrações do banco de dados:
                <pre><code>python manage.py migrate</code></pre>
            </li>
            <li>(Opcional) Crie um superusuário para acessar o painel administrativo:
                <pre><code>python manage.py createsuperuser</code></pre>
            </li>
            <li>Inicie o servidor de desenvolvimento:
                <pre><code>python manage.py runserver</code></pre>
            </li>
        </ol>
        <p>🔗 Agora você pode acessar o projeto no navegador: <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a></p>
    </section>

  <section>
        <h2>🌍 Endpoints do Projeto</h2>
        <h3>🔹 Rotas para Gerenciamento de Carros</h3>
        <ul>
            <li><strong>GET</strong> <code>/project/listCars/</code> - Lista todos os carros cadastrados.</li>
            <li><strong>GET</strong> <code>/project/detailCars/&lt;pk&gt;/</code> - Exibe detalhes de um carro específico.</li>
            <li><strong>POST</strong> <code>/project/registerCars/</code> - Adiciona um novo carro.</li>
            <li><strong>PUT</strong> <code>/project/updateCars/&lt;pk&gt;/</code> - Atualiza um carro existente.</li>
            <li><strong>DELETE</strong> <code>/project/deleteCars/&lt;pk&gt;/</code> - Remove um carro do sistema.</li>
        </ul>

  <h3>🔹 Rotas para Contas de Usuários</h3>
        <ul>
            <li><strong>POST</strong> <code>/account/registerAccount/</code> - Registra um novo usuário.</li>
            <li><strong>POST</strong> <code>/account/loginAccount/</code> - Realiza login.</li>
            <li><strong>POST</strong> <code>/account/logoutAccount/</code> - Realiza logout.</li>
        </ul>
    </section>

  <section>
        <h2>🔮 Melhorias Futuras</h2>
        <ul>
            <li>Adição de filtros avançados para pesquisa de carros (por preço, marca, modelo, etc.).</li>
            <li>Implementação de avaliações e comentários dos usuários sobre os veículos.</li>
            <li>Interface mais moderna utilizando Bootstrap ou Tailwind CSS.</li>
            <li>Integração com sistemas de pagamento para permitir compras online.</li>
        </ul>
    </section>

  <footer>
        <h2>📩 Contato</h2>
        <p>Caso tenha alguma dúvida ou sugestão, entre em contato!</p>
        <p>📧 <strong>Email:</strong> <a href="mailto:kailanesarahpro@gmail.com">kailanesarahpro@gmail.com</a></p>
        <p>🔗 <strong>GitHub:</strong> <a href="https://github.com/kailanesarah">Kailane Sarah</a></p>
        <p>📢 <strong>Gostou do projeto? Deixe uma ⭐ no repositório!</strong> 🚀</p>
    </footer>
</body>
</html>

