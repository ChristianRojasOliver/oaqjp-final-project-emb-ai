import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()

        # Parse the JSON response
        emotions = json.loads(response.text)
        
        # Extract emotion scores
        emotion_scores = emotions['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion (emotion with highest score)
        dominant_emotion = max(emotion_scores.items(), key=lambda x: x[1])[0]

        # Create formatted output
        output = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        return output

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error processing response: {e}")
        return None