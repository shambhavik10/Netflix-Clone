from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import get_supabase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Netflix Backend Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


def run_supabase_query(query):
    try:
        return query.execute().data
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Supabase request failed: {exc}",
        ) from exc


def supabase_client():
    try:
        return get_supabase()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/test")
def test():
    supabase = supabase_client()
    return run_supabase_query(supabase.table("users").select("*"))


@app.get("/add-user")
def add_user():
    supabase = supabase_client()

    # Demo-only user seed. Real production apps should use Supabase Auth
    # or password hashing instead of storing raw passwords.
    query = supabase.table("users").insert(
        {
            "email": "test@gmail.com",
            "password": "123456",
        }
    )

    return run_supabase_query(query)


@app.post("/login")
def login(email: str, password: str):
    supabase = supabase_client()

    # Demo-only login for the college project. Real production apps should
    # use Supabase Auth or hashed passwords instead of comparing raw values.
    users = run_supabase_query(
        supabase.table("users")
        .select("*")
        .eq("email", email)
        .eq("password", password)
    )

    if users:
        return {"message": "Login Successful"}

    return {"message": "Invalid Email or Password"}


@app.get("/movies")
def get_movies():
    supabase = supabase_client()
    return run_supabase_query(supabase.table("movies").select("*"))
