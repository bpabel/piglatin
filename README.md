# piglatin

Converts english text to piglatin.

## Installation

`piglatin` can be installed from PyPI using `pip`.

    pip install piglatin

## Usage

```python
>>> import piglatin
>>> piglatin.translate("hello world!")
'ello-hay orld-way!'
```

## Command Line Usage

`piglatin` can also be used as a command line tool.

```bash    
$ python -m piglatin "hello world!"
ello-hay orld-way
```

Or read and write to files.

```bash
$ python -m piglatin -i input.txt -o output.txt
```

