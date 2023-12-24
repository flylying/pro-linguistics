
from .TokenSpan import TokenSpan
from .remove_list_duplicates import remove_list_duplicates
from .EntityType import EntityType


class Entity(TokenSpan):

	def __init__(self, obj, document):
		super().__init__(obj=obj, document=document)
		for token in self.tokens: