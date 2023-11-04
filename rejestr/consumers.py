from channels.consumer import SyncConsumer


class rejestrConsumer(SyncConsumer):

    def app1_message(self, message):
        # do something with message
        print(message)
    
    