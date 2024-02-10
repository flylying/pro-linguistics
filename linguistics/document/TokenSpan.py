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
		"""
		:rtype: tokens.Span
		"""
		return self._obj

	@property
	def start(self):
		"""
		:rtype: int
		"""
		try:
			return self._start
		except AttributeError:
			self._start = self.obj.start
		return self._start

	@property
	def end(self):
		"""
		:rtype: int
		"""
		try:
			return self._end
		except AttributeError:
			self._end = self.obj.end
		return self._end

	@property
	def end_except_punctuation(self):
		"""
		:rtype: int
		"""
		try:
			return self._end_except_punctuation
		except AttributeError:
			self._end_except_punctuation = max([x.index for x in self.tokens if not x.is_punctuation])
		return self._end_except_punctuation

	@property
	def id(self):
		return (self.document.id, 'span', self.start, self.end)

	@property
	def text(self):
		"""
		:rtype: str
		"""
		return self.obj.text


	@property
	def tokens(self):
		"""
		:rtype: list[.Document.Token]
		"""
		return self.document.tokens[self.start:self.end]

	@property
	def las