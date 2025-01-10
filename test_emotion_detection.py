import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for text, expected_emotion in test_cases:
            result = emotion_detector(text)
            # Check if result is not None
            self.assertIsNotNone(result)
            # Check if result contains dominant_emotion key
            self.assertIn('dominant_emotion', result)
            # Check if dominant emotion matches expected emotion
            self.assertEqual(result['dominant_emotion'], expected_emotion, 
                f"Expected {expected_emotion} for text: '{text}', but got {result['dominant_emotion']}")

if __name__ == "__main__":
    unittest.main()