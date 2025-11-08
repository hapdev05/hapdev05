from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from typing import List

app = FastAPI(title="Smart P2P File Classifier")


class ClassificationRequest(BaseModel):
    file_name: str
    mime_type: str | None = None
    tags: List[str] | None = None


class ClassificationResponse(BaseModel):
    label: str
    confidence: float


def load_model() -> None:
    """Placeholder for loading the actual ML model from disk."""
    models_path = Path("/opt/models/latest")
    models_path.mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
async def startup_event() -> None:
    load_model()


@app.post("/classify", response_model=ClassificationResponse)
async def classify(request: ClassificationRequest) -> ClassificationResponse:
    """Dummy implementation that infers the label from the file extension."""
    ext = Path(request.file_name).suffix.lower()
    if ext in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".img"}:
        return ClassificationResponse(label="image", confidence=0.85)
    if ext in {".mp4", ".mkv", ".avi"}:
        return ClassificationResponse(label="video", confidence=0.8)
    if ext in {".mp3", ".wav", ".flac"}:
        return ClassificationResponse(label="audio", confidence=0.75)
    return ClassificationResponse(label="document", confidence=0.6)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
