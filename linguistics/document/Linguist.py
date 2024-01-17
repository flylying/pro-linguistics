import warnings
import spacy
from spacy.lang.en import English
from .Document import Document


class Linguist:
	def __init__(self, spacy_core='en_core_web_sm', prefer_gpu=None, wikipedia_api=None):
		if prefer_gpu is None:
			self._gpu = spacy.prefer_gpu()
		elif prefer_gpu:  # explicit True
			self._gp