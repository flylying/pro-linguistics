
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

	def __add__(self, other):
		"""
		:param Token or Document other: adding two tokens (or several tokens) creates a Document
		:rtype: Document
		"""
		return Document(text=str(self).rstrip()+' '+str(other).lstrip(), nlp=self.nlp)

	@property
	def parents(self):
		"""
		:rtype: list[Token]
		"""
		if self._parents is None:
			self._parents = [Token(obj=x, document=self.document) for x in self.token.ancestors]
		return self._parents

	@property
	def children(self):
		"""
		:rtype: list[Token]
		"""
		if self._children is None:
			self._children = [Token(obj=x, document=self.document) for x in self.token.children]
		return self._children


class Document:
	def __init__(self, text=None, nlp=None, id=0, _doc=None):
		"""
		:type text: str
		"""
		spacy.prefer_gpu()
		if isinstance(text, list):
			text = ' '.join([str(x) for x in text])
		self._id = id

		if text is None and _doc is None:
			raise ValueError('Either text or _doc should be given!')
		elif text is None:
			self._doc = _doc
			self._text = _doc.text
			self._nlp = nlp
		elif _doc is None:
			self._doc = None
			self._text = str(text)
			self._nlp = nlp or spacy.load('en_core_web_sm')
		else:
			raise ValueError('Either text or _doc should be None!')

		self._doc = None
		self._tokens = None
		self._noun_chunks = None
		self._entity_chunks = None
		self._entities = None
		self._sentences = None
		self._sentences_method = None
		self._entity_graph = None
		self._syntax_graph = None

	@property
	def nlp(self):
		"""
		:rtype: spacy.tokens.doc.Doc or NoneType
		"""
		return self._nlp

	@property
	def text(self):
		return self._text

	def tokenize(self):
		self._tokens = remove_list_duplicates([Token(obj=x, document=self) for x in self.doc])
		self._entities = remove_list_duplicates([Entity(obj=span, document=self) for span in self.doc.ents])
		self._noun_chunks = remove_list_duplicates([
			NounChunk(obj=span, document=self) for span in self.doc.noun_chunks
		])
		self._entity_chunks = remove_list_duplicates([EntityChunk(entity=entity) for entity in self._entities])

	@property
	def id(self):
		return self._id

	@property
	def doc(self):
		"""
		:rtype: tokens.Doc
		"""
		if self._doc is None:
			self._doc = self._nlp(self._text)
		return self._doc

	def __repr__(self):
		return self.doc.__repr__()

	def __str__(self):
		return self.doc.__str__()

	def graph_str(self):
		if len(str(self)) > 50:
			return f'{self}'[0:47] + '...'
		else:
			return str(self)

	@property
	def sentences(self):

		"""
		uses spacy to split a Document class into a list of Sentence objects
		:rtype: list[Sentence]
		"""
		if self._sentences is None:
			self._sentences = self.get_sentences(method='spacy', return_type='Sentence')
		return self._sentences

	def get_sentences(self, method='spacy', return_type='Sentence'):

		"""