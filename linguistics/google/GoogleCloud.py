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
			cache=None
	):
		"""
		:param str api_key:
		:param str language:
		:param bool standardize:
		:param bool extract_entities:
		:param bool extract_sentiment:
		:param bool extract_syntax:
		:param disk.Cache.Cache cache:
		"""
		self._api_key = api_key
		self._la