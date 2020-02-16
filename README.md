# Python Setup for Visual Studio Code

vsc/python virtual environments, intellisense, debugging, testing, documentation, live output, etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
git init
```

```bash
git clone https://github.com/johnbroaddusivccv/pythonSetup.git
```

```bash
cd pythonSetup
```

## Usage
Make sure Python is installed 
```bash
python ––version
```
When using python it's important to create a virtual enviroment. A virtual enviroment is a tool that helps to keep dependencies required by different projects separate by isolation.

To create a virtual enviroment bash the following.
* on windows 10
```bash
py -m venv venv
```

to activate the virtual enviroment bash the following.
```bash
source venv/scripts/activate
```
to deactivate the virtual enviroment bash the following.
```bash
deactivate
```
## Python Extension for Visual Studio Code
* The most important extension is the [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) it gives us ability for intellisense, snippets, debugging, testing, etc.
* [Kite](https://kite.com/download/?utm_medium=referral&utm_source=youtube&utm_campaign=TechGuyWeb&utm_content=python_vscode) allows us to view in depth documentation with a simple hover in Visual Studio Code. I use this when writing python but this is optional.
* [AREPL](https://marketplace.visualstudio.com/items?itemName=almenon.arepl) is a scratchpad in which debugging, running, and writing your code can all be done at the same time.
* [AutoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) allows us to quickly generate docstrings for python functions.
* [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) Allows us to run [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) or [pytest](https://docs.pytest.org/en/latest/) with the [test explorer ui](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

### Example
```bash
py main.py
```
```python

import json

items = json.loads(
    '[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}, {"id":3, "text": "Item 3"}]')

for item in items:
    print(item['text'])


def greet(greeting, name):
    """returns a greeting
    Arguments:
        greeting {string} -- A greet word
        name {string} -- A persons name
    Returns:
        string  -- A greeting with a name
    """
    return f'{greeting} {name}'


print(greet('Hello', 'world'))
```
When [main.py](https://github.com/johnbroaddusivccv/pythonSetup/blob/master/main.py) is ran it would return to following:
```bash
item 1
item 2
item 3
Hello world
```
While this is simple python code it is visible when using these extensions how this can be helpful in dealing with API's or really big datasets.
* Using AREPL we are able to run our code in real time and view it on the right hand side.
    * Notice how we can view the JSON easily and not have to leave the text editor to view the properties and methods inside the object
* Using AutoDocString we are able to tab through our function quickly.
    * Press enter after opening docstring with triple quotes (""" or ''') then tab through the function.
* Using Kite we are able to read documentation without having to open a tab or exit Visual Studio Code.
    * Get docs quicker with just a click. Kite shows them to you in-line, covering 800+ Python libraries with code examples.
* Using Python Test Explorer we are able to run unittest and pytest in the visual studio code test explorer ui.
    * By default the extension uses the configuration from [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) To configure Python for your project see [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial).

## License
[MIT](https://choosealicense.com/licenses/mit/)
