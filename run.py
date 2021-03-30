from flask import Flask, request, jsonify
from utils.workflow import workflow


app = Flask(__name__)


@app.route('/bestprovider/', methods=['GET'])
def netprovider():
	
	query = request.args.get('q')
	
	if not query:
		return jsonify(message='A query should be defined, eg : 2 rue paul vaillant ..', status=404)

	result = workflow(query)

	return jsonify(message=str(result), status=200)


if __name__ == "__main__":
	app.run(debug=True)