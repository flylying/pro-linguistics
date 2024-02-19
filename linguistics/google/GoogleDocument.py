
from abstract import Graph

from .GoogleToken import GoogleToken
from .GoogleEntity import GoogleEntity
from .GoogleSentence import GoogleSentence
from .GoogleSentiment import GoogleSentiment


class GoogleDocument:
	def __init__(self, text=None, cloud=None, id=0, _analysis=None):
		"""
		:param str or NoneType text: a text to be converted to a GoogleDocument
		:param .GoogleCloud.GoogleCloud cloud: GoogleCloud API