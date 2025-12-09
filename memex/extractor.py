import os, json, openai
from typing import List
from groq_client import get_groq_client
from .models import ExtractionResult
from .prompts import EXTRACTION_PROMPT
from dotenv import load_dotenv
load_dotenv()

client = get_groq_client()

def extract_memory(messages: List[str]) -> ExtractionResult:
    conversation = "\n".join(f"{i:02}: {m}" for i, m in enumerate(messages))
    prompt = EXTRACTION_PROMPT.format(conversation=conversation)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=2000
    )
    raw = response.choices[0].message.content

    def clean_json_text(text: str) -> str:
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return text.strip()

    try:
        data = json.loads(clean_json_text(raw))
        return ExtractionResult(**data)
    except Exception as e:
        # basic retry: ask model to fix JSON
        fix_resp = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": raw},
                {"role": "user", "content": "Fix the JSON only. Output ONLY valid JSON."}
            ],
            temperature=0
        )
        data = json.loads(clean_json_text(fix_resp.choices[0].message.content))
        return ExtractionResult(**data)