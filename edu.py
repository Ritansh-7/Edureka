import streamlit as st
import time

# Define a dictionary of responses
responses = {
    "hello": {"response": "Hi there! Edu-bot this side how can i  assist you today?", "index": 1},
    "how are you": {"response": "I'm just a computer program, so I don't have feelings, but I'm here to help you.", "index": 2},
    "what all features an Edu-bot can provide": {"response": "Edu-Bot is an educational bot which assists you to all queries related to Education", "index": 3},
    "what is machine learning": {"response": "Machine learning is a type of artificial intelligence that allows computers to learn from data and make predictions or take action without being explicitly programmed.", "index": 4},
    "what is deep learning": {"response": "Deep learning is a subset of machine learning that uses artificial neural networks with many layers to learn and make decisions. It is particularly useful for processing large amounts of data and can be used for tasks such as image and speech recognition.", "index": 5},
    "bye": {"response": "Goodbye! Have a nice day!", "index": 6},
}

# Streamed response emulator
def response_generator(prompt):
    if prompt.lower() in responses:
        response = responses[prompt.lower()]["response"]
    else:
        response = "I'm not sure how to respond to that. Please try again."
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Edu-bot ")

st.subheader("Made by Ritansh")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})