from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/confirmacion', methods=['POST'])
def confirmacion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        destino = request.form.get('destino', 'Ningún destino seleccionado')
        fecha = request.form.get('fecha', 'Ninguna fecha seleccionada')
        necesidades = request.form.getlist('necesidades')

        return render_template('confirmacion.html', nombre=nombre, destino=destino, fecha=fecha, necesidades=necesidades)

if __name__ == '__main__':
    app.run(debug=True)
