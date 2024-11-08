"""
Emotion Detector Application

This module provides a Flask web application for detecting emotions in a given text.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    """
    Route to analyze emotions in a given text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    detected_emotions = emotion_detector(text_to_analyze)

    if detected_emotions['dominant_emotion'] is None:
        response = "Invalid text! Please try again!"
    else:
        response = f"""
        For the given statement, the system response is 'anger': {detected_emotions['anger']},
         'disgust': {detected_emotions['disgust']}, 'fear': {detected_emotions['fear']}, 
         'joy': {detected_emotions['joy']} and 'sadness': {detected_emotions['sadness']}. 
         The dominant emotion is {detected_emotions['dominant_emotion']}.
        """

    return response

@app.route("/")
def render_index_page():
    """
    Handles rendering of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
