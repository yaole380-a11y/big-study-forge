import datetime
import time

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Big Study Forge",
    page_icon="📚",
    layout="wide"
)


def estimate_tokens(text: str) -> int:
    """A simple token estimation function for prototype display only."""
    if not text:
        return 0
    return max(1, len(text) // 2)


def generate_summary(material: str, learner_stage: str, subject: str) -> str:
    preview = material.strip()[:300]

    return f"""
## Learning Summary

This is a prototype summary generated for a **{learner_stage}** learner studying **{subject}**.

The learning material mainly discusses the following content:

> {preview}

### Main Idea

The material contains knowledge that can be converted into a structured learning summary, key concepts, practice questions, and review suggestions.

### Learning Value

Big Study Forge can help learners understand the material more clearly by organizing long or scattered content into simple sections.
"""


def generate_key_points(material: str, subject: str) -> str:
    words = material.replace("\n", " ").split()
    keywords = []

    for word in words:
        clean_word = word.strip(".,!?;:()[]{}\"'")
        if len(clean_word) >= 5 and clean_word.lower() not in keywords:
            keywords.append(clean_word.lower())

        if len(keywords) >= 8:
            break

    if not keywords:
        keywords = ["concept", "example", "review", "practice"]

    keyword_lines = "\n".join([f"- {word}" for word in keywords])

    return f"""
## Key Concepts

Based on the current **{subject}** learning material, the following concepts may be important:

{keyword_lines}

### Suggested Focus

Learners should focus on definitions, relationships between concepts, examples, and common mistakes.
"""


def generate_quiz(subject: str) -> str:
    return f"""
## Practice Questions

### Question 1

What is the main topic of this **{subject}** learning material?

**Answer Guide:**  
Explain the central idea in your own words.

### Question 2

List three important concepts from the material.

**Answer Guide:**  
Choose concepts that are repeated, difficult, or useful for problem solving.

### Question 3

Create one example related to the material.

**Answer Guide:**  
A good example should connect the concept with a real learning situation.

### Question 4

What is one possible misunderstanding a learner may have?

**Answer Guide:**  
Identify a confusing part and explain how to avoid the mistake.

### Question 5

How would you review this material before an exam?

**Answer Guide:**  
Use summary, practice questions, mistake review, and spaced repetition.
"""


def generate_study_plan(learner_stage: str, subject: str, goal: str) -> str:
    if not goal.strip():
        goal = "understand and review the learning material"

    return f"""
## Personalized Study Plan

### Learner Stage

{learner_stage}

### Subject

{subject}

### Learning Goal

{goal}

### 3-Day Review Plan

#### Day 1: Understand

- Read the material carefully.
- Highlight unfamiliar words or concepts.
- Use Big Study Forge to generate a summary.

#### Day 2: Practice

- Review the key concepts.
- Complete generated practice questions.
- Mark difficult or incorrect answers.

#### Day 3: Review

- Revisit mistakes.
- Explain the material in your own words.
- Create a short final review note.

### Long-Term Suggestion

Use repeated review, quiz practice, and mistake analysis to improve learning results.
"""


def generate_token_log(material: str, output_text: str, task_type: str) -> dict:
    input_tokens = estimate_tokens(material)
    output_tokens = estimate_tokens(output_text)

    return {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": "prototype",
        "task_type": task_type,
        "input_tokens_estimated": input_tokens,
        "output_tokens_estimated": output_tokens,
        "total_tokens_estimated": input_tokens + output_tokens,
    }


if "token_logs" not in st.session_state:
    st.session_state.token_logs = []

if "generated_output" not in st.session_state:
    st.session_state.generated_output = ""


st.title("📚 Big Study Forge")

st.subheader("AI-powered study assistant for learners of all ages")

st.info(
    "Prototype mode: this version shows the product workflow before Xiaomi MiMo API integration."
)

st.markdown(
    """
Big Study Forge helps learners transform notes, textbooks, PDFs, questions, mistakes,
code snippets, and other learning materials into summaries, quizzes, explanations,
study plans, and future voice-based review content.
"""
)

st.divider()

left_col, right_col = st.columns([2, 1])

with left_col:
    st.header("1. Paste Learning Material")

    sample_text = """
Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.
Photosynthesis generally involves the green pigment chlorophyll and generates oxygen as a byproduct.
This process is important because it provides energy for plants and releases oxygen into the atmosphere.
"""

    material = st.text_area(
        "Paste notes, textbook content, questions, code snippets, or study materials here:",
        value=sample_text.strip(),
        height=260,
    )

with right_col:
    st.header("2. Learning Settings")

    learner_stage = st.selectbox(
        "Learner stage",
        [
            "Primary school",
            "Middle school",
            "High school",
            "University",
            "Adult learner",
            "Self-learner",
        ],
    )

    subject = st.selectbox(
        "Subject type",
        [
            "Science",
            "Mathematics",
            "Language learning",
            "Programming",
            "History",
            "Exam preparation",
            "Professional certification",
            "General learning",
        ],
    )

    learning_goal = st.text_input(
        "Learning goal",
        placeholder="Example: prepare for a test, understand key concepts, review mistakes...",
    )

    task_type = st.selectbox(
        "Task type",
        [
            "Full study support",
            "Summary only",
            "Quiz only",
            "Study plan only",
        ],
    )

st.divider()

st.header("3. Generate Study Support")

generate_button = st.button("Generate Prototype Output", type="primary")

if generate_button:
    if not material.strip():
        st.warning("Please paste some learning material first.")
    else:
        with st.spinner("Generating prototype learning support..."):
            time.sleep(1)

            summary = generate_summary(material, learner_stage, subject)
            key_points = generate_key_points(material, subject)
            quiz = generate_quiz(subject)
            study_plan = generate_study_plan(learner_stage, subject, learning_goal)

            if task_type == "Summary only":
                output = summary + "\n\n" + key_points
            elif task_type == "Quiz only":
                output = quiz
            elif task_type == "Study plan only":
                output = study_plan
            else:
                output = summary + "\n\n" + key_points + "\n\n" + quiz + "\n\n" + study_plan

            st.session_state.generated_output = output
            st.session_state.token_logs.append(
                generate_token_log(material, output, task_type)
            )

if st.session_state.generated_output:
    st.success("Prototype output generated successfully.")

    tab_summary, tab_log = st.tabs(["Generated Study Output", "Token Usage Log"])

    with tab_summary:
        st.markdown(st.session_state.generated_output)

    with tab_log:
        logs_df = pd.DataFrame(st.session_state.token_logs)
        st.dataframe(logs_df, use_container_width=True)

        total_estimated_tokens = logs_df["total_tokens_estimated"].sum()
        st.metric("Estimated Total Tokens", int(total_estimated_tokens))

st.divider()

st.header("Project Roadmap")

st.markdown(
    """
- [x] Create public GitHub repository
- [x] Add README and project documentation
- [x] Build first interactive Streamlit prototype
- [ ] Add Xiaomi MiMo API integration
- [ ] Add real token usage tracking
- [ ] Add PDF input support
- [ ] Add mistake analysis module
- [ ] Add voice review feature
- [ ] Deploy public demo
"""
)

st.caption(
    "Big Study Forge is currently a beginner-friendly AI learning assistant prototype."
)
