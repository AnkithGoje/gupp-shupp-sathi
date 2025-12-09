EXTRACTION_PROMPT = """You are a memory-extraction assistant.
Below are 30 recent chat messages from a user (in English or Hindi).

{conversation}

Output ONLY valid JSON of the form:
{{
  "preferences": [ ... ],
  "emotional_patterns": [ ... ],
  "facts": [ ... ]
}}

Follow these rules:
- preference.topic: short noun phrase
- preference.polarity: "like", "dislike", or "neutral"
- preference.strength: 0.0-1.0
- preference.evidence_msgs: list of zero-based indices into the 30-msg list
- emotional_pattern.trigger: short phrase
- emotional_pattern.valence: -1.0 (very negative) to +1.0 (very positive)
- emotional_pattern.arousal: 0.0 (calm) to 1.0 (excited)
- emotional_pattern.example_quote: quote from the user
- fact.category: "self", "other", or "world"
- fact.content: the fact itself
- fact.confidence: 0.0-1.0
- fact.source_msg_idx: single zero-based index into the 30-msg list

"""