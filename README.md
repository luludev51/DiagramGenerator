# DiagramGenerator

A librabry that allow to make diagram simply with 2 lines

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install diagramme
```

## Usage

```python
import diagramme

# returns a base64 chart pie
encode = diagramme.pie(["Male","Female"],[60,40])

with open("example.html",'w') as f:
    f.write(f"<img src='data:image/png;base64,{pie(["a", "b", "c"], [1, 2, 3], True, False)} '>")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)