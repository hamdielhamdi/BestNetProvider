from flask import Flask, request


from .utils import workflow



app = Flask(__name__)




@app.route('bestprovider/')
def netprovider():
    query = request.args.get('q')
    
    result = workflow(q)

    