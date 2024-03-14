
import re
from .get_string_similarity import get_string_similarity


class Word:
	def __init__(self, string):
		if string is None: string = ''
		if isinstance(string, self.__class__):
			string = string._string
		else:
			string = str(string)
		self._string = re.sub(r'\W+', '', string)

	@property
	def string(self):