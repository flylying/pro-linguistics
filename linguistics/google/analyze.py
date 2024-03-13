
import requests
from ..document.part_of_speach_definitions import PART_OF_SPEACH

_analyze_to_engine = {
	'entities': 'analyzeEntities',
	'entity_sentiment': 'analyzeEntitySentiment',
	'sentiment': 'analyzeSentiment',
	'syntax': 'analyzeSyntax',
	'all': 'annotateText',
	'document': 'classifyText'
}


def standardize_text(text):
	if 'beginOffset' in text:
		text['begin_offset'] = text.pop('beginOffset')


def standardize_token(token):
	if 'text' in token:
		text = token['text']
		standardize_text(text=text)

	if 'partOfSpeech' in token:
		part_of_speech = token.pop('partOfSpeech')
		token['part_of_speech'] = {
			key: standardirze_part_of_speech(value.lower()) if key == 'tag' else value.lower()
			for key, value in part_of_speech.items()
			if not value.endswith('_UNKNOWN')
		}

	if 'dependencyEdge' in token:
		dependency_edge = token.pop('dependencyEdge')
		if 'headTokenIndex' in dependency_edge:
			dependency_edge['head_token_index'] = dependency_edge.pop('headTokenIndex')
		if 'label' in dependency_edge:
			dependency_edge['label'] = dependency_edge['label'].lower()