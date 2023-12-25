from .TokenSpan import TokenSpan
from .Entity import Entity
from .EntityType import EntityType
from .remove_list_duplicates import remove_list_duplicates
from .join_punctuation import join_punctuation


class EntityChunk(TokenSpan):
	def __init__(self, entity):
		"""
		:type entity: Entity
		"""
		super().__init__(obj=None, docu