from flask import Flask, render_template, session, url_for
import qrcode
from uuid import uuid4

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/signup')
def signup():
    # Aqui você adicionará a lógica para mostrar o formulário de inscrição
    # e para processar os dados do formulário quando for submetido
    return render_template('signup.html')

@app.route('/')
def index():
    # Gere um token único para a sessão do usuário
    session_token = str(uuid4())
    session['user_token'] = session_token

    # Dados que você quer codificar no QR Code
    # A função url_for gera uma URL para a rota 'signup'
    dados = url_for('signup', _external=True, token=session_token)

    # Gere o QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    # Crie uma imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Salve a imagem na pasta 'static'
    qr_code_filename = f'qrcode_{session_token}.png'
    img.save(f'static/{qr_code_filename}')

    # Passe o caminho do QR Code para o template
    return render_template('index.html', qr_code_path=qr_code_filename)

if __name__ == '__main__':
    app.run(debug=True)
