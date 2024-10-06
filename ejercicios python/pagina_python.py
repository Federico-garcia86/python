from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def form():
    return render_template('form.html')

# Ruta para recibir el formulario y mostrar el resultado
@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        nombre = request.form['nombre']  # Tomamos el dato del formulario
        return f'¡Hola, {nombre}!'  # Mostramos el nombre ingresado

if __name__ == '__main__':
    app.run(debug=True)

