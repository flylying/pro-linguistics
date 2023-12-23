
from .DocumentObject import DocumentObject
from .dependency_definitions import DEPENDENCY_DEFINITONS
from .part_of_speach_definitions import PART_OF_SPEACH
from .EntityType import EntityType


class BasicToken(DocumentObject):
	def __init__(self, obj, document):
		"""
		:param obj: any object from a document
		:type document: Document
		"""
		super().__init__(obj=obj, document=document)
		self._entity = None
		self._noun_chunk = None
		self._entity_chunk = None
		if self._obj.ent_type_:
			self._entity_type = EntityType(name=self._obj.ent_type_)
		else:
			self._entity_type = None

	@property
	def index(self):
		"""
		:rtype: int
		"""
		return self.token.i

	@property