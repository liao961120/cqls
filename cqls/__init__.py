from typing import Union
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .expand_quantifiers import expand_quantifiers


def parse(cql: str, default_attr:Union[str, int]="word", max_quant:int=15):
    """Parse a CQL string into lists of queries in JSON format


    Parameters
    ----------
    cql : str
        CQL query
    default_attr : Union[str, int], optional
        Default attribute for a token to generate if
        none is provided in the CQL, by default "word".
        E.g., "item" is equivalent to [word="item"] if
        `default_attr` is set to "word"
    max_quant : int, optional
        The maximum quantity of the quantifiers * and +, by default 15

    Returns
    -------
    list
        A list of queries, each of them consists of a list of query terms
        represented as a dictionary.
    """
    if cql.strip() == '':
        return []

    tokens = list(Lexer(cql).generate_tokens())
    parser = Parser(tokens)
    queries = expand_quantifiers(tokens, max_quant)

    values = []
    for query in queries:
        parser = Parser(query)
        tree = parser.parse()
        interpreter = Interpreter(default_attrname=default_attr)
        value = interpreter.visit(tree)
        if len(value) > 0:
            values.append(value)

    return values
