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
	:type string_id: list