from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

# Connect to Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# User model
class User(BaseModel):
    email: str


# Home route
@app.get("/")
def home():
    return {"message": "Hello World"}


# Health check route
@app.get("/health")
def health():
    return {"status": "ok"}


# Create user
@app.post("/users")
def create_user(user: User):

    result = supabase.table("users").insert(
        {
            "email": user.email
        }
    ).execute()

    return result.data


# Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: str):

    result = (
        supabase.table("users")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    if not result.data:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result.data[0]