from .analyze import analyze
from .GoogleDocument import GoogleDocument


class GoogleCloud:
	def __init__(
			self,
			api_key,
			language='english',
			standardize=True,
			extract_entities=True,
			extract_sentiment=True,
			extract_syntax=True,
			