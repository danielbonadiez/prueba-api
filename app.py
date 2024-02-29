# Importar el módulo Flask
from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Función de vista para la ruta '/personas'
@app.route('/personas', methods=['GET'])
def get_personas():
    
    # Lista de nombres de personas
    personas = [
        {'nombre': 'Juan'},
        {'nombre': 'María'},
        {'nombre': 'ramiro'},
        {'nombre': 'kiara'},
        {'nombre': 'Luis'},
    ]
    # Convertir la lista en formato JSON
    return jsonify(personas)

if __name__ == '__main__':
    app.run(debug=True)
