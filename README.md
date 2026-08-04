# 🎵 SONIQ AI - Universal Open-Source AI Music Generator Studio

> **Production-grade AI Music Generation Platform specializing in Global Genres & Regional Indian Music Intelligence (Marwadi Folk, Rajasthani Manganiyar, Punjabi Bhangra, Gujarati Garba, Carnatic & Bollywood Fusion).**

[![View Source on GitHub](https://img.shields.io/badge/GitHub-View%20Source-00f2fe?style=for-the-badge&logo=github)](https://github.com/parikshitv811-ux/tdi-og-)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1%2B-EE4C2C?style=for-the-badge&logo=pytorch)](https://pytorch.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)

---

## 🌟 Overview

**SONIQ AI** is a complete open-source alternative to commercial AI music generation platforms (such as Suno, Udio, and Midjourney for audio). It provides:

1. **Frontend Studio (`index.html`)**: Single-file glassmorphic dark-theme UI with responsive audio visualizers, stems mixer station, prompt tags, regional preset selector, and in-browser Web Audio API synthesis fallback.
2. **PyTorch FastAPI Backend (`backend/`)**: High-performance backend integrating state-of-the-art open-source audio foundation models.
3. **Regional Indian Music Pipeline (`backend/indian_ai/` & `backend/training/`)**: LoRA fine-tuning for Meta AudioCraft (MusicGen), TCSinger for vocal synthesis, RVC v2 for regional voice conversion, and AI4Bharat IndicTTS for Indian language phonetics.

---

## 🚀 Supported Open-Source AI Music Frameworks & Models

| Model / Framework | Repository | Capabilities |
| :--- | :--- | :--- |
| **AudioCraft (MusicGen)** | `facebookresearch/audiocraft` | Text-to-Music, Melody conditioning, AudioGen, EnCodec |
| **DiffRhythm** | `ASLP-lab/DiffRhythm` | High-speed latent diffusion for full song generation |
| **ACE-Step** | `ACE-Step` | Open foundation model for music editing, continuation & remixing |
| **HeartMuLa** | `HeartMuLa/heartlib` | Complete ecosystem (HeartCodec, HeartTranscriptor, HeartCLAP) |
| **YuE** | `multimodal-art-projection/YuE` | Lyrics-to-Song full vocal & instrumental generation |
| **Stable Audio Tools** | `stability-ai/stable-audio-tools` | Stability AI diffusion framework for professional audio |
| **Amphion** | `open-mmlab/Amphion` | Voice conversion, singing voice synthesis (SVS), and TTS |
| **Riffusion** | `riffusion/riffusion` | Spectrogram diffusion music generation |
| **MusicLM-PyTorch** | `lucidrains/musiclm-pytorch` | Open PyTorch implementation of Google's MusicLM |
| **TCSinger & RVC v2** | `RVC-Project/Retrieval-based-Voice-Conversion-WebUI` | Zero-shot singing synthesis & regional voice conversion |
| **AI4Bharat IndicTTS** | `AI4Bharat/Indic-TTS` | Indian regional language pronunciation & phoneme parsing |
| **Demucs** | `facebookresearch/demucs` | Multitrack stem separation (Drums, Bass, Synth, Vocals) |

---

## 📂 Repository Structure

```
.
├── index.html                   # Single-file Web Studio (Glassmorphic UI, Visualizer, Web Audio API)
├── README.md                    # Project Documentation
├── requirements.txt             # Python Dependencies
├── Dockerfile                   # CUDA GPU Docker Setup
└── backend/
    ├── main.py                  # FastAPI Generation Endpoint (/generate)
    ├── models/
    │   ├── audiocraft_engine.py # Meta AudioCraft / MusicGen Loader
    │   ├── diffrhythm_engine.py # DiffRhythm Diffusion Engine
    │   └── yue_engine.py        # YuE Lyrics-to-Song Engine
    ├── vocals/
    │   └── tcsinger_rvc.py      # TCSinger & RVC v2 Voice Layer
    ├── indian_ai/
    │   └── indic_processor.py   # AI4Bharat Language Phoneme Pipeline
    ├── audio_engine/
    │   └── mixer_mastering.py   # Demucs Stem Separator & Matchering Mastering
    └── training/
        └── train_lora_musicgen.py # PyTorch LoRA Fine-Tuning Script for Indian Instruments
```

---

## ⚡ Quick Start

### 1. Launch Frontend (Standalone)
Simply open `index.html` in any modern web browser (Chrome, Firefox, Edge, Safari).
If no backend is connected, the built-in **Web Audio API Engine** will generate audio directly inside your browser!

### 2. Run Python PyTorch Backend Server
```bash
# Clone the repository
git clone https://github.com/parikshitv811-ux/tdi-og-.git
cd tdi-og-

# Install dependencies
pip install -r requirements.txt

# Start FastAPI GPU Backend Server
python backend/main.py
```
The server will run on `http://localhost:8000`. You can test the generation endpoint via:
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "Marwadi wedding folk song with dholak, algoza and female vocals",
       "bpm": 128,
       "model": "AudioCraft",
       "vocal_model": "TCSinger",
       "duration": 60
     }'
```

### 3. Fine-Tune MusicGen on Regional Indian Instruments (LoRA)
To train the model on custom datasets (e.g. Dholak, Kamaycha, Algoza, Ravanahatha, Tabla, Tumbi):
```bash
python backend/training/train_lora_musicgen.py \
    --dataset_path ./data/indian_folk \
    --epochs 50 \
    --output_dir ./checkpoints/musicgen_indian_lora
```

---

## 🔗 Repository Link
View source code & updates on GitHub:  
[https://github.com/parikshitv811-ux/tdi-og-](https://github.com/parikshitv811-ux/tdi-og-)
