from flask import jsonify, request

# Sample data
users = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Smith'}
]

def register_routes(app):
    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users), 200

    @app.route('/users', methods=['POST'])
    def create_user():
        new_user = request.get_json()
        users.append(new_user)
        return jsonify({'message': 'User added', 'user': new_user}), 201

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user_by_id(user_id):
        user = next((u for u in users if u['id'] == user_id), None)
        if user:
            return jsonify(user), 200
        return jsonify({'message': 'User not found'}), 404
