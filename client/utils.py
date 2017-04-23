import json


def wrapper_to_str(wrapper_object):
    type_fields = type(wrapper_object)._type_._fields_

    # Create strings containing "name": value from fields on the object in json format
    attribute_names = [field[0] for field in type_fields]
    attribute_vals = [getattr(wrapper_object.contents, field[0]) for field in type_fields]
    attribute_vals_strings = ['[ %s ]' % ', '.join([str(e) for e in attr]) if hasattr(attr, '_length_') else str(attr)
                              for attr in attribute_vals]
    attribute_strings = ['"%s": %s' % attr for attr in zip(attribute_names, attribute_vals_strings)]

    # Pretty print it with json module
    json_string = '{ %s }' % ', '.join(attribute_strings)
    object_str = json.dumps(json.loads(json_string), sort_keys=False, indent=4)
    return '%s: %s' % (type(wrapper_object)._type_.__name__, object_str)