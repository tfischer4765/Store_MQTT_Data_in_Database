class UnknownTopicError(Exception):

    def __init__(self,topic):
        self.topic = topic
