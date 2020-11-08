# multilanguage-spell-checker


## 1. Pre-requisites

1) Python 3.6 or higher
2) Install enchant (e.g.: sudo apt-get install libenchant-dev)
3) Install dictionaries (e.g.: sudo apt-get install hunspell-it hunspell-es hunspell-de-de hunspell-fr)
4) Install Python dependencies (pip install -r requirements.txt)

## 2. Run

Execute "python app.py" from project folder.

## 3. Example

Once executed locally, perform a POST call towards:

http://127.0.0.1:5000/analyze-sentence

with body:

{

   "text": "Hello, this sentencee does indeeed contain somee mistackes",

   "min_prob": 0.99

}

To obtain:

{

 "Language": {

   "lang": "en",

   "prob": 0.9999955090592161

 },

 "SpellCheck": {

   "similarity": 0.9617898441427855,

   "suggestion": "Hello this sentence does indeed contain some mistakes"

  }

}
