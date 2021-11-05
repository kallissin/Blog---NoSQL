from flask import Flask, jsonify, request

from app.models.post_model import Post


def posts_controller(app: Flask):
    @app.route('/posts', methods=['GET'])
    def read_posts():
        list_posts = Post.get_all_posts()
        return jsonify(list_posts), 200

    @app.route('/posts/<int:id>', methods=['GET'])
    def read_post_by_id(id: int):
        post = Post.get_post_id(id)
        return jsonify(post), 200
    
    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        post = Post(**data) 
        post.generate_id()
        new_post = post.save()
        return jsonify(new_post), 201

    @app.route('/posts/<int:id>', methods=['PATCH'])
    def update_post(id: int):
        data = request.get_json()
        new_post = Post.post_update(id, data)
        return jsonify(new_post), 200
    
    @app.route('/posts/<int:id>', methods=['DELETE'])
    def delete_post(id: int):
        Post.post_delete(id)
        return {}, 204