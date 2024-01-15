
from collections import OrderedDict

# source: https://spacy.io/usage/linguistic-features
ENTITY_TYPES_BY_SHORTNAME = OrderedDict([
	('PERSON', ('People, including fictional', 'person')),
	('NORP', ('Nationalities or religious or political groups', 'group')),
	('FAC', ('Buildings, airports, highways, bridges, etc', 'facility')),
	('ORG', ('Companies, agencies, institutions, etc', 'organization')),
	('GPE', ('Countries, cities, states', 'geopolitical_entity')),
	('LOC', ('Non-GPE locations, mountain ranges, bodies of water', 'location')),
	('PRODUCT', ('Objects, vehicles, foods, etc (Not services)', 'product')),
	('EVENT', ('Named hurricanes, battles, wars, sports events, etc', 'event')),
	('WORK_OF_ART', ('Titles of books, songs, etc', 'word_of_art')),
	('LAW', ('Named documents made into laws', 'law')),
	('LANGUAGE', ('Any named language', 'language')),
	('DATE', ('Absolute or relative dates or periods', 'date')),
	('TIME', ('Times smaller than a day', 'time')),
	('PERCENT', ('Percentage, including "%"', 'percent')),
	('MONEY', ('Monetary values, including unit', 'money')),
	('QUANTITY', ('Measurements, as of weight or distance', 'quantity')),
	('ORDINAL', ('"first", "second", etc', 'ordinal')),
	('CARDINAL', ('Numerals that do not fall under another type', 'cardinal'))
])