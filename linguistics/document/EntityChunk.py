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
		super().__init__(obj=None, document=entity.document)
		self._start = min(
			[entity.start] + [
				noun_chunk.start for noun_chunk in entity.parent_noun_chunks if not noun_chunk.is_sentence
			]
		)
		self._end = max(
			[entity.end] + [
				noun_chunk.end for noun_chunk in entity.parent_noun_chunks if not noun_chunk.is_sentence
			]
		)
		self._entities = remove_list_duplicates([token.entity for token in self.tokens if token.entity])
		for token in self.tokens:
			token._entity_chunk = self

	@property
	def entities(self):
		"""
		:rtype: list[Entity]
		"""
		return self._entities

	@property
	def start(self):
		"""
		:rtype: int
		"""
		return self._start

	@property
	def end(self):
		"""
		:rtype: int
		"""
		return self._end

	@property
	def id(self):
		"""
		:rtype: tuple
		"""
		return self.do