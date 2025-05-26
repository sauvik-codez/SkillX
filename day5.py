import streamlit as st
import ollama
import base64

# Set page config
st.set_page_config(page_title="Mental Health Chatbot", layout="wide")

# Optional background image loader (if you want to use an image in future)
def get_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# If you use a background image, uncomment and update below
# bin_str = get_base64("background.png.jpg")

# Peaceful styling with animated gradient and white input box
st.markdown(
    f"""
    <style>
    /* Peaceful Animated Background */
    .stApp {{
        background: linear-gradient(-45deg, #a8edea, #fed6e3, #dcedc1, #ffd3b6);
        background-size: 400% 400%;
        animation: gradientBG 30s ease infinite;
    }}

    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Button Styling */
    button[kind="primary"], button {{
        border-radius: 12px !important;
        padding: 14px 30px !important;
        font-size: 16px !important;
        color: white !important;
        background: linear-gradient(145deg, #6dd5ed, #2193b0);
        border: none !important;
        box-shadow: 0 4px 15px rgba(33, 147, 176, 0.5);
        transition: all 0.4s ease-in-out;
    }}

    button[kind="primary"]:hover, button:hover {{
        background: linear-gradient(145deg, #2193b0, #6dd5ed);
        box-shadow: 0 6px 25px rgba(33, 147, 176, 0.6);
        transform: scale(1.02);
    }}

    /* White input box */
    input[type="text"] {{
        background-color: #bfbfbf !important;
        color:black !important;
        border: 1px solid #ccc !important;
        border-radius: 8px !important;
        padding: 12px !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1) !important;
    }}

    /* Chat text */
    label, .markdown-text-container {{
        color: #003366 !important;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown(
    """
    <h1 style='
        color: #003366;
        text-align: center;
        font-family: "Segoe UI", sans-serif;
        text-shadow: 1px 1px 3px #b0c4de;
        padding: 20px 0;
    '>🌿 Take Care of Your Mental Health</h1>
    """,
    unsafe_allow_html=True
)

# Chat prompt
st.markdown(
    """
    <label style='
        font-size: 20px;
        font-weight: bold;
        color: #005f73;
    '>How can I help you today?</label>
    """,
    unsafe_allow_html=True
)

# Session state to hold chat history
st.session_state.setdefault('conversation_history', [])

# Function to generate chatbot response
def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama3.2", messages=st.session_state['conversation_history'])
    ai_response = response['message']['content']
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

# Function to return affirmation
def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed"
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Function to return guided meditation
def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Display conversation history
for msg in st.session_state['conversation_history']:
    if msg['role'] == "user":
        st.markdown(
            f"<div style='color: #0044cc; font-weight: bold;'>You: {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='color: #222;'>AI: {msg['content']}</div>",
            unsafe_allow_html=True
        )

# Input box
user_message = st.text_input(label="", key="user_input", placeholder="Type your thoughts here...")

# On input submission
if user_message:
    with st.spinner("Thinking....."):
        ai_response = generate_response(user_message)
        st.markdown(
            f"<div style='color: #222;'>AI: {ai_response}</div>",
            unsafe_allow_html=True
        )

# Buttons for extra support
col1, col2 = st.columns(2)

with col1:
    if st.button("Give me a positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"<div style='color: #333;'>💬 *Affirmation:* {affirmation}</div>", unsafe_allow_html=True)

with col2:
    if st.button("Give me a guided meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"<div style='color: #333;'>🧘 *Guided Meditation:* {meditation_guide}</div>", unsafe_allow_html=True)
