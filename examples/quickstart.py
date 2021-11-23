"""
Example from [Readme.md](../README.md)
"""
from pprint import pprint
from river import datasets

ds = datasets.Phishing()


def first_observation(dataset):
    """first observation"""
    print((80 * "~") + "\n" + "upgrade")
    for x, y in dataset:
        pprint(x)
        print(y)
        break

    # output
    """
    /home/.../quickstart.py
    {'age_of_domain': 1,
     'anchor_from_other_domain': 0.0,
     'empty_server_form_handler': 0.0,
     'https': 0.0,
     'ip_in_url': 1,
     'is_popular': 0.5,
     'long_url': 1.0,
     'popup_window': 0.0,
     'request_from_other_domain': 0.0}
    True
    
    Process finished with exit code 0
    """


if __name__ == '__main__':
    first_observation(ds)
