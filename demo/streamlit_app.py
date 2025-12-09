import streamlit as st, requests, json

st.title("Companion AI – Memory-driven Tone Demo")
st.markdown("Paste ±30 messages (one per line), pick a tone, and see the rewrite.")

messages = st.text_area("Chat history (one message per line)").splitlines()
tone = st.selectbox("Tone", ["calm_mentor", "witty_friend", "therapist"])
original = st.text_input("Original answer to rewrite")

if st.button("Rewrite"):
    if not (messages and original):
        st.warning("Need messages and original answer")
        st.stop()
    with st.spinner("Extracting memory + rewriting …"):
        r = requests.post("http://localhost:8000/rewrite", json={
            "messages": messages,
            "tone": tone,
            "original_answer": original
        })
    r.raise_for_status()
    data = r.json()
    col1, col2 = st.columns(2)
    with col1: st.markdown("**Before:**\n" + data["before"])
    with col2: st.markdown("**After:**\n" + data["after"])