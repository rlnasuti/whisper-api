from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

# Load the Whisper ASR model
model = whisper.load_model("base")

# Define an endpoint for transcription
@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Retrieve the audio file from the request
    audio_file = request.files.get('audio')

    if audio_file:
        # Save the uploaded audio file to a temporary path
        temp_audio_path = 'temp_audio.mp3'
        audio_file.save(temp_audio_path)

        # Transcribe the audio file using the Whisper ASR model
        result = model.transcribe(temp_audio_path)

        # Extract the transcription text from the result
        transcription = result["text"]

        # Return the transcription as a JSON response
        return jsonify({'transcription': transcription})
    else:
        return jsonify({'error': 'No audio file provided.'}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='localhost', port=5001)

