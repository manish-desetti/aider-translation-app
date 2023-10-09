import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Function to translate text using GPT-3.5 Turbo model
def translate_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-16k",
        prompt=text,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Streamlit app code
def main():
    st.title("English to German Translation")
    input_text = st.text_input("Enter text in English")
    if st.button("Translate"):
        if input_text:
            translation = translate_text(input_text)
            st.write("Translation:")
            st.write(translation)
        else:
            st.write("Please enter some text to translate")

if __name__ == "__main__":
    main()
