from editdistance import eval as get_edit_distance
from jellyfish import jaro_winkler as get_similarity

def convert_distance_function_to_score_function(function=get_edit_distance):
	def score_func(s1, s2):
		distance = function(s1, s2)
		score = max(0,1-float(distance)/max(len(s1), len(s2)))
		return score
	return score_func

def create_weight