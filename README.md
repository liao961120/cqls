# cqls

Interpret Corpus Query Language as a list of queries in JSON format.


## Installation

```bash
pip install cqls
```


## Usage

```python
>>> import cqls
>>> cql = '''
... "我" [pos="V."]+
... '''
>>> cqls.parse(cql, default_attr="word", max_quant=5)
[
    [{'match': {'word': ['我']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}], 
    [{'match': {'word': ['我']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}], 
    [{'match': {'word': ['我']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}], 
    [{'match': {'word': ['我']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}, {'match': {'pos': ['V.']}, 'not_match': {}}]
]
```