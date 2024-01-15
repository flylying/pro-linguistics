import warnings
import spacy
from spacy.lang.en import English
from .Document import Document


class Linguist:
	def __init__(self, spacy_core='en_core_web_sm', prefer_g