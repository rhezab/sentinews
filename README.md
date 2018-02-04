# Sentinews

The function avg_sentiment returns the average sentiment of a topic (e.g. "Facebook") across several chosen news outlets (see code for details). This is a wrapper that combines the functionalities of [NewsAPI](https://newsapi.org/), [Newspaper](https://github.com/codelucas/newspaper), and [FastText](https://github.com/facebookresearch/fastText/tree/master/python).

### How to use? 
1. Clone the project directory. 
2. If you haven't already, isntall [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not pipenv, but virtualenv - the lower level option in the link). Then set up a python3 virtualenv as follows: `virtualenv -p python3 venv_name`. Follow the link for more details. This will make sure installations go smoothly. 
3. `pip install -r requirements.txt`
4. Install [FastText](https://github.com/facebookresearch/fastText/tree/master/python) (see installation directions in the link).
5. Get a [NewsAPI API](https://newsapi.org/) key. Un-comment the variable 'newsapi_key' and set it at the top of sentinews.py
6. See demo usage at the bottom of sentinews.py