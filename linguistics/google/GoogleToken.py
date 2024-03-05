from .GoogleDocumentObject import GoogleDocumentObject


class GoogleToken(GoogleDocumentObject):
	def __init__(self, dictionary, document):
		text = dictionary.pop('text')
		content = text.pop('content')
		begin = text.pop('begin_offset')
		end = begin + len(content)
		super().__init__(dictionary=dictionary, document=document, begin=begin, end=end)

		self._text = conte