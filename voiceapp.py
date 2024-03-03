from flask import Flask, request, render_template, abort, jsonify
import speech_recognition as sr
import librosa
import numpy as np

app = Flask(__name__, template_folder='templates')

# Function to perform speech recognition and extract words from audio file
def extract_words(audio_file):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)  # Record the audio file
            # Perform speech recognition
            recognized_text = recognizer.recognize_google(audio_data)
            # Split the recognized text into words
            words = recognized_text.split()
            return words
    except Exception as e:
        print(f"Error extracting words: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    try:
        file1 = request.files['file1']
        file2 = request.files['file2']
        
        # Process the uploaded files and compute similarity score
        # Placeholder values for demonstration
        mfcc_similarity = 0.75
        pitch_similarity = 0.8
        
        # Placeholder data for pitch and timbre
        pitch_data = np.array([3, 4, 2, 5, 4])  # Convert list to NumPy array
        timbre_data = np.array([5, 3, 2, 4, 3])  # Convert list to NumPy array

        # Extract words from the audio files using speech recognition
        words1 = extract_words(file1)
        words2 = extract_words(file2)

        # Pass the similarity scores, actual words, pitch, and timbre data as JSON response
        return jsonify({
            'mfcc_similarity': mfcc_similarity,
            'pitch_similarity': pitch_similarity,
            'words1_actual': words1,  # Actual words extracted from audio file 1
            'words2_actual': words2,  # Actual words extracted from audio file 2
            'pitch_data': pitch_data.tolist(),  # Convert NumPy array back to list for JSON serialization
            'timbre_data': timbre_data.tolist(),  # Convert NumPy array back to list for JSON serialization
        })
    except Exception as e:
        print(f"Error processing request: {e}")
        abort(500)

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # You can set debug=True to enable debug mode
