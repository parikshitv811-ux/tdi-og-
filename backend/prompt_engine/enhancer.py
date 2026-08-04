# AI Prompt Enhancer & Negative Prompt Processing System

class PromptEnhancer:
    DEFAULT_NEGATIVE_PROMPT = "noise, static, distortion, clipping, non-harmonic sound, broken audio, erratic frequencies, abrupt cuts, low quality"

    GENRE_MAP = {
        "marwadi": {
            "genre": "Marwadi Folk",
            "region": "Rajasthan, India",
            "instruments": ["Dholak", "Kamaycha", "Algoza", "Ravanahatha"],
            "vocals": "Traditional Rajasthani folk singing",
            "tempo": 110
        },
        "bhangra": {
            "genre": "Punjabi Bhangra",
            "region": "Punjab, India",
            "instruments": ["Dhol", "Tumbi", "Modern Trap Brass", "808 Bass"],
            "vocals": "High-energy Punjabi male folk vocals",
            "tempo": 140
        },
        "garba": {
            "genre": "Gujarati Garba",
            "region": "Gujarat, India",
            "instruments": ["Dholak", "Shehnai", "Harmonium"],
            "vocals": "Festive Garba choir",
            "tempo": 125
        },
        "carnatic": {
            "genre": "South Indian Carnatic Classical",
            "region": "South India",
            "instruments": ["Veena", "Bamboo Flute", "Mridangam"],
            "vocals": "Carnatic classical vocalization",
            "tempo": 100
        },
        "cinematic": {
            "genre": "Hollywood Cinematic Score",
            "instruments": ["Orchestral Strings", "French Horns", "Trailer Percussion"],
            "tempo": 90
        }
    }

    @classmethod
    def enhance_prompt(cls, user_prompt: str, custom_negative_prompt: str = "") -> dict:
        lower = user_prompt.toLowerCase() if hasattr(user_prompt, 'toLowerCase') else user_prompt.lower()
        
        detected_meta = {
            "genre": "General AI Music",
            "instruments": ["Acoustic & Electronic Instruments"],
            "production": "Studio Recording, Clean Mix, 48kHz Stereo",
            "negative_prompt": custom_negative_prompt or cls.DEFAULT_NEGATIVE_PROMPT
        }

        for key, meta in cls.GENRE_MAP.items():
            if key in lower:
                detected_meta.update(meta)
                break

        enhanced_prompt = (
            f"Genre: {detected_meta['genre']}. "
            f"Instruments: {', '.join(detected_meta.get('instruments', []))}. "
            f"Production: High-Fidelity Studio Production, Musical Harmony, Smooth Envelopes. "
            f"User Vibe: {user_prompt}"
        )

        return {
            "enhanced_prompt": enhanced_prompt,
            "negative_prompt": detected_meta["negative_prompt"],
            "metadata": detected_meta
        }
