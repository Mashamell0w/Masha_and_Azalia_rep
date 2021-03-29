from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My_Store',
        'items': [
            {
                'item_name': 'Chair',
                'price': 1500
            },
            {
                'item_name': 'Cup',
                'price': 77
            }
        ]
    }
]


# POST /store -> name
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    store = {
        'name': data['name'],
        'items': []
    }
    stores.append(store)
    return store


# GET /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<name>/item -> name, price
@app.route('/store/<string:name>', methods=['POST'])
def create_item(name):
    data = request.get_json()
    item = {'item_name': data['item_name'], 'price': data['price']}
    for store in stores:
        if store['name'] == name:
            store['items'].append(item)
            return item


# GET /store/<name>/item
@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])


if __name__ == '__main__':
    app.run(debug=True)
