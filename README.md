# Python debugging interview

This is a forked version of flask from ~7 years ago. It has a (relatively) simple bug in it that is your job to now fix.

## Setup

This requires Python 2.7.x (tested on Python 2.7.13)

I'd recommend using a virtualenv:

```bash
virtualenv local
source ./local/bin/activate
```

Then install the dependencies:
```bash
pip install .
pip install jsonschema mock
```

## The bug

Take a look at https://github.com/denniszl/python-debug-interview/issues/1 and figure out how best to fix the bug.

## Tests

Run tests with `python setup.py test`
