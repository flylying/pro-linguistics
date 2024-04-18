
from chronometry.progress import ProgressBar

from .get_string_similarity import get_string_similarity
from .get_sentence_similarity import get_sentence_similarity


def get_similarity(
		s1, s2, method='jaro_winkler', similarity_function=None,
		case_sensitivity=1.0, first_char_weight=0.0, first_word_weight=0.0
):
	"""
	:type s1: str
	:type s2: str
	:type treat_as_sentence: bool
	:param str method: can be one of 'jaro_winkler', 'levenshtein', 'sentence_jaro_winkler', 'sentence_levenshtein'
	:type case_sensitivity: float
	:type first_char_weight: float
	:type first_word_weight: float
	:rtype: float
	"""
	if similarity_function is not None:
		return similarity_function(s1, s2)
	else:
		if method.startswith('sentence_'):
			treat_as_sentence = True
			method = method.split('_', 1)[1]
		else:
			treat_as_sentence = False

	if treat_as_sentence:
		return get_sentence_similarity(
			words1=s1, words2=s2, method=method, first_char_weight=first_char_weight, first_word_weight=first_word_weight,
			case_sensitivity=case_sensitivity
		)

	else: