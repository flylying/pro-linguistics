def get_char_by_char_equality(s1, s2):
	if s1 is None or s2 is None: return 0
	s1, s2 = str(s1), str(s2)
	weights = [1 / (2 ** i) for i in range(1, max(len(s1), len(s2)))]
	scores =