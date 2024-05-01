
from setuptools import setup, find_packages
# manually make sure en_core_web_sm is installed
import os
try:
	import spacy
	spacy.prefer_gpu()
	
	try:
		nlp = spacy.load('en_core_web_sm')
	except:
		os.system('python -m spacy download en')
except:
	os.system('pip install spacy')
	os.system('python -m spacy download en')
	try:
		nlp = spacy.load('en_core_web_sm')
	except:
		os.system('python -m spacy download en')


def readme():
	with open('./README.md') as f:
		return f.read()


setup(
	name='linguistics',