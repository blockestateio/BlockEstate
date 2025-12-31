from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.website_manager import website_manager
from utils.config import config

app = FastAPI(title="BlockEstate Automation API")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class HomeUpdate(BaseModel):
    text: str

class AnnouncementModel(BaseModel):
    title: str
    content: str

class UserQuery(BaseModel):
    name: str
    email: str
    message: str

# Endpoints
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/update_home")
def update_home(update: HomeUpdate):
    return website_manager.update_homepage_message(update.text)

@app.post("/send_announcement")
def send_announcement(announcement: AnnouncementModel):
    return website_manager.post_news_update(announcement.title, announcement.content)

@app.get("/stats")
def get_stats():
    return website_manager.fetch_token_stats()

@app.post("/contact")
def contact_form(query: UserQuery):
    return website_manager.save_user_query(query.name, query.email, query.message)

def run_api():
    import uvicorn
    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)
