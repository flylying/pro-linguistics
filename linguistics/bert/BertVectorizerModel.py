
import torch
import torch.nn as nn
from torch import Tensor
from pandas import Series
from transformers import BertTokenizer
from transformers import BertModel


class BertVectorizerModel(nn.Module):
	def __init__(self, num_tokens=50):
		super().__init__()
		self._bert_layer = BertModel.from_pretrained('bert-base-uncased')
		self._tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
		self._num_tokens = num_tokens

		self._classification_layer = nn.Linear(768, 1)
		self._activation_layer = nn.Sigmoid()