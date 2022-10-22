class Reminder:
    def __init__(self, class_id, concurrent, message):
        self.class_id = class_id
        self.concurrent = concurrent
        self.message = message
        self.logs = []