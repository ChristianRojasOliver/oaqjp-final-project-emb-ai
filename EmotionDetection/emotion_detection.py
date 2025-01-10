import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank or empty input
    if not text_to_analyze or text_to_analyze.isspace():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=input_json, headers=headers)
        
        # Check for bad status code
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
        response.raise_for_status()

        # Parse the JSON response
        emotions = json.loads(response.text)
        
        # Extract emotion scores
        emotion_scores = emotions['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion (emotion with highest score)
        dominant_emotion = max(emotion_scores.items(), key=lambda x: x[1])[0]

        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

    except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error processing request: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }