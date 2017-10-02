import json
import generator


def generate_json(count, **kwargs):
    """Use generators to fill the data of each field"""
    result = []
    for i in range(count):
        obj = {}
        for key, value in kwargs.items():
            if isinstance(value, str):
                if hasattr(generator, value):
                    obj.update({key: getattr(generator, value)(1)[0]})
            else:
                obj.update({key: value()})
        result.append(obj)
    return json.dumps(result)
