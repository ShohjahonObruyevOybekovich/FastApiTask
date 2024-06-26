from fastapi import FastAPI
from app.tasks.routes import task_router
from app.auth.routes import router
from app.db import init_db

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(router, prefix="/auth", tags=["auth"])

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Add other necessary configurations and middlewares
