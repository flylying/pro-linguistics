from slytherin import trim

class DocumentObject:
	def __init__(self, obj, document):
		"""
		:param obj: any object from a document
		:type document: Document
		"""
		self._obj = obj
		self._document = document

	@property
	def nlp(self):
		return self.document.nlp

	@property
	def document(self)