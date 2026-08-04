# 🎵 SONIQ AI - Universal Real AI Music Production Platform

> **Production AI Music Generation Platform connected to PyTorch Audio Models (Meta AudioCraft MusicGen, ACE-Step, YuE, DiffRhythm, HeartMuLa) specializing in Global & Regional Indian Music (Marwadi Folk, Rajasthani Manganiyar, Punjabi Bhangra, Gujarati Garba, Carnatic & Bollywood Fusion).**

[![View Source on GitHub](https://img.shields.io/badge/GitHub-View%20Source-00f2fe?style=for-the-badge&logo=github)](https://github.com/parikshitv811-ux/tdi-og-)
[![Backend Status](https://img.shields.io/badge/FastAPI%20Backend-Online-10b981?style=for-the-badge)](#-fastapi-backend-server)

---

## ⚡ Architecture Update: Pure AI Music Pipeline

This platform communicates strictly with a **Python PyTorch FastAPI Backend API**. Browser Web Audio tone generators and fake oscillator fallbacks have been completely removed.

```
User Prompt

↓

Studio Frontend (index.html)

↓

FastAPI Endpoint (POST http://localhost:8000/generate)

↓

PyTorch AI Music Model (MusicGen / ACE-Step / YuE / DiffRhythm)

↓

Quality Validation Gate & Pedalboard Mastering

↓

WAV / MP3 Output File

↓

HTML5 Audio Player & 1-Click Track Download
```

---

## 🚀 Running the Server & Web Studio

### 1. Launch FastAPI Backend Server
```bash
# Clone the repository
git clone https://github.com/parikshitv811-ux/tdi-og-.git
cd tdi-og-

# Install PyTorch & dependencies
pip install -r requirements.txt

# Run FastAPI Server
python backend/main.py
```
The backend API will start on `http://localhost:8000`.

### 2. Open Web Studio
Open `index.html` in Chrome or Edge.
The status badge in the header will display:  
**`AI Backend Connected ✓ (CUDA GPU Active)`**

---

## 🔗 Repository
[https://github.com/parikshitv811-ux/tdi-og-](https://github.com/parikshitv811-ux/tdi-og-)
