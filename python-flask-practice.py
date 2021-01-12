from flask import Flask,render_template,request,jsonify
from flask_json import FlaskJSON,JsonError,json_response,as_json
from flask_cors import CORS,cross_origin
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

app = Flask(__name__)
json = FlaskJSON(app)
app.config["DEBUG"] = True

books = [
    { 'id':1,'author':'Stephen King','title':'The Outsider' },
    { 'id':2,'author':'Stephen King','title':'Pet Sematary' },
    { 'id':3,'author':'Philip Roth','title':'American Pastoral' },
    { 'id':4,'author':'John Boyne','title':'The Heart\'s Invisible Furies' },
    { 'id':5,'author':'Hanya Yanagihara','title':'A Little Life' },
    { 'id':6,'author':'Donna Tartt','title':'The Secret History' }
]

# route to index page
@app.route('/',methods=["GET"])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/books/all',methods=['GET'])
@cross_origin()
def get_books():
    return jsonify(books)

# call here: http://127.0.0.1:5000/books/?id=1
@app.route('/books/',methods=['GET'])
@cross_origin()
def get_book_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = [] # results of search
    # loop through data and match id to results
    for i in range(len(books)):
        if books[i]['id'] == id:
            results.append(books[i])
    return jsonify(results)

#run the Flask app
if __name__ == '__main__':
    app.run()
