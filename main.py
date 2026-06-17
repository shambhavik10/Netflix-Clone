from fastapi import FastAPI
from database import supabase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Netflix Backend Running"}


@app.get("/test")
def test():

    response = (
        supabase
        .table("users")
        .select("*")
        .execute()
    )

    return response.data


@app.get("/add-user")
def add_user():

    response = (
        supabase
        .table("users")
        .insert({
            "email": "test@gmail.com",
            "password": "123456"
        })
        .execute()
    )

    return response.data


@app.post("/login")
def login(email: str, password: str):

    response = (
        supabase
        .table("users")
        .select("*")
        .eq("email", email)
        .eq("password", password)
        .execute()
    )

    if response.data:
        return {"message": "Login Successful"}

    return {"message": "Invalid Email or Password"}
@app.get("/movies")
def get_movies():

    response = (
        supabase
        .table("movies")
        .select("*")
        .execute()
    )

    return response.data