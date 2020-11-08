import string
import enchant
from difflib import SequenceMatcher
from langdetect import detect_langs
from model import Language, SpellCheck, Response

lang_to_dict = {
    "it": "it-IT",
    "fr": "fr_FR",
    "es": "es_ES",
    "en": "en_GB",
    "de": "de_DE"
}


def map_language_to_dict(lang):
    """Determines hunspell dictionary to be used for spell-check

  :return hunspell dictionary given the input language
  """
    if lang in lang_to_dict:
        return lang_to_dict[lang]

    return "Unknown dictionary"


def detect_language(input, min_prob=0.9, get_prob=True):
    """Detect most likely language of input text

  Can specify 'min_prob' (default 0.9) as minimum probability
  under which reject the detected language.

  :return detected language
  and also probability if 'get_prob' is True
  """
    if not input:
        return ("Unknown language", 0)

    first_guess = detect_langs(input)[0]
    prob = first_guess.prob
    lang = first_guess.lang

    if get_prob and prob > min_prob:
        return (lang, prob)

    if prob > min_prob:
        return lang

    return ("Unknown language", 0)


def spellcheck(text, hunspell_dict):
    """Identify misspellings and correct input text

  :return suggestion and a similarity measure with the input text
  if no misspelling is found, a message is returned
  """
    if hunspell_dict == "Unknown dictionary":
        return "No language detected or no dictionary available.", 0

    d = enchant.Dict(hunspell_dict)

    suggestion = []
    suggestion_similarity = []
    replaced_terms = 0

    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # for each token word in the input text
    for token in text.split():
        # if word is mispelled
        if not d.check(token):
            # replace it with new token from spell-check suggestion
            new_token = d.suggest(token)[0]
            suggestion.append(new_token)
            # calculate similarity between original word and replacement
            similarity = SequenceMatcher(None, new_token, token).ratio()
            suggestion_similarity.append(similarity)
            # increase the replacements counter
            replaced_terms += 1
        # if word is not mispelled, keep it as-is
        else:
            suggestion.append(token)
            # if the word is identical, its similarity is 1
            suggestion_similarity.append(1)

    # calculate suggested sentence and overall similarity
    suggested_text = " ".join(suggestion)
    overall_similarity = sum(suggestion_similarity) / len(suggestion_similarity)

    # if no misspelling was found, return message
    if replaced_terms == 0:
        return "No misspelling detected. Input text is correct.", overall_similarity

    return suggested_text, overall_similarity


def process_input_text(text, min_prob=0.9):
    """Identify language and suggest correction in case of misspellings
    Takes input text and minimum desired probability for language detection

    :return detected language, probability, suggestion and similarity
    """
    lang, prob = detect_language(text, min_prob)
    d = map_language_to_dict(lang)
    suggestion, similarity = spellcheck(text, d)
    result = Response(Language(lang, prob), SpellCheck(suggestion, similarity))

    return result
