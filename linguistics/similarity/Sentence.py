
import re
from .Word import Word
from .get_sentence_similarity import get_sentence_similarity


def get_similarity_matrix(s1, s2, case_sensitivity=1, first_char_weight=0, method='jaro_winkler'):
	if not isinstance(s1, Sentence):
		s1 = Sentence(s1)
	if not isinstance(s2, Sentence):
		s2 = Sentence(s2)

	max_length = max(s1.length, s2.length)

	def get_similarity_by_index(i1, i2):
		try:
			return s1.words[i1].get_similarity(
				s2.words[i2], case_sensitivity=case_sensitivity, first_char_weight=first_char_weight, method=method
			)
		except:
			return 0

	return [
		[(i1, i2, get_similarity_by_index(i1, i2))
		 for i2 in range(max_length)]
		for i1 in range(max_length)
	]


def get_similar_pairs(s1, s2, case_sensitivity=1, first_char_weight=0, method='jaro_winkler'):
	similarity_matrix = get_similarity_matrix(
		s1, s2, case_sensitivity=case_sensitivity, first_char_weight=first_char_weight, method=method
	)

	flat_list = [e for l in similarity_matrix for e in l]
	sorted_similarities = sorted(flat_list, key=lambda x: -x[2])

	result = []
	for i1, i2, similarity in sorted_similarities:
		if similarity_matrix[i1][i2] is not None:
			if i1 < s1.length and i2 < s2.length:
				word_1, word_2 = s1.words[i1], s2.words[i2]
				index_1, index_2 = i1, i2
			elif i1 < s1.length:
				word_1, word_2 = s1.words[i1], None
				index_1, index_2 = i1, None
			else:
				word_1, word_2 = None, s2.words[i2]
				index_1, index_2 = None, i2

			result.append({
				'word_1': word_1, 'word_2': word_2, 'similarity': similarity,
				'index_1': index_1, 'index_2': index_2
			})

			# remove all elements at column i2 (iterate over rows)
			for j1 in range(len(similarity_matrix)):
				similarity_matrix[j1][i2] = None

			# remove all elements at row i1 (iterate over columns)
			for j2 in range(len(similarity_matrix[i1])):
				similarity_matrix[i1][j2] = None

	return result


class Sentence:
	def __init__(self, string):
		if isinstance(string, self.__class__):
			self._string = string._string
			self._words = string.words.copy()
		elif isinstance(string, (list, tuple)):
			self._words = [Word(x) for x in string]
			self._string = ' '.join([str(x) for x in string])
		else:
			self._string = str(string)
			self._words = None

	@property
	def words(self):
		if self._words is None:
			words = [
				Word(string=s)
				for s in re.findall(r'[^\s!,.?":;]+', self._string)
			]
			self._words = [word for word in words if word.length > 0]

		return self._words

	def __sub__(self, other):
		"""
		:type other: Sentence
		:rtype: float
		"""