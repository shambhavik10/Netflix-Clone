# Deployment Guide

This project is split into three deployment parts:

- Frontend: Vercel static site
- Backend: Render FastAPI web service
- Database: Supabase

## Backend on Render

Create a new Render service with these settings:

- Service Type: Web Service
- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

Add these Render environment variables:

```text
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_or_service_key
```

Do not commit real Supabase values to GitHub. Use Render environment variables for production and a local `.env` file for development.

After Render deploys, copy the backend URL and confirm these endpoints work:

- `https://your-render-service.onrender.com/`
- `https://your-render-service.onrender.com/health`
- `https://your-render-service.onrender.com/docs`

## Frontend on Vercel

Deploy the repository to Vercel with these settings:

- Framework Preset: Other
- Root Directory: `./`
- Build Command: None
- Output Directory: `.`
- Install Command: Empty

The included `vercel.json` keeps Vercel configured as a static frontend deploy.

## Frontend API URL

In `script.js`, set:

```js
const API_BASE_URL = "https://your-render-service.onrender.com";
```

The frontend uses that URL to call the Render backend:

- `POST /login`
- `GET /movies`

## Local Development

Create a local `.env` file based on `.env.example`:

```text
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn main:app --reload
```

Open these backend URLs:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

Open `index.html` and `browse.html` in a browser to test the frontend.
