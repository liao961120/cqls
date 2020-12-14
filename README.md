# cqls

Parse Corpus Query Language into a list of queries in JSON format.


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


## Supported CQL features

- token: `[]`, `"我"`, `[word="我"]`, `[word!="我" & pos="N.*"]`
- token-level quantifier: `+`, `*`, `?`, `{n,m}`
- grouping: `("a" "b"? "c"){1,2}`
- label: `lab1:[word="我" & pos="N.*"] lab2:("a" "b")`