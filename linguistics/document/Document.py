
from .NounChunk import NounChunk
from .Entity import Entity
from .BasicToken import BasicToken
from .EntityChunk import EntityChunk
from .EntityType import EntityType
from .Sentence import Sentence
from .remove_list_duplicates import remove_list_duplicates
from .join_punctuation import join_punctuation
from .split_into_sentences import split_into_sentences

from abstract import Graph
import spacy


class Token(BasicToken):
	def __init__(self, obj, document):
		super().__init__(obj=obj, document=document)
		self._parents = None
		self._children = None