import streamlit as st

st.set_page_config(
    page_title="Big Study Forge",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Big Study Forge")

st.subheader("AI-powered study assistant for learners of all ages")

st.write(
    """
    Big Study Forge helps learners transform notes, textbooks, PDFs, questions,
    mistakes, and other learning materials into summaries, quizzes, explanations,
    study plans, and future voice-based review content.
    """
)

st.info("This project is currently in the early development stage.")

st.header("Planned Features")

st.markdown(
    """
    - Learning material summarization
    - Key concept extraction
    - Quiz generation
    - Mistake analysis
    - Personalized study planning
    - Token usage tracking
    - Future voice-based review
    """
)

st.header("Demo Input")

user_input = st.text_area(
    "Paste learning material here:",
    placeholder="Paste notes, textbook content, questions, or study materials..."
)

if st.button("Generate Study Support"):
    if user_input.strip():
        st.success("In the next version, this button will call Xiaomi MiMo API.")
        st.write("Input preview:")
        st.write(user_input[:500])
    else:
        st.warning("Please paste some learning material first.")
