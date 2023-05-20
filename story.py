"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, words, text):
        """Create story with words and template text."""
        self.name = name
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story("Default",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

class storyOption:
    def __init__(self, name, words, story):
        self.name = name
        self.story = story
        self.words = words

stories = []

option = storyOption('Basic',["adjective","noun","verb","place"], """The {adjective} {noun} liked to {verb} all over the {place}""")
stories.append(option)

option = storyOption('Default',["place", "noun", "verb", "adjective", "plural_noun"], """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
stories.append(option)

option = storyOption('Stranger',["noun","verb","noun2", "pronoun", "adjective", "noun3"], """There once was a {noun} who {verb} a {noun2}, and now {pronoun} is known as {adjective} {noun3}""")
stories.append(option)

option = storyOption('You',["adjective","noun","feeling","verb","noun2"], """You are a {adjective} {noun} and I am {feeling} to be around you. Please {verb} yourself and give me a {noun2}.""")
stories.append(option)