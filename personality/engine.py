import os, yaml, openai
from groq_client import get_groq_client
from typing import Dict
from memex.models import ExtractionResult

client = get_groq_client()

# load tones once
with open("personality/tones.yaml", encoding="utf-8") as f:
    TONES: Dict = yaml.safe_load(f)

def build_context_block(mem: ExtractionResult) -> str:
    lines = ["===User memory===", ""]
    for p in mem.preferences:
        lines.append(f"- {p.polarity.capitalize()}s {p.topic}  (strength {p.strength})")
    for e in mem.emotional_patterns:
        lines.append(f"- Feels {e.valence} arousal when {e.trigger}")
    for f in mem.facts:
        lines.append(f"- Fact ({f.category}): {f.content}")
    return "\n".join(lines)

def rewrite(answer: str, mem: ExtractionResult, tone: str) -> str:
    if tone not in TONES:
        raise ValueError(f"Unknown tone {tone}")
    meta = TONES[tone]
    context = build_context_block(mem)
    sys = meta["system_prompt"].strip() + "\n\n" + context
    user = f"""Original answer to rewrite:
{answer}

Instructions:
1. Rewrite the answer in the persona defined above.
2. You MUST explicitly reference at least one specific fact, preference, or emotional pattern from the user's memory to make it personal.
3. Keep it "on point" and concise.
"""
    resp = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": sys},
            {"role": "user", "content": user}
        ],
        temperature=meta["temperature"],
        max_tokens=meta["max_tokens"]
    )
    return resp.choices[0].message.content.strip()