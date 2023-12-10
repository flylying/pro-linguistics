from .BertVectorizerModel import BertVectorizerModel
import torch


class BertVectorizer:
	def __init__(self, num_tokens=50):
		self._has_gpu = torch.cuda.device_count() > 0
		self._model = BertVectorizerModel(num_tokens=num_tokens)

		if self._has_gpu:
			self._device = torch.device('cuda')
			self._num_devices = torch.cuda.device_count()
			self._model.to(self._device)

		else:
			self._device = torch.device('cpu')
			self._num_devi