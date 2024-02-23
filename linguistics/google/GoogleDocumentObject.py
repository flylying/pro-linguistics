from slytherin import trim


class GoogleDocumentObject:
	def __init__(self, dictionary, document, begin, end):
		"""
		:param dict dictionary: any object from a document
		:type document: .GoogleDocument.GoogleDocument
		"""
		self._dictionary = dictionary
		self._document = document
		self._begin = begin
		self._end = end

	@property
	def begin(self):
		return self._begin

	@property
	def end(self):
		return self._end

	def __lt__(self, other):
		"""
		:type other: GoogleToken
		:rtype: bool
		"""
		if self.begin < other.begin and self.end < other.end:
			return True
		elif self.begin >= other.begin and self.end >= other.end:
			return False
		else:
			raise ValueError(f'Token "{self}" and "{other}" overlap!')

	def __gt__(self, other):
		return other.__lt__(self)

	def __le__(self, other):
		return not self.__gt__(other)

	def __g