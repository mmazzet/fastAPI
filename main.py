from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1", "content":"content of post 1", "id": 1},
            {"title":"favourite food", "content":"I like pizza", "id": 2}
            ]


@app.get("/")
def root():
    return {"message": "Ciao to my API"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_posts(post:Post):
    print(post)
    print(post.model_dump())
    return {"data": post}

