from chronometry.progress import ProgressBar
import pandas as pd

from .get_similarity import get_similarities

def find_most_similar_for_one_string(
		string, candidates, candidate_ids=None, string_id=None, method='jaro_winkler', similarity_function=None,
		case_sensitivity=1.0, first_char_weight=0.0, first_word_weight=0.0, num_results=1, echo=0
):
	"""
	:type string: str
	:type candidates: list[str]
	:type candidate_ids: list or NoneType
	:type string_id: list or NoneType
	:param str method: can be one of 'jaro_winkler', 'levenshtein', 'sentence_jaro_winkler', 'sentence_levenshtein'
	:type treat_as_sentence: bool
	:type case_sensitivity: float
	:type first_char_weight: float
	:type first_word_weight: float
	:type num_results: int
	:type echo: int
	:rtype: pd.DataFrame
	"""
	echo = max(0, echo)
	num_results = max(1, min(num_results, len(candidates)))
	similarities = get_similarities(
		string=string, strings=candidates, method=method, similarity_function=similarity_func