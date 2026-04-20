import re
import reprlib

"""
this is the "generator" version of the sentence class
"""

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word_match in RE_WORD.finditer(self.text):
            yield word_match.group()
