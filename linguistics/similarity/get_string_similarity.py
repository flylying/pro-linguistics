from .levenshtein import get_levenshtein_similarity
from .jaro_winkler import get_jaro_winkler_similarity




def get_string_similarity(s1, s2, case_sensitivity=1.0, first_char_weight=0.0, method='jaro_winkler'):