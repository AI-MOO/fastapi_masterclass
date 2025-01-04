from fastapi import FastAPI
from enum import Enum 
# fastapi object 
app = FastAPI()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/')
def index():
    return {'message': 'Hello World !!!'}

@app.get('/blog/all')
def get_all_blogs():
    return {'message': 'all blog ids provided' } 

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f"Blog with id {id}"}
