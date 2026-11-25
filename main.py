from fastapi import FastAPI
from pydantic import BaseModel
import textwrap

app = FastAPI(title="MemoMind AI Assistant HUD Bridge")

GLOSSARY = {
    "PM": "Preventive Maintenance (예방 보전)",
    "PLC": "Programmable Logic Controller (자동제어장치)",
    "Downtime": "설비 비가동 시간",
}

class TranscriptInput(BaseModel):
    text: str
    max_chars_per_line: int = 34
    max_lines: int = 3

def format_for_hud(text: str, width: int = 34, max_lines: int = 3) -> list[str]:
    for term, desc in GLOSSARY.items():
        if term in text:
            text = text.replace(term, f"{term}[{desc}]")
    lines = textwrap.wrap(text, width=width)
    return lines[:max_lines]

@app.post("/hud/format")
async def create_hud_payload(payload: TranscriptInput):
    hud_lines = format_for_hud(
        payload.text,
        width=payload.max_chars_per_line,
        max_lines=payload.max_lines
    )
    return {"display": "640x350_MicroLED", "lines": hud_lines}
