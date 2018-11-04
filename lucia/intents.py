import re
import os
import string
import logging
from fastText import train_supervised, load_model


class Intents(object):
    RE_PUNCT = re.compile('[{p}]'.format(p=re.escape(string.punctuation)))
    RE_PUNCT_STRIP = re.compile(
        '^[{p}]+|[{p}]+$'.format(p=re.escape(string.punctuation)))

    def __init__(self, opts):
        self.input_file = os.path.join(opts.data_dir, 'intents.txt')
        self.model_file = '/tmp/lucia/intents.bin'
        self._load()

    def _load(self):
        if os.path.exists(self.model_file):
            logging.info('Loading intents model from {0}'.format(
                self.model_file))
            self.model = load_model(self.model_file)
        else:
            logging.warning(
                'Intents model {0} doesn\'t exist, training a new one'.format(
                    self.model_file))
            self._learn()

    def _learn(self):
        self.model = train_supervised(
            input=self.input_file, epoch=100, lr=1.0, wordNgrams=2, verbose=1)
        self.model.save_model(self.model_file)

    def _clean_text(self, text):
        text = text.strip()
        text = self.RE_PUNCT_STRIP.sub('', text)
        text = self.RE_PUNCT.sub(r' \0 ', text)
        text = re.sub(r'\s\s+', ' ', text)
        text = text.lower()
        return text

    def find(self, text):
        text = self._clean_text(text)
        try:
            return self.model.predict(
                text, threshold=0.9)[0][0].replace('__label__', '')
        except:
            return None

    def add(self, label, text):
        text = self._clean_text(text)
        logging.info(
            'Learning alias "{text}" for "{label}"'.format(**locals()))
        with open(self.input_file, 'a') as f:
            f.write('__label__{label} {text}'.format(**locals()))
        self._learn()
