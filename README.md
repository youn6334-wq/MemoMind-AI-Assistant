# MemoMind-AI-Assistant (Industrial & Office Bilingual HUD Bridge)

A lightweight Python & REST API middleware designed to bridge real-time speech-to-text, bilingual technical terminology lookup (English ↔ Korean), and automated maintenance checklist logging for hands-free wearable HUDs and smart glasses.

## Overview

In manufacturing facilities and cross-lingual engineering offices, checking smartphones or laptops during floor walks and technical meetings disrupts workflow. This project provides a low-latency backend service that processes audio streams, extracts domain-specific engineering acronyms, and formats concise 2–3 line text payloads optimized for monochrome MicroLED smart glass displays (such as 640×350 HUDs).

## Key Features

- **Bilingual Technical Glossary & Live Translation:** Integrates Whisper/FunASR speech-to-text with LLM-powered context translation tailored for industrial automation, SAP/MES terminology, and facility maintenance.
- **Hands-Free Inspection Checklist Logger:** Converts voice status updates from wearable microphones into structured JSON/CSV maintenance logs.
- **HUD Payload Formatter:** Automatically truncates and wraps long responses into clean, glanceable 3-line cards to minimize eye fatigue on compact smart glass displays.
- **Low-Latency Webhook & BLE Bridge:** Lightweight FastAPI server ready to connect mobile companion apps with external wearable hardware.

## Tech Stack

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **AI & Audio:** OpenAI Whisper / LLM REST APIs, Pydantic
- **Data & Logging:** Pandas, CSV/JSON local storage, SAP/MES export formatters

## Quick Start

```bash
git clone https://github.com
cd MemoMind-AI-Assistant
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
