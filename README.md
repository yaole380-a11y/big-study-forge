# Big Study Forge

Big Study Forge is an AI-powered study assistant for learners of all ages.  
It helps users transform textbooks, notes, PDFs, questions, mistakes, code snippets, and learning materials into structured summaries, quizzes, explanations, study plans, and voice-based review content.

## Project Goal

The goal of Big Study Forge is to explore how Xiaomi MiMo API can be used in real-world learning scenarios across different education stages.

This project is designed for:

- Primary school students
- Middle school students
- High school students
- University students
- Adult learners
- Self-learners preparing for exams, certifications, programming, languages, and professional skills

## Why This Project

Many learners struggle with long study materials, scattered notes, unclear concepts, repeated mistakes, and inefficient revision.

Big Study Forge aims to solve these problems by using AI to:

- Summarize long learning materials
- Extract key concepts
- Generate practice questions
- Explain mistakes
- Create personalized study plans
- Track learning progress
- Convert review materials into voice content in the future

## Core Features

### 1. Learning Material Summarization

Users can paste or upload learning materials such as:

- Class notes
- Textbook chapters
- PDF content
- Exam review materials
- Code snippets
- Mistake records
- Language learning materials

The AI assistant will generate:

- Short summary
- Key points
- Important concepts
- Difficult parts
- Easy-to-miss details
- Review suggestions

### 2. Quiz Generation

Based on the learning materials, the system can generate:

- Multiple-choice questions
- True or false questions
- Short-answer questions
- Fill-in-the-blank questions
- Programming questions
- Detailed answer explanations

### 3. Mistake Analysis

Users can input wrong answers or difficult questions.  
The AI assistant will explain:

- Why the answer is wrong
- The correct solution
- Related knowledge points
- Similar practice questions
- Review suggestions

### 4. Personalized Study Planning

Users can enter:

- Learning goal
- Exam date
- Available study time
- Current level
- Weak areas

The system will generate a personalized study plan.

### 5. Token Usage Tracking

The project will track API usage, including:

- Task type
- Model name
- Input token usage
- Output token usage
- Total token usage
- Response time
- User feedback

This helps evaluate the performance, cost, and effectiveness of Xiaomi MiMo API in education scenarios.

### 6. Future Voice Review

In the future, Big Study Forge will test text-to-speech features to generate audio review materials, so users can review knowledge while walking, commuting, or resting.

## Why Xiaomi MiMo API Is Needed

Big Study Forge requires frequent AI model calls for:

- Long-context learning material processing
- Multi-turn learning conversations
- Quiz generation
- Mistake explanation
- Study plan generation
- Model performance evaluation
- Token usage analysis
- Future multimodal and voice learning features

Because learning materials are often long and users may ask many follow-up questions, this project needs a relatively high token quota for development, testing, and real learning scenario validation.

## Current Stage

## Current Stage

This project is currently in the early prototype stage.

The first interactive Streamlit prototype has been created. It supports learning material input, learner stage selection, subject selection, learning goal input, prototype summary generation, quiz generation, study plan generation, and estimated token usage logging.

Planned development steps:

- [x] Create project repository and documentation
- [x] Build the first Streamlit prototype
- [x] Add text input and prototype learning output generation
- [x] Add estimated token usage tracking
- [ ] Add Xiaomi MiMo API integration
- [ ] Add real token usage logging
- [ ] Add PDF input support
- [ ] Add mistake analysis
- [ ] Add study plan improvement
- [ ] Add sample learning materials
- [ ] Add demo screenshots
- [ ] Prepare application materials for higher token quota

## Tech Stack

Planned technology stack:

- Python
- Streamlit
- SQLite or JSON
- Xiaomi MiMo API
- PDF text extraction tools
- Token usage logging

## Project Structure

```text
big-study-forge/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   ├── sample_notes.md
│   └── token_logs.json
├── modules/
│   ├── mimo_client.py
│   ├── summarizer.py
│   ├── quiz_generator.py
│   ├── mistake_analyzer.py
│   ├── study_planner.py
│   └── token_tracker.py
└── docs/
    ├── project_plan.md
    ├── application_material.md
    └── demo_script.md
