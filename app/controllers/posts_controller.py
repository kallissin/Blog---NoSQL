from flask import Flask


def posts_controller(app: Flask):
    @app.route('/posts', methods=['GET'])
    def read_posts():
        ...

    @app.route('/posts/<int:id>', methods=['GET'])
    def read_post_by_id(id: int):
        ...
    
    @app.route('/posts', methods=['POST'])
    def create_post():
        ...
    
    @app.route('/posts/<int:id>', methods=['PATCH'])
    def update_post(id: int):
        ...
    
    @app.route('/posts/<int:id>', methods=['DELETE'])
    def delete_post(id: int):
        ...