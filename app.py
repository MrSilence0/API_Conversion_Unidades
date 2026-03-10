from flask import Flask, request, jsonify

app = Flask(__name__)

ultima_conversion = {}

@app.route('/api/fahrenheit', methods=['POST'])
def celsius_to_fahrenheit():
    global ultima_conversion
    datos = request.get_json()
    
    temp_c = datos.get('temperatura_celsius')
    
    # Validación: Que exista y que sea un número (int o float)
    if temp_c is None or not isinstance(temp_c, (int, float)):
        return jsonify({'error': 'Proporcione una temperatura_celsius válida (numérica)'}), 400

    temp_f = (temp_c * 9/5) + 32
    
    ultima_conversion = {
        'temperatura_celsius': temp_c,
        'temperatura_fahrenheit': round(temp_f, 2) # Redondeamos a 2 decimales
    }
    return jsonify({'ultima_conversion': ultima_conversion})

@app.route('/api/celsius', methods=['POST'])
def fahrenheit_to_celsius():
    global ultima_conversion
    datos = request.get_json()
    temp_f = datos.get('temperatura_fahrenheit')
    
    if temp_f is None or not isinstance(temp_f, (int, float)):
        return jsonify({'error': 'Proporcione una temperatura_fahrenheit válida (numérica)'}), 400

    temp_c = (temp_f - 32) * 5/9
    
    ultima_conversion = {
        'temperatura_fahrenheit': temp_f,
        'temperatura_celsius': round(temp_c, 2)
    }
    return jsonify({'ultima_conversion': ultima_conversion})

@app.route('/api/ultima-conversion', methods=['GET'])
def obtener_ultima_conversion():
    if not ultima_conversion:
        return jsonify({'message': 'No se ha realizado ninguna conversión aún'}), 200 # 200 es mejor si está vacío pero funciona
    return jsonify({'ultima_conversion': ultima_conversion})    

if __name__ == '__main__':
    app.run(debug=True)