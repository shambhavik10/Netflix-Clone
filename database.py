import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()


def get_supabase() -> Client:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        raise RuntimeError(
            "Missing Supabase configuration. Set SUPABASE_URL and SUPABASE_KEY "
            "in your environment or local .env file."
        )

    return create_client(supabase_url, supabase_key)
