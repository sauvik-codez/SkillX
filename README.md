# 🌿 Mental Health Chatbot

A calming and supportive web-based chatbot built with Streamlit and powered by LLaMA 3.2 (via Ollama) to provide mental health support, positive affirmations, and guided meditation.

## Features

- 🤖 AI-powered conversation to talk about mental wellness
- 🌞 Instant positive affirmations
- 🧘 5-minute guided meditations
- 🎨 Peaceful animated gradient background for a soothing experience
- 💬 Maintains session-based conversation history

## Technologies Used

- [Streamlit](https://streamlit.io/) – Frontend web interface
- [Ollama](https://ollama.com/) – Local model runner (LLaMA 3.2 used)
- Python standard libraries
- Optional: Support for background images using Base64

## Setup Instructions

1. **Install Dependencies**  
   Ensure you have Python 3.8+ installed. Then run:

   ```bash
   pip install streamlit ollama

Start the Ollama service and pull the LLaMA 3.2 model:
ollama run llama3.2

Run the App:
streamlit run day5.py
