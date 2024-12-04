''''Detects emotions by calling emotion_Detection.py'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def em_detector():
    ''' Detects the emotion of the sentence '''
    emotion_text = request.args.get('textToAnalyze')

    response = emotion_detector(emotion_text)
    if response['anger'] is None:
        return "Invalid text! Please try again!"

    resp_return = 'For the given statement, the system response is '
    for key, value in response.items():
        if key == 'joy':
            resp_return += "'" + key + "'" + ' : ' + str(value) + ' and '
        elif key == 'sadness':
            resp_return += "'" + key + "'" + ' : ' + str(value) + '. '
        elif key == "dominant_emotion":
            resp_return += "The dominant emotion is " + value + '.'
        else:
            resp_return += "'" + key + "'" + ' : ' + str(value) + ' , '

    return resp_return

@app.route("/")
def render_index_page():
    '''renders the template index'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
