Descrição Detalhada do Projeto
Importações
O código começa por importar os módulos necessários. O Flask e o render_template são utilizados para criar a aplicação web e renderizar os templates HTML, respetivamente. A session e o url_for são usados para gerir as sessões dos utilizadores e gerar URLs para rotas específicas. O qrcode é utilizado para gerar os códigos QR e o uuid4 para gerar tokens únicos.

Inicialização do Flask
Uma instância do Flask é criada e uma chave secreta é definida para a aplicação.

Rota ‘/signup’
Esta rota renderiza um template HTML chamado ‘signup.html’. Aqui, vais adicionar a lógica para mostrar o formulário de inscrição e processar os dados submetidos quando o utilizador preenche o formulário.

Rota ‘/’
Esta é a rota principal da aplicação. Quando um utilizador acede a esta rota, é gerado um token único para a sessão desse utilizador. Esse token é então codificado num código QR, que é guardado como uma imagem na pasta ‘static’. O caminho para essa imagem é passado para o template ‘index.html’.

Geração do Código QR
O código QR é gerado utilizando a biblioteca qrcode. Os dados codificados no código QR incluem a URL para a rota ‘signup’, juntamente com o token da sessão do utilizador.

Execução da Aplicação
Finalmente, a aplicação é executada em modo de depuração.

Este projeto pode ser útil em situações onde se pretende fornecer a cada utilizador um meio único e seguro para aceder a uma determinada rota (neste caso, a rota de inscrição) através de um código QR. Por exemplo, pode ser usado num evento onde os participantes se inscrevem digitalizando o código QR fornecido. Cada código QR seria único para cada sessão de utilizador, aumentando a segurança.
![image](https://github.com/cadorio/gerar-qr-code/assets/35230903/7464470f-8aa8-4889-b026-ae7b15ca486a)


