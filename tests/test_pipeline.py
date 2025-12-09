import sys, os; sys.path.append(".")
from memex.extractor import extract_memory
from personality.engine import rewrite

fake_chat = [
    "I hate waking up early, I’m a night owl",
    "Coffee is life ☕",
    "My dog Rex always cheers me up",
    "I feel anxious when deadlines pile up",
    "I love dark humour and sarcasm",
    "I’m a software engineer, 29, living in Berlin",
] * 5   # 30 lines

mem = extract_memory(fake_chat)
print("Extracted", len(mem.preferences), "prefs,", len(mem.emotional_patterns), "emo,", len(mem.facts), "facts")

orig = "You should try meditation."
for t in ["calm_mentor", "witty_friend", "therapist"]:
    print(t + ":", rewrite(orig, mem, t))