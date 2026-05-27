from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('nome')
    estado = request.form['estado']
    formaçao = request.form['formaçao']
    modalidade = request.form.getlist('modalidades')
    senha = request.form.get('senha')

    if senha == 12345:
        return f"senha correta!"
    else: 
        return f"senha incorreta!"

    return "{} e {} e {} e {} e {}".format(nome,email, estado, formaçao, modalidade)

if __name__ == '__main__':
    app.run(debug=True)