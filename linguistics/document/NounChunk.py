from .TokenSpan import TokenSpan
from .remove_list_duplicates import remove_list_duplicates
from .Entity import Entity


class NounChunk(TokenSpan):

	def __init__(self, obj, documen