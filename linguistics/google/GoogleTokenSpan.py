from .GoogleDocumentObject import GoogleDocumentObject
from .GoogleToken import GoogleToken


class GoogleTokenSpan(GoogleDocumentObject):
	def __init__(self, dictionary, document, begin, end):
		super().__init__(dictionary=dictionary, document=do