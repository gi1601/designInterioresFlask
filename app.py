from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

@app.route('/')
def design():
    return render_template('design.html', Titulo="Influenciers: ")

@app.route('/blog')
def blog():
    return render_template('blog.html', Titulo="Influenciers: ")

@app.route('/solicite')
def solicite():
    return render_template('solicite.html', Titulo="Influenciers: ")

if __name__ == '__main__':
    app.run()