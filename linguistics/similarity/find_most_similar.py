from chronometry.progress import ProgressBar
import pandas as pd

from .get_similarity import get_similarities

def find_most_similar_for_one_string(
		string, candidates, candidate_ids=None, string_id=None, method='jaro_win