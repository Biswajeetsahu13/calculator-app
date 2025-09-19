from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Safe evaluation: only allow basic operations
        allowed = {'+','-','*','/','(',')','.'}
        if not all(c.isdigit() or c in allowed for c in expression):
            return jsonify({"error": "Invalid input"})

        result = eval(expression)  # In real apps, use a safe parser
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
