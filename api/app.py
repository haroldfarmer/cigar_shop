from flask import Flask, request, redirect
import db_api

app = Flask(__name__)

@app.route('/get')
def get_cigar():
    test = request.args.get('brand')
    print(test)
    results = db_api.query_cigars(brand=test)
    return results

@app.route('/post')
def delete_cigar(id):
    id = request.args.get('id')
    pass

if __name__ == "__main__":
    app.run(debug=True)