import telepot
import telepot.api
import urllib3

telepot.api._pools = {
    'default': urllib3.PoolManager(num_pools=3, maxsize=10, retries=5, timeout=900),
}


class Mailer:
    def __init__(self):
        pass

    def send(self,text):
        self.bot = telepot.Bot("275198711:AAGF2cppsvIWHkfL4yFSCTSZpmxwtG-wtp8")
        self.bot.sendMessage(238370268,text)

    def get_current_message(self):
        self.bot = telepot.Bot("275198711:AAGF2cppsvIWHkfL4yFSCTSZpmxwtG-wtp8")
        updates = self.bot.getUpdates()
        if len(updates) == 0:
            return ""
        message_offset = updates[len(updates)-1]["update_id"]
        current_message = self.bot.getUpdates(offset = message_offset)
        return current_message[0]["message"]["text"]
