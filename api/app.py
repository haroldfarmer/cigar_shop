from flask import Flask, request, redirect
from flask_cors import CORS
import db_api

app = Flask(__name__)
CORS(app)

@app.route('/get')
def get_cigar():
    test = request.args.get('brand')
    results = db_api.query_cigars(brand=test)
    return results

@app.route('/post')
def delete_cigar(id):
    id = request.args.get('id')
    pass

if __name__ == "__main__":
    app.run(debug=True)