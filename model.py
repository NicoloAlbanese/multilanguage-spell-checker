import json


class Language:
    """Language class
        - lang [string]: language identifier (e.g.: en)
        - prob [double]: probability (e.g. 0.999)
    """

    def __init__(self, lang, prob):
        self.lang = lang
        self.prob = prob


class SpellCheck:
    """SpellCheck class
        - suggestion [string]: recommended sentence
        - similarity [double]: measure of similarity between input and recommendation
    """

    def __init__(self, suggestion, similarity):
        self.suggestion = suggestion
        self.similarity = similarity


class Response:
    """Response class
        - SpellCheck object:
            - suggestion [string]: recommended sentence
            - similarity [double]: measure of similarity between input and recommendation
        - Language object:
            - lang [string]: language identifier (e.g.: en)
            - prob [double]: probability (e.g. 0.999)
    """

    def __init__(self, Language, SpellCheck):
        self.Language = Language
        self.SpellCheck = SpellCheck

    def __repr__(self):
        return 'Response: (\n\tLanguage:\n\t\tlang : "%s" \n\t\tprob : "%s" \n\tSpellCheck:\n\t\tsuggestion : "%s" ' \
               '\n\t\tsimilarity : "%s" \n)' % (
                   self.Language.lang, self.Language.prob, self.SpellCheck.suggestion, self.SpellCheck.similarity)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
