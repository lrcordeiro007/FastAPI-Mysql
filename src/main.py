from fastapi import FastAPI, HTTPException, Depends, status, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from starlette.middleware.sessions import SessionMiddleware
import os

SECRET_KEY = os.urandom(32).hex()

app = FastAPI()

templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)
app.add_middleware(SessionMiddleware, secret_key = SECRET_KEY)


class Post(BaseModel):
    content : str
    user_id: int

class User(BaseModel):
    username : str
    password : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", response_class= HTMLResponse )
async def start(request : Request):
   return templates.TemplateResponse("start.html", {"request" : request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login", response_class = HTMLResponse)
async def login(
    request : Request,
    db: Session = Depends(get_db),
    username: str = Form(...),
    password: str = Form (...)
):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user or not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": " Invalid username or password"},
            status_code= status.HTTP_401_UNAUTHORIZED
        )
    request.session["user_id"]= user.id
    
    response = RedirectResponse(url = "/welcome", status_code=status.HTTP_303_SEE_OTHER)
    return response

@app.get("/register", response_class = HTMLResponse)
async def register_page(request : Request):
    return templates.TemplateResponse("/register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(
    request: Request,
    db: Session = Depends(get_db),
    username: str = Form(...),
    password: str = Form(...)
):
    existing_user = db.query(models.User).filter(models.User.username == username).first()
    if existing_user:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Nome de usuário já existe."},
            status_code=status.HTTP_409_CONFLICT
        )
    
    hashed_password = pwd_context.hash(password)

    new_user = models.User(username=username, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    response = RedirectResponse(url="/login",status_code=status.HTTP_303_SEE_OTHER)
    return response

@app.get("/welcome", response_class = HTMLResponse)
async def welcome(request : Request):
    return templates.TemplateResponse("/welcome.html", {"request": request})

@app.post("/welcome", response_class= HTMLResponse)
async def welcome_page(
        request : Request,
    db: Session = Depends(get_db),
    post: str = Form(...)
):
    user_id = request.session.get("user_id")

    new_post = models.Post(post = post, user_id = user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return templates.TemplateResponse("/welcome.html", {"request": request})




@app.get("/post/{post_id}", status_code= status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code = 404, detail= "Post not found")
    return post

@app.post("/post/", status_code = status.HTTP_201_CREATED)
async def create_post(post: Post, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int , db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code= 404, detail= 'User not found')
    return user

if __name__ == "__main__":
  import uvicorn 
  uvicorn.run(app,
  host="0.0.0.0", port=8000,
  reload = True)