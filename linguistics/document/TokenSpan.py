from .DocumentObject import DocumentObject
from spacy import tokens


class TokenSpan(DocumentObject):

	@property
	def character_range(self):
		return self.tokens[0].character_range[0], self.tokens[-1].character_ran