import base64
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

from groq_ai import *
from TTS import *

def autoplay_audio(file: str):
    with open(file, "rb") as f:
        audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        md = f"""<audio autoplay="autoplay" controls="controls" src="data:audio/wav;base64,{b64}">"""
        st.markdown(md, unsafe_allow_html=True)


def main():
    st.title("Talking Assistant with Groq-AI 🎤")
    st.write("Please click below button to start/stop recording.")

    if 'stt_button' not in st.session_state:
        # Create a Speak button and store it in session state
        st.session_state.stt_button = Button(label="Speak", width=100)
    
    st.bokeh_chart(st.session_state.stt_button)

    # Define custom JavaScript to start speech recognition
    st.session_state.stt_button.js_on_event("button_click", CustomJS(code="""
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function (e) {
            var value = '';
            for (var i = e.resultIndex; i < e.results.length; i++) {
                if (e.results[i].isFinal) {
                    value += e.results[i][0].transcript;
                }
            }
            
            if (value !== '') {
                document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
            }
        };
        
        recognition.start();
    """))

    # Capture the custom event and display the recognized text
    result = streamlit_bokeh_events(
        st.session_state.stt_button,
        events="GET_TEXT",
        key="speech",
        refresh_on_update=True,
        override_height=75,
        debounce_time=0,
    )

    if result is not None:
        if "GET_TEXT" in result:
            response = generate_response(result.get("GET_TEXT"))
            file = TTS(response)
            autoplay_audio(file)

if __name__ == "__main__":
    main()
