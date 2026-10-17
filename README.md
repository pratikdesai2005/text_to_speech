🔊 Text-to-Speech Converter

A simple and interactive Text-to-Speech (TTS) web application built using Python, Streamlit, and Google Text-to-Speech (gTTS). This application converts written text into spoken audio in multiple languages and allows users to listen to and download the generated speech.

✨ Features
📝 Text Input: Enter text to convert into speech.
🌐 Multiple Languages: Supports English, Hindi, Kannada, Marathi, Tamil, and Telugu.
🐢 Slow Speech Mode: Enable slower speech for easier listening and understanding.
🔊 Audio Playback: Listen to the generated speech directly in the application.
📥 Download Audio: Download the generated speech as an MP3 file.
⚠️ Input Validation: Displays a warning when no text is entered.
🛡️ Error Handling: Displays an error message if speech generation fails.
🛠️ Technologies Used
Python – Core programming language.
Streamlit – Creates the interactive web interface.
gTTS (Google Text-to-Speech) – Converts text into speech.
BytesIO – Stores generated audio in memory without requiring a temporary audio file.
📂 Project Structure
text-to-speech-converter/
│
├── app.py
├── requirements.txt
└── README.md

app.py – Main application code.
requirements.txt – Lists the required Python libraries.
README.md – Project documentation.
⚙️ Installation and Setup
1. Clone the Repository
git clone <your-repository-url>
cd text-to-speech-converter


Replace <your-repository-url> with your Git repository URL.

2. Create a Virtual Environment (Optional)
python -m venv venv


Activate the environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install Dependencies

Create a requirements.txt file with the following content:

streamlit
gTTS


Install the dependencies:

pip install -r requirements.txt

4. Run the Application

Execute the following command in your terminal:

streamlit run app.py


The application will open in your default web browser. If it does not, open the local URL displayed in the terminal, usually http://localhost:8501.

🚀 How to Use
Launch the application.
Enter the text you want to convert into speech.
Select your preferred language from the dropdown menu.
Enable Speak slowly if you want slower audio playback.
Click Convert to Speech.
Listen to the generated audio using the built-in audio player.
Click Download MP3 to save the audio file.
🌍 Supported Languages
Language	Language Code
English	en
Hindi	hi
Kannada	kn
Marathi	mr
Tamil	ta
Telugu	te
📦 Dependencies
Library	Purpose
streamlit	Web interface and interactive controls
gTTS	Text-to-speech generation
io.BytesIO	In-memory audio storage

The io module is part of Python's standard library and does not need to be installed separately.

⚠️ Important Notes
An active internet connection is generally required because gTTS communicates with Google's text-to-speech service.
Speech generation may fail if the service is unavailable or the network connection is interrupted.
Voice characteristics and pronunciation depend on the selected language and the speech service.
The generated audio is MP3, so the download filename should use the .mp3 extension.

Note: In the current code, the download filename is speech.wav, but the audio format is MP3. For consistency, change it to:

file_name="speech.mp3"

🔮 Future Enhancements
Add more supported languages.
Allow users to upload text files.
Provide voice and accent customization where supported.
Add controls for speech speed and audio settings.
Support text-to-speech conversion for uploaded documents.
Improve the interface with additional themes and customization.
👨‍💻 Author

Developed as a Python project to demonstrate text-to-speech conversion using Streamlit and gTTS.

📄 License

This project is available for learning and personal use. Add a specific open-source license, such as the MIT License, if you intend to distribute the project under those terms.
