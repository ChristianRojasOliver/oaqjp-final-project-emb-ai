from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    try:
        # Get the text from the POST request
        text = request.json.get('text')
        
        # Call the emotion_detector function
        result = emotion_detector(text)
        
        # Check if the result indicates an error (dominant_emotion is None)
        if result['dominant_emotion'] is None:
            return jsonify({"response": "Invalid text! Please try again!"}), 400

        # Format the response string
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

if __name__ == "__main__":
    app.run(host="localhost", port=5000)