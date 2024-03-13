from .GoogleDocumentObject import GoogleDocumentObject
from .GoogleToken import GoogleToken


class GoogleTokenSpan(GoogleDocumentObject):
	def __init__(self, dictionary, document, begin, end):
		super().__init__(dictionary=dictionary, document=document, begin=begin, end=end)
		self._tokens = None

	def __str__(self):
		return ', '.join([str(token) for token in self.tokens])

	def __repr__