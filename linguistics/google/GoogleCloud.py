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
		self._language = language[:2].lower()
		self._standardize = standardize
		self._extract_entities = extract_entities
		self._extract_sentiment = extract_sentiment
		self._extract_syntax = extract_syntax
		self._cache = cache
		if self._cache:
			self._cached_analyze = self._cache.make_cached(
				function=self._analyze, id='google_cloud_analyze_function',
				sub_directory='analyze'
			)
		else:
			self.