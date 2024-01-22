from .TokenSpan import TokenSpan
from .remove_list_duplicates import remove_list_duplicates
from .Entity import Entity


class NounChunk(TokenSpan):

	def __init__(self, obj, document):
		super().__init__(obj=obj, document=document)
		for token in self.tokens:
			token._noun_chunk = self

	@property
	def child_entitie