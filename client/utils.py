import json

import sys


def wrapper_to_str(wrapper_object):
    type_fields = type(wrapper_object)._type_._fields_

    # Create strings containing "name": value from fields on the object in json format
    attribute_names = [field[0] for field in type_fields]
    attribute_vals = [getattr(wrapper_object.contents, field[0]) for field in type_fields]
    attribute_vals_strings = [None] * len(attribute_vals)
    for i in range(len(attribute_vals)):
        attr = attribute_vals[i]
        if hasattr(attr, '_length_'):
            # Attribute is an array
            attribute_vals_strings[i] = '[ %s ]' % ', '.join([str(e) for e in attr])
        elif type(attr) == bool:
            # Attribute is a boolean, proper boolean string needs to be used
            attribute_vals_strings[i] = 'true' if attr else 'false'
        else:
            attribute_vals_strings[i] = str(attr)
    attribute_strings = ['"%s": %s' % attr for attr in zip(attribute_names, attribute_vals_strings)]

    # Pretty print it with json module
    json_string = '{ %s }' % ', '.join(attribute_strings)
    try:
        json_object = json.loads(json_string)
    except:
        print('Unexpected error:', sys.exc_info()[0])
        print('Error while json parsing following json string:')
        print(json_string)
        raise
    try:
        formatted_json_string = json.dumps(json_object, sort_keys=False, indent=4)
        return '%s: %s' % (type(wrapper_object)._type_.__name__, formatted_json_string)
    except:
        print('Unexpected error:', sys.exc_info()[0])
        print('Error while json formatting following object:')
        print(str(json_object))
        raise
