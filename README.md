# DiagramGenerator

A librabry that allow to make diagram simply

# /!\ WARNING : DO NOT TRY TO `pip install` cause it will not work. For installation, follow the line right after

## Installation

Download `diagramme.py` and put it in your project folder.

## Usage
**for html usage**

```python
import diagramme

# returns a base64 chart pie
encode = diagramme.pie(["Male","Female"],[60,40])

with open("example.html",'w') as f:
    f.write(f"<img src='data:image/png;base64,{pie(["a", "b", "c"], [1, 2, 3], True, False)} '>")
```

**for image show**

```python
import diagramme
import plt

fig = diagramme.pie(names=['a', 'b', 'c'], values=[1, 2, 3], image=True)
img = plt.imread(fig)
plt.imshow(img)
plt.show()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
