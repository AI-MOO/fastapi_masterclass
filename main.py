from fastapi import FastAPI
from enum import Enum 
from typing import Optional
from fastapi import status, Response 
# fastapi object 
app = FastAPI()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/')
def index():
    return {'message': 'Hello World !!!'}

# @app.get('/blog/all')
# def get_all_blogs(page = 1, page_size = 10):
#     return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/all', tags=['blog'], 
         summary='Get all blogs', 
         description='This api call returns all blogs.',
         response_description='List of available blogs')
def get_all_blogs(page = 1, page_size:Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

# @app.get('/blog/{id}/comments/{comment_id}')
# def get_comment(id:int, comment_id:int, valid:bool=True, username:Optional[str]=None):
#     return {'message': f'blog_id {id}, comment_id {comment_id}, valid: {valid}, username: {username}'}
@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id:int, comment_id:int, valid:bool=True, username:Optional[str]=None):
    """
    Simulates retrieving a comment of a blog
    - **id**: mandatory path parameter, blog id
    - **comment_id**: mandatory path parameter, comment id   
    - **valid**: optional query parameter
    - **username**: optional query parameter
    """

    return {'message': f'blog_id {id}, comment_id {comment_id}, valid: {valid}, username: {username}'}


# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'all blog ids provided' } 

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f"Blog type is {type}"}

# @app.get('/blog/{id}')
# def get_blog(id: int):
#     return {'message': f"Blog with id {id}"}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f"Blog with id {id}"}