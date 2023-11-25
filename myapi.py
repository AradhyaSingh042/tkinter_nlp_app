import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('asXmyTpBdooRTt6mAPy54Y2vDv6AWr06pUBWRz2iVgA')

    def sentiment_analysis(self,text):
        sentiment_response = paralleldots.sentiment(text)
        return sentiment_response

    def ner(self,text):
        ner_response = paralleldots.ner(text)
        return ner_response

    def emotion_detection(self,text):
        emotion_response = paralleldots.emotion(text)
        return emotion_response



