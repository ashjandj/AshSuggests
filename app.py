from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_folder='static')

# Load product data from a JSON file
def load_products():
    with open('products.json', 'r') as file:
        return json.load(file)

products = load_products()

@app.route('/')
def home():
    return render_template('index.html')  # assuming your HTML is index.html in templates folder

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = [product for product in products if query in product['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
