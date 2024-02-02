from .DocumentObject import DocumentObject
from spacy import tokens


class TokenSpan(DocumentObject):

	@property
	def character_range(self):
		return self.tokens[0].character_range[0], self.tokens[-1].character_range[1]

	def __str__(self):
		character_range = self.character_range
		return self.document.text[character_range[0]: character_range[1]]
		# return ' '.join([str(x) for x in self.tokens])

	def __repr__(self):
		return str(self)

	@property
	def obj(self):
		"