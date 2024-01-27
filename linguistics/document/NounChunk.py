from .TokenSpan import TokenSpan
from .remove_list_duplicates import remove_list_duplicates
from .Entity import Entity


class NounChunk(TokenSpan):

	def __init__(self, obj, document):
		super().__init__(obj=obj, document=document)
		for token in self.tokens:
			token._noun_chunk = self

	@property
	def child_entities(self):
		"""
		:rtype: list[Entity]
		"""
		return [e for e in self.document.entities if e.start >= self.start and e.end <= self.end]

	@property
	def parent_entities(self):
		"""
		:rtype: list[Entity]
		"""
		return [e for e in self.document.entities if e.start <= self.start and e.end >= self.end]

	@property
	def entities(self):
		"""
		:rtype: list[Entity]
		"""
		return remove_list_duplicates(self.child_entities + self.parent_entities)

	@property
	def id(self):
		return self.document.id, 'noun_chunk', self.start, self.end

	def graph_str(self):
		if self.entities:
			return f"{self}\n({str(self.main_entity_type).re