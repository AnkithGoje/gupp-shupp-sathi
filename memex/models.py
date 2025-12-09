from pydantic import BaseModel, Field
from typing import List, Literal

class Preference(BaseModel):
    topic: str
    polarity: Literal["like", "dislike", "neutral"]
    strength: float = Field(ge=0, le=1)
    evidence_msgs: List[int]

class EmotionalPattern(BaseModel):
    trigger: str
    valence: float = Field(ge=-1, le=1)
    arousal: float = Field(ge=0, le=1)
    example_quote: str

class Fact(BaseModel):
    category: Literal["self", "other", "world"]
    content: str
    confidence: float = Field(ge=0, le=1)
    source_msg_idx: int

class ExtractionResult(BaseModel):
    preferences: List[Preference]
    emotional_patterns: List[EmotionalPattern]
    facts: List[Fact]