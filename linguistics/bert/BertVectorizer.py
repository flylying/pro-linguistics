from .BertVectorizerModel import BertVectorizerModel
import torch


class BertVectorizer:
	def __init__(self, num_tokens=50):
		self._has_gpu = torch.cuda.device_count() > 0
		self._model = BertVector