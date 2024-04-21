from .levenshtein import get_levenshtein_similarity
from .jaro_winkler import get_jaro_winkler_similarity




def get_string_similarity(s1, s2, case_sensitivity=1.0, first_char_weight=0.0, method='jaro_winkler'):


	s1 = s1 or ''
	s2 = s2 or ''
	s1 = str(s1)
	s2 = str(s2)

	if method=='jaro_winkler':
		_get_similarity = get_jaro