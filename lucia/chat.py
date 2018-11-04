import os
import sys
from .intents import Intents
from .actions import Actions
from .responses import Responses


class Chat(object):
    def __init__(self, opts):
        self.context = {'curr': {}, 'prev': {}}
        self.intents = Intents(opts)
        self.actions = Actions(opts)
        self.responses = Responses(opts)
        with open(os.path.join(opts.data_dir, 'learn_triggers.txt')) as f:
            self.learn_triggers = f.read().splitlines()

    def _learn_alias(self, text):
        """
        Checks whether the text contains a learning trigger, and previous action wasn't
        detected. In this case previous text is considered to be an alias that needs to 
        be learned. For instance, consider the following conversation:

         > Yohanga!
         < I don't undertand you...
         > I meant: hello
         .. (learned that 'yohanga' is an alias to 'hello') ...
         < Hello there!
        """
        learn_trigger = next(
            iter([t for t in self.learn_triggers if text.startswith(t)]), None)
        if learn_trigger is not None:
            try:
                if self.context['prev']['action'] == None:
                    text = text.lower().strip()
                    alias = text.replace(learn_trigger, '')
                    alias_intent = self.intents.find(alias)
                    if alias_intent is not None:
                        self.intents.add(alias_intent,
                                         self.context['prev']['text'])
                        return alias_intent
            except KeyError:
                pass
        return None

    def _find_action(self, intent):
        return action

    def _find_response(self, action):
        response = self.responses.find(action)
        self.context['curr']['response'] = response
        return response

    def handle(self, text):
        self.context['prev'] = self.context['curr']
        self.context['curr'] = {'text': text}
        self.context['curr']['intent'] = self._learn_alias(text) or self.intents.find(text)
        self.context['curr']['action'] = self.actions.find(self.context['curr']['intent'])
        self.context['curr']['response'] = self._find_response(self.context['curr']['action'])
        return self.context

    def run_in_console(self):
        while True:
            text = input('> ')
            self.handle(text)
            print(self.context)
