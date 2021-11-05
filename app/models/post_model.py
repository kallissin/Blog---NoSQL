from datetime import datetime
from app.models import db

class Post:
    def __init__(self, title: str, author: str, tags: list, content: str):
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
    
    @staticmethod
    def get_all_posts():
        post_list = list(db.posts.find())
        for post in post_list:
            del post['_id']
        return post_list
    
    @staticmethod
    def get_post_id(id):
        post = db.posts.find_one({"id": id})
        del post['_id']
        return post

    def generate_id(self):
        try:
            data = list(db.posts.find())
            self.id = data[-1]['id'] + 1
        except IndexError:
            self.id = 1

    def save(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        post = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content,
            "created_at": self.created_at,
            "update_at": self.updated_at
        }      

        _id = db.posts.insert_one(post).inserted_id
        new_post = db.posts.find_one(_id)
        del new_post['_id']
        return new_post 
    
    @staticmethod
    def post_update(id, data):
        post = db.posts.find_one_and_update({"id": id}, {"$set": data})
        del post['_id']
        return post
    
    @staticmethod
    def post_delete(id):
        db.posts.find_one_and_delete({"id": id})
        