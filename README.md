# 🎵 SONIQ AI - High-Quality AI Music Production Platform

> **Studio-Grade AI Music Generation System featuring Noise-Free Synthesis, Negative Prompt Filtering, Post-Generation Quality Validation Gate, and Regional Indian Music Pipeline.**

[![View Source on GitHub](https://img.shields.io/badge/GitHub-View%20Source-00f2fe?style=for-the-badge&logo=github)](https://github.com/parikshitv811-ux/tdi-og-)
[![Audio Quality](https://img.shields.io/badge/Audio%20Quality-Clean%20%2F%2048kHz-10b981?style=for-the-badge)](#-audio-quality--noise-elimination)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1%2B-EE4C2C?style=for-the-badge&logo=pytorch)](https://pytorch.org)

---

## 🛠️ Noise Elimination & Quality Upgrades

1. **Studio Web Audio Synthesizer (`index.html`)**:
   - Polyphonic musical scale voicings (Pentatonic, Bhairav/Maand Indian Folk, Synthwave).
   - ADSR Gain Envelopes (Attack, Decay, Sustain, Release) on every note to eliminate clicks, digital pops, and static noise.
   - Lowpass Biquad filtering and soft peak limiter (-1.0dB threshold) preventing clipping distortion.
2. **Negative Prompt System (`backend/prompt_engine/enhancer.py`)**:
   - Automatic injection of negative prompts (`"noise, static, distortion, clipping, non-harmonic sound, broken audio, erratic frequencies"`) to suppress unwanted acoustic artifacts during AI inference.
3. **Quality Validation Gate (`backend/audio_processing/validator.py`)**:
   - Inspects RMS energy, peak dB ceiling, silence, and file corruption after generation. Automatically regenerates if audio quality drops.
4. **Mastering Engine (`backend/audio_engine/mastering.py`)**:
   - 3-band EQ, sub-rumble cut (below 30Hz), dynamic compression, and loudness normalization.

---

## 📂 Repository Structure

```
.
├── index.html                      # Studio Web UI (ADSR Synthesizer, Negative Prompt UI, Visualizer)
├── README.md                       # Project Documentation
├── requirements.txt                # PyTorch & Audio Processing Dependencies
├── Dockerfile                      # CUDA GPU Container
└── backend/
    ├── main.py                     # FastAPI Pipeline Server & Logging Engine
    ├── prompt_engine/
    │   └── enhancer.py             # Prompt Enhancer & Negative Prompt Processing
    ├── audio_processing/
    │   ├── validator.py            # Quality Gate (RMS, Peak & Corruption Check)
    │   └── converter.py            # FFmpeg 44.1kHz/48kHz Stereo Converter
    ├── models/                     # AI Model Inference Wrappers
    ├── vocals/                     # TCSinger SVS & RVC v2 Voice Converter
    ├── indian_ai/                  # AI4Bharat Indic Language Phoneme Layer
    ├── audio_engine/
    │   └── mastering.py            # Pedalboard & Matchering Mastering Engine
    └── training/
        └── train_lora_musicgen.py  # PyTorch LoRA Fine-Tuning Script
```

---

## 🔗 View Source on GitHub
[https://github.com/parikshitv811-ux/tdi-og-](https://github.com/parikshitv811-ux/tdi-og-)
