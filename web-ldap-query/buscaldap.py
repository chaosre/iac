

import flask
from flask import Flask, request, flash
from shelljob import proc

app = Flask(__name__)

PAGE = """
    <html>
        <head>
            <title>Buscaldap</title>
        </head>
        <body>
            <form action="/process" method="POST">
                <label>Racf</label>
                <input name="racf" />
                <br/><br/>
                <label>Senha</label>
                <input name="senha" />
                <br/><br/>
                <label>GrupoAD</label>
                <input name="grupoad" />
                <br/><br/>
                <input type="submit" />                
            </form>
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

    proc_group = proc.Group()
    run_shell = proc_group.run( [ "bash", "-c", "uname %s %s %s" % (racf,senha,grupoad) ] )

    def read_process():
        while proc_group.is_pending():
            lines = proc_group.readlines()
            for proc, line in lines:
                yield line

    return flask.Response( read_process(), mimetype= 'text/plain' )

if __name__ == '__main__':
    app.run(debug=True)