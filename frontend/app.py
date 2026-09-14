

import os
from pathlib import Path

import requests
import streamlit as st
from dotenv import load_dotenv


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Dreamscape AI",
    page_icon="🌙",
    layout="centered",
)


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/api/query"
)


# =========================================================
# LOAD CUSTOM CSS
# =========================================================

CSS_PATH = Path(__file__).parent / "style.css"

if CSS_PATH.exists():
    st.markdown(
        f"<style>{CSS_PATH.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🌙 Dreamscape
    </div>

    <div class="subtitle">
        ✨ Your AI Guide to a Magical Fantasy World ✨
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# WELCOME MESSAGE
# =========================================================

st.markdown("""
<div class="welcome-box">

<h3>🌌 Welcome to Dreamscape!</h3>

<p>Ask me about:</p>

<ul>
<li>🧙 Characters</li>
<li>🗺️ Locations</li>
<li>✨ Magic</li>
<li>📜 History</li>
<li>🐺 Creatures</li>
</ul>

<p>
I will answer using the Dreamscape knowledge base.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# CHAT HISTORY
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# DISPLAY PREVIOUS MESSAGES
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:
                st.caption(
                    "📚 Sources: " + ", ".join(sources)
                )


# =========================================================
# USER QUESTION
# =========================================================

question = st.chat_input(
    "Ask something about Dreamscape..."
)


# =========================================================
# PROCESS QUESTION
# =========================================================

if question:

    # -----------------------------------------------------
    # Add user message
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)


    # -----------------------------------------------------
    # Generate assistant answer
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("🌙 Searching the Dreamscape..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=180
                )


                # -----------------------------------------
                # Successful response
                # -----------------------------------------

                if response.status_code == 200:

                    data = response.json()

                    answer = data.get(
                        "answer",
                        "I couldn't find an answer."
                    )

                    sources = data.get(
                        "sources",
                        []
                    )


                    st.markdown(answer)


                    if sources:

                        st.caption(
                            "📚 Sources: "
                            + ", ".join(sources)
                        )


                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": sources
                        }
                    )


                # -----------------------------------------
                # API error
                # -----------------------------------------

                else:

                    error_message = (
                        f"⚠️ API error: {response.status_code}"
                    )

                    st.error(error_message)


                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": error_message,
                            "sources": []
                        }
                    )


            # ---------------------------------------------
            # Backend is not running
            # ---------------------------------------------

            except requests.exceptions.ConnectionError:

                error_message = (
                    "⚠️ I couldn't connect to the Dreamscape API. "
                    "Please make sure the FastAPI backend is running."
                )

                st.error(error_message)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "sources": []
                    }
                )


            # ---------------------------------------------
            # Request timeout
            # ---------------------------------------------

            except requests.exceptions.Timeout:

                error_message = (
                    "⏳ The Dreamscape AI took too long to respond. "
                    "Please try again."
                )

                st.error(error_message)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "sources": []
                    }
                )


            # ---------------------------------------------
            # Unexpected error
            # ---------------------------------------------

            except Exception as e:

                error_message = (
                    "⚠️ Something went wrong while contacting "
                    "the Dreamscape server."
                )

                st.error(error_message)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "sources": []
                    }
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
"""
<div class="dreamscape-footer">
<p>Created by <strong>Aryam Abogadala</strong> ✦</p>
</div>
""",
unsafe_allow_html=True
)
