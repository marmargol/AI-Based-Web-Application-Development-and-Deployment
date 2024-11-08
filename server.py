from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    text_to_analyze = request.args.get('textToAnalyze')
    detected_emotions = emotion_detector(text_to_analyze)
    response = f"For the given statement, the system response is 'anger': {detected_emotions['anger']}, 'disgust': {detected_emotions['disgust']}, 'fear': {detected_emotions['fear']}, 'joy': {detected_emotions['joy']} and 'sadness': {detected_emotions['sadness']}. The dominant emotion is {detected_emotions['dominant_emotion']}."
    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
