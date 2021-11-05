from datetime import datetime
from app.models import db
from app.models.exception import InvalidKeyError,InvalidValueError, RequiredKeyError

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
    
    @staticmethod
    def validate_required(data):
        keys_data = list(data.keys())
        model_required = ['title', 'author', 'tags', 'content']
        if keys_data != model_required:    
            raise RequiredKeyError(data)

    @staticmethod
    def validate_value(data):
        model_value = {
            "title": str,
            "author": str,
            "tags": list,
            "content": str
        }
        for key, value in data.items():
            if type(value) !=  model_value[key]:
                raise InvalidValueError(data)
    
    @staticmethod
    def validate_key(data):
        model_key = ['title', 'author', 'tags', 'content']
        for key in data.keys():
            if key not in model_key:
                raise InvalidKeyError(data)

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
            "updated_at": self.updated_at
        }      

        _id = db.posts.insert_one(post).inserted_id
        new_post = db.posts.find_one(_id)
        del new_post['_id']
        return new_post 
    
    @staticmethod
    def post_update(id, data):
        data['updated_at'] = datetime.now()
        print(data)
        post = db.posts.find_one_and_update({"id": id}, {"$set": data})
        del post['_id']

        return post
    
    @staticmethod
    def post_delete(id):
        post = db.posts.find_one_and_delete({"id": id})
        del post['_id']
        return post