from .GoogleTokenSpan import GoogleTokenSpan
from .GoogleSentiment import GoogleSentiment


class GoogleSentence(GoogleTokenSpan):
	def __init__(self, dictionary, document):

		text = dictionary.pop('text')
		content = text.pop('content')
		begin = text.pop('begin_offset')
		end = begin + len(content)

		super().__init__(dictionary=dictionary, document=document