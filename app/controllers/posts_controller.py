from flask import Flask, jsonify, request
from app.models.exception import InvalidKeyError, InvalidValueError, RequiredKeyError

from app.models.post_model import Post


def posts_controller(app: Flask):
    @app.route('/posts', methods=['GET'])
    def read_posts():
        list_posts = Post.get_all_posts()
        return jsonify(list_posts), 200

    @app.route('/posts/<int:id>', methods=['GET'])
    def read_post_by_id(id: int):
        try:
            post = Post.get_post_id(id)
            return jsonify(post), 200
        except TypeError:
            return {"error": "post not found"}, 404

    @app.route('/posts', methods=['POST'])
    def create_post():
        try:
            data = request.get_json()
            Post.validate_key(data)
            Post.validate_required(data)
            Post.validate_value(data)
        except RequiredKeyError as err:
            return jsonify(err.__dict__['message']), 400
        except InvalidValueError as err:
            return jsonify(err.__dict__['message']), 400
        except InvalidKeyError as err:
            return jsonify(err.__dict__['message']), 400
        post = Post(**data) 
        post.generate_id()
        new_post = post.save()
        return jsonify(new_post), 201

    @app.route('/posts/<int:id>', methods=['PATCH'])
    def update_post(id: int):
        try:
            data = request.get_json()
            Post.validate_key(data)
            Post.validate_value(data)
        except TypeError:
            return {"error": "post not found"}, 404
        except InvalidKeyError as err:
            return jsonify(err.__dict__['message']), 400
        except InvalidValueError as err:
            return jsonify(err.__dict__['message']), 400
        new_post = Post.post_update(id, data)
        return jsonify(new_post), 200

    @app.route('/posts/<int:id>', methods=['DELETE'])
    def delete_post(id: int):
        try:
            post = Post.post_delete(id)
            return jsonify(post), 200
        except TypeError:
            return {"error": "post not found"}, 404 