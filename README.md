# Pro-Linguistics\nPro-Linguistics is an advanced Python library built for natural language processing, now maintained by flylying.\n\n## Installation\nUse the package manager pip to install pro-linguistics.\n```bash\npip install pro-linguistics\n```\n\n## Dependencies\nPro-Linguistics leverages the power of Abstract and Graphviz to generate visual representations of document structures.\n\n## Usage\n\n### Similarity\n\n#### Sentence\n\n##### get_similar_pairs\n\n```python\nfrom pro_linguistics.similarity import Sentence\n\nsentence_1 = Sentence('John Joseph Nicholson')\nsentence_2 = Sentence('Nicholson, Jack')\nprint(sentence_1.get_similar_pairs(sentence_2))\n```\nResults:\n```json\n[{'word_1': Nicholson,\n  'word_2': Nicholson,\n  'similarity': 1.0,\n  'index_1': 2,\n  'index_2': 0},\n {'word_1': John,\n  'word_2': Jack,\n  'similarity': 0.5,\n  'index_1': 0,\n  'index_2': 1},\n {'word_1': Joseph,\n  'word_2': None,\n  'similarity': 0,\n  'index_1': 1,\n  'index_2': None}]\n```\n\n##### get_unordered_similarity\n```python\nprint(sentence_1.get_unordered_similarity(sentence_2))\nprint(sentence_1.get_unordered_sim