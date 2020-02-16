# Python Setup for Visual Studio Code

vsc/python virtual environments, intellisense, debugging, testing, documentation, live output, etc.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
git init
```

```
git clone https://github.com/johnbroaddusivccv/pythonSetup.git
```

```
cd pythonSetup
```

## Usage
When using python its important to create a virtual enviroment. A virtual enviroment is a tool that helps to keep dependencies required by different projects separate by isolation.

To create a virtual enviroment bash the following.
* on windows 10
```
py -m venv venv
```

to activate the virtual enviroment bash the following.
```
source venv/scripts/activate
```
to deactivate the virtual enviroment bash the following.
```
deactivate
```
```python
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
