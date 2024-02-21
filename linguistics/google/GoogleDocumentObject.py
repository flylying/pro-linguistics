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

	