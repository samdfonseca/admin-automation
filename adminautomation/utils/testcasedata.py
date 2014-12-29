from collections import namedtuple
from simplejson import load as readjson


def read_test_case_data_file(data_file):
    """
    Deserializes a json file containing test case input data into a usable object. Results are then sorted
    alphabetically to match the order of test case execution.

    :param data_file: the absolute path to the target data file as a string
    :return: a sorted list of dicts
    """

    with open(data_file, 'r') as f:
        contents = readjson(f)

    test_data = [(key, new_test_case_data_object(contents['tests'][key])) for key in contents['tests'].keys()]
    return dict(test_data)


def new_test_case_data_object(data_dict):
    """
    Creates the pseudo-class TestCaseData and returns an instance of it. Attributes are named at runtime, based on
    the supplied test case data.

    :param data_dict: the test case data as a dict
    :return: a TestCaseData object
    """
    TestCaseData = namedtuple('TestCaseData', ' '.join(data_dict.keys()))
    values = data_dict.values()

    return TestCaseData(*values)
