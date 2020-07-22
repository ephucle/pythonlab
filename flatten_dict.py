#!/usr/bin/env python3

def flatten_dict(d, result=None):
    """Flattens a nested list.

        >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
        {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = dict()

    for x in d:
        if isinstance(d[x], dict):
            #flatten_dict(x, result)
            sub_dict = d[x]
            for key in sub_dict:
                result[x+"."+str(key)] = sub_dict[key]
        else:
            result[x]=d[x]

    return result



if __name__ == "__main__":
    import doctest
    doctest.testmod()