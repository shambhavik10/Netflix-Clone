from supabase import create_client

SUPABASE_URL = "https://wxmznbtsceiijhhuflzn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4bXpuYnRzY2VpaWpoaHVmbHpuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE1ODA3NTcsImV4cCI6MjA5NzE1Njc1N30.Ctuu2BwnZvtbPghkg9rrync75NV-RM6a9tTPNt-jR7Q"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)