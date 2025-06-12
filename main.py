# main.py

from fastapi import FastAPI

# Import routers
from routers import user, event, speaker, register

# Create FastAPI app instance
app = FastAPI(
    title="Event Management API System",
    description="This system allows users to register for events, track attendance, and manage both event information and speaker details.",
    version="1.0.0"
)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(event.router, prefix="/events", tags=["Events"])
app.include_router(speaker.router, prefix="/speakers", tags=["Speakers"])
app.include_router(register.router, prefix="/registrations", tags=["Registrations"])


@app.get("/")
async def home():
    return {"message": "Welcome home"}