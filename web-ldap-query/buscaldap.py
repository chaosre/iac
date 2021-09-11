

import flask
from flask import Flask, request, flash
#from shelljob import proc
import os

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700&display=swap');

* {
    margin: 0;
    border: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

body {
    background: linear-gradient(45deg, #e2a32d, #e06c00);
    background-repeat: no-repeat;
    min-height: 100vh;
    min-width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
}

main.container {
    background: white;
    min-width: 320px;
    min-height: 40vh;
    padding: 2rem;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
}

main h2 {
    font-weight: 600;
    margin-bottom: 2rem;
    position: relative;
}

main h2::before {
    content: '';
    position: absolute;
    height: 4px;
    width: 25px;
    bottom: 3px;
    left: 0;
    border-radius: 8px;
    background: linear-gradient(45deg, #e2a32d, #e06c00);
}

form {
    display: flex;
    flex-direction: column;
}

.input-field {
    position: relative;
}

form .input-field {
    margin-bottom: 1.5rem;
}

.input-field .underline::before {
    content: '';
    position: absolute;
    height: 1px;
    width: 100%;
    bottom: -5px;
    left: 0;
    background: rgba(0, 0, 0, 0.2);
}

.input-field .underline::after {
    content: '';
    position: absolute;
    height: 1px;
    width: 100%;
    bottom: -5px;
    left: 0;
    background: linear-gradient(45deg, #e2a32d, #e06c00);
    transform: scaleX(0);
    transition: all .3s ease-in-out;
    transform-origin: left;
}

.input-field input:focus ~ .underline::after {
    transform: scaleX(1);
}

.input-field input {
    outline: none;
    font-size: 0.9rem;
    color: rgba(0, 0, 0, 0.7);
    width: 100%;
}

.input-field input::placeholder {
    color: rgba(0, 0, 0, 0.5);
}

form input[type="submit"] {
    margin-top: 2rem;
    padding: 0.4rem;
    width: 100%;
    background: linear-gradient(to left, #e2a32d, #e06c00);
    cursor: pointer;
    color: white;
    font-size: 0.9rem;
    font-weight: 300;
    border-radius: 4px;
    transition: all 0.3s ease;
}

form input[type="submit"]:hover {
    letter-spacing: 0.5px;
    background: linear-gradient(to right, #e2a32d, #e06c00);
}

.footer {
    display: flex;
    flex-direction: column;
    margin-top: 1rem;
}

</style>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/1ab94d0eba.js" crossorigin="anonymous"></script>
    <title>BuscaLDAP</title>
</head>
<body>
    <main class="container">
        <h2>BuscaLDAP</h2>
        <form action="process" method="POST">
            <div class="input-field">
                <input type="text" name="racf" id="racf" placeholder="Digite seu RACF">
                <div class="underline"></div>
            </div>
            <div class="input-field">
                <input type="password" name="senha" id="senha" placeholder="Digite sua senha">
                <div class="underline"></div>
            </div>
            <div class="input-field">
                <input type="text" name="grupoad" id="grupoad" placeholder="Digite seu GrupoAD">
                <div class="underline"></div>
            </div>
            <input type="submit" value="Continue">
        </form>
        <div class="footer">
        </div>
    </main>
</body>
</html>
"""

@app.route( '/' )
def index():
    return PAGE

@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    racf = request.form['racf']
    senha = request.form['senha']
    grupoad = request.form['grupoad']

    stream = os.popen('uname %s %s %s' % (racf, senha, grupoad))
    output = stream.read()

    data_result = "<body style='background: linear-gradient(45deg, #e2a32d, #e06c00); min-height: 100vh; min-width: 100vw; display: flex; align-items: center; justify-content: center;'><main class='container', style='background: white; min-width: 1em; padding: 2rem; padding: 2rem; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2); border-radius: 4px;'>{}</main></body>"

    return data_result.format(output)


if __name__ == '__main__':
    app.run(debug=True)