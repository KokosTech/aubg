from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    try: 
        name = request.json.get('name', 'N/A')
    except Exception as e:        
        return make_response(
            jsonify({
                'error': 'Unsupported Media Type. Please send JSON data.'
            }),
            415
        )
    
    return make_response(
        jsonify({
            'message': 'Hello, ' + name + '!'
        }),
    )

@app.route('/name/<name>/age/<age>', methods=['GET'])
def get_name_and_age(name, age):
    return make_response(
        jsonify({
            'name': name,
            'age': age
        }),
        200
    )

if __name__ == '__main__':
    app.run(debug=True)