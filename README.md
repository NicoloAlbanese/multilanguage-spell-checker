# multilanguage-spell-checker

## I. Introduction

This is a simple multilingual spell-checker service in Python.

Given an input sentence, this service determines the language first, with an associated probability:

![Language Detection](https://github.com/NicoloAlbanese/multilanguage-spell-checker/blob/main/img/img1.png)


Then, it checks for misspellings in the input text, based on the detected language, and provides a recommended sentence replacing each misspelled word with a correct one.
A measure of similarity between the input and recommended text is also provided:

![Recommended Sentence](https://github.com/NicoloAlbanese/multilanguage-spell-checker/blob/main/img/img2.png)

## II. Colab Notebook

This project comes with a [Sample Notebook](https://github.com/NicoloAlbanese/multilanguage-spell-checker/blob/main/sample_notebook/Multilingual_spell_checker.ipynb) that may be executed on Google Colab.

Here are some examples of what the service returns from different input sentences:

![Recommendations Example](https://github.com/NicoloAlbanese/multilanguage-spell-checker/blob/main/img/img4.png)

## 1. Pre-requisites

1) Python 3.6 or higher (tested on Python 3.6).
2) Install enchant (e.g.: sudo apt-get install libenchant-dev)
3) Install dictionaries (e.g.: sudo apt-get install hunspell-it hunspell-es hunspell-de-de hunspell-fr)
4) Install Python dependencies (pip install -r requirements.txt)

## 2. Run

Execute "python app.py" from project folder.

## 3. Example

Once executed locally, perform a POST call towards:

http://127.0.0.1:5000/analyze-sentence

Providing in the body the string "text" (input sentence to analyze) and the double "min_prob" (the probability, between 0 and 1, under which to reject the detected language).

Example:

![API call](https://github.com/NicoloAlbanese/multilanguage-spell-checker/blob/main/img/img5.png)


## 4. Supported Languages

Currently, the supported languages are:

* English
* French
* German
* Spanish
* Italian

More languages may be easily included by installing the appropriate dictionaries and configuring them in the project.
