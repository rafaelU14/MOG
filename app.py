from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    # Extraemos los datos del JSON (convertidos a float para mayor precisión)
    looks = float(data.get('v1', 5))     # How good looking are you?
    goodness = float(data.get('v2', 5))  # How would you rate yourself as a person?
    quirky = float(data.get('v3', 5))    # How quirky are you?
    books = float(data.get('v4', 5))     # How many books do you read a year?

    # Aplicamos tu fórmula:
    # MOG score = (Books / 20) + (((Quirky * (Looks - 7) - 30) / 20) + 5) + (Goodness / 4)
    
    term_books = books / 20
    term_quirky_looks = (((quirky * (looks - 7)) - 30) / 20) + 5
    term_goodness = goodness / 4
    
    score = term_books + term_quirky_looks + term_goodness
    
    # Redondeamos a 2 decimales
    final_score = round(score, 2)

    # Clasificación basada en el score
    if final_score >= 8:
        category = "Elite Mogger 🗿"
    elif final_score >= 5:
        category = "Solid Presence"
    else:
        category = "Needs more aura"

    return jsonify({
        'score': final_score,
        'category': category
    })

if __name__ == '__main__':
    app.run(debug=True)