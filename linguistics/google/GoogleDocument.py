
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
		:param int or str id:
		:param dict or NoneType _analysis: result of GoogleCloud.analyze(text)
		"""

		if isinstance(text, list):
			text = ' '.join([str(x) for x in text])
		self._id = id

		if text is None and _analysis is None:
			raise ValueError('Either text or _analysis should be given!')
		elif text is None:
			self._dictionary = _analysis.copy()
			self._cloud = cloud
		elif _analysis is None:
			self._cloud = cloud
			self._dictionary = self._cloud.analyze(text=text)

		self._text = self._dictionary.pop('text')
		self._sentences = None
		self._tokens = None
		self._entities = None
		sentiment = self._dictionary.pop('document_sentiment')
		self._sentiment = GoogleSentiment(score=sentiment.pop('score'), magnitude=sentiment.pop('magnitude'))
		self._language = None
		self._graph = None

	def __str__(self):
		return '\n'.join([str(sentence) for sentence in self.sentences])

	def __repr__(self):
		return str(self)

	@property
	def id(self):
		return self._id

	@property
	def cloud(self):
		"""
		:rtype: .GoogleCloud.GoogleCloud
		"""
		return self._cloud

	def _get_from_dictionary(self, name):
		if name in self._dictionary:
			return self._dictionary.pop(name)
		elif name in ['text', 'sentiment', 'language']:
			return False
		else:
			return []

	def tokenize(self):
		self._text = self._get_from_dictionary('text')

		self._sentences = [GoogleSentence(x, document=self) for x in self._get_from_dictionary('sentences')]
		self._sentences.sort()
		for index, sentence in enumerate(self._sentences):
			sentence._index = index

		self._tokens = [GoogleToken(x, document=self) for x in self._get_from_dictionary('tokens')]
		self._tokens.sort()
		for index, token in enumerate(self._tokens):
			token._index = index

		self._entities = [GoogleEntity(x, document=self) for x in self._get_from_dictionary('entities')]
		for index, entity in enumerate(self._entities):
			entity._index = index

		self._sentiment = self._get_from_dictionary('sentiment')

		self._language = self._get_from_dictionary('language')

	@property
	def text(self):
		if self._text is None:
			self.tokenize()
		return self._text

	@property
	def sentences(self):
		"""
		:rtype: list[GoogleSentence]
		"""
		if self._sentences is None:
			self.tokenize()
		return self._sentences

	@property
	def tokens(self):
		"""
		:rtype: list[GoogleToken]
		"""
		if self._tokens is None:
			self.tokenize()
		return self._tokens

	@property
	def entities(self):
		"""
		:rtype: list[GoogleEntity]
		"""
		if self._entities is None:
			self.tokenize()
		return self._entities

	@property
	def sentiment(self):
		"""
		:rtype: GoogleSentiment
		"""
		if self._sentiment is None:
			self.tokenize()
		return self._sentiment

	@property