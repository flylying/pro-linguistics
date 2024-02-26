from .GoogleTokenSpan import GoogleTokenSpan
from .GoogleSentiment import GoogleSentiment


class GoogleSentence(GoogleTokenSpan):
	def __init__(self, dictionary, document):

		text = dictionary.pop('text')
		content = tex