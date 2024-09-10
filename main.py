from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"Hello": "FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data": "Here are your post data!"}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    return {"post": post}



@app.get("/users")
def get_users():
    pass