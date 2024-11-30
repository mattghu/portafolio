from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def form():
    return render_template('form.html')

# Ruta para procesar los datos del formulario
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        date = request.form.get('date')
        
        # Guardar los datos en un archivo .txt
        with open("data.txt", "a") as file:
            file.write(f"Nombre: {name}\n")
            file.write(f"Correo: {email}\n")
            file.write(f"Dirección: {address}\n")
            file.write(f"Fecha: {date}\n")
            file.write("="*20 + "\n")  # Separador entre entradas
        
        # Renderizar la plantilla de resultados
        return render_template('form_result.html', name=name, email=email, address=address, date=date)
    
    return "Método no permitido", 405

if __name__ == '__main__':
    app.run(debug=True)
