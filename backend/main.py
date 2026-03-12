from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from database import engine, SessionLocal
from models import Base, SearchHistory

from ai_engine import classify_task, generate_options, generate_full_response
from tool_recommender import tool_recommender

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


class PromptRequest(BaseModel):
    prompt: str


class ContentRequest(BaseModel):
    prompt: str
    sections: list



@app.post("/analyze")
async def analyze(data: dict):

    prompt = data.get("prompt")

    category = classify_task(prompt)

    ai_response = generate_full_response(prompt)

    return {
        "category": category,
        "ai_response": ai_response
    }

@app.post("/generate")

async def generate(data: ContentRequest):

    content = generate_full_response(data.prompt, data.sections)

    db = SessionLocal()

    history = SearchHistory(
        user_prompt=data.prompt,
        ai_response=content
    )

    db.add(history)
    db.commit()
    db.close()

    return {"content": content}


app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)