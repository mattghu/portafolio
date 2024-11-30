from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def form():
    return render_template('form.html')

# Ruta para procesar los datos del formulario
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    date = request.form.get('date')
    
    return render_template('form_result.html',
                           name=name,
                           email=email,
                           address=address,
                           date=date)

if __name__ == '__main__':
    app.run(debug=True)
