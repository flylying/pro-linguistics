import numpy as np

from .get_string_similarity import get_string_similarity

def get_sentence_distance(words1, words2, first_char_weight=0, case_sensitivity=1, method='jaro_winkler'):
	"""
	:type words1: list[str] or str
	:type words2: list[str] or str
	:type first_char_weight: float
	:type case_sensitivity: float
	: