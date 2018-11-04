class Console(object):
    def __init__(self, chat):
        self.chat = chat

    def run(self):
        try:
            while True:
                text = input('> ')
                context = self.chat.handle(text)
                print(context)
        except EOFError:
            print('Quit')
            pass
