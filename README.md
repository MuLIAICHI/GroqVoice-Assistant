
# Talking Assistant with Groq-AI

## Overview
This project implements a talking assistant that utilizes advanced AI capabilities for speech-to-text and text-to-speech functionalities. The application allows users to interact using their voice, processes the input through Groq AI, and responds audibly using Deepgram's text-to-speech technology.

## Technologies Used
- **Groq API**: Leveraged for AI-driven chat completions, making use of the powerful Llama3-70b model.
- **Deepgram**: Utilized for converting text responses back into speech, providing a seamless conversational experience.
- **Streamlit**: Serves as the frontend framework to create an interactive web application.
- **Bokeh**: Used within Streamlit to manage interactive elements, such as buttons that trigger speech recognition.
- **Python**: The core programming language used for the backend processing.

## Files Description
- `app_s.py`: Main application file that initializes the Streamlit interface, handles speech-to-text functionality, integrates Groq AI for processing user input, and utilizes the text-to-speech capabilities of Deepgram.
- `groq_ai.py`: Defines the `generate_response` function which interacts with the Groq API to convert user speech input into text and process it through an AI model to generate a response.
- `TTS.py`: Handles the text-to-speech conversion using Deepgram's API, turning the AI-generated text responses into audible speech.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - GROQ_API_KEY: Your Groq API key.
   - DG_API_KEY: Your Deepgram API key.

## Running the Application
To run the application, execute the following command in your terminal:
   ```bash
   streamlit run app_s.py
   ```

## License
[Mozilla Public License 2.0](LICENSE)

## Contributors
- [LIAICHI MUSTAPHA](MuLIAICHI](https://github.com/MuLIAICHI))

Feel free to contribute to this project by submitting issues or creating pull requests.
