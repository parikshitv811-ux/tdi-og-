import os
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="SONIQ AI Music Backend Engine", version="2.5")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("generated_audio", exist_ok=True)
app.mount("/audio", StaticFiles(directory="generated_audio"), name="audio")

class MusicGenerationRequest(BaseModel):
    prompt: str
    bpm: int = 128
    style: str = "General"
    model: str = "AudioCraft"
    vocal_model: str = "TCSinger"
    duration: int = 60
    language: str = "Rajasthani"
    quality: str = "High Quality"

@app.get("/")
def read_root():
    return {
        "status": "online",
        "engine": "SONIQ AI Music Pipeline",
        "supported_models": [
            "AudioCraft", "DiffRhythm", "ACE-Step", "HeartMuLa",
            "YuE", "Stable Audio", "Amphion", "Riffusion", "MusicLM-PyTorch"
        ]
    }

@app.post("/generate")
async def generate_music(request: MusicGenerationRequest):
    try:
        track_id = str(uuid.uuid4())[:8]
        filename = f"generated_audio/soniq_{track_id}.mp3"

        # In production pipeline:
        # 1. Calls backend.models.audiocraft_engine or diffrhythm / yue
        # 2. Applies TCSinger / RVC v2 vocal layer if lyrics provided
        # 3. Runs Demucs stem separation & Matchering audio mastering
        
        # Placeholder response pointing to generated audio file URL
        return {
            "status": "completed",
            "track_id": track_id,
            "prompt": request.prompt,
            "model": request.model,
            "bpm": request.bpm,
            "duration": request.duration,
            "audio_url": f"http://localhost:8000/audio/soniq_{track_id}.mp3"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
