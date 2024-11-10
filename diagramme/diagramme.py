import matplotlib.pyplot as plt
from io import BytesIO
import base64


def pie(names: list, values: list, backgroundTransparent: bool = True, percent: bool = True, image = False) -> str or matplotlib.pyplot.Figure:
    """
    Return a pie chart using matplotlib.pyplot library
    encoding in base64 for HTML usage.
    Can return the matplotlib.pyplot figure if image set to True



    Parameters
    ----------
        - "names" : list of str
        - "values" : list of float or int
        - "backgroundTransparent" : bool
        - "percent" : bool
        - "image" : bool

    Returns
    -------
        - image : str or matplotlib.pyplot.Figure

    Usage
    -----
    **For HTML usage**:

        import diagramme

        encode = diagramme.pie(["Male","Female"],[60,40])
        with open("example.html",'w') as f:
            f.write(f"<img src='data:image/png;base64,{encode} '>")


    **For Image show**:

        import diagramme
        import plt


        fig = diagramme.pie(names=['a', 'b', 'c'], values=[1, 2, 3], image=True)
        img = plt.imread(fig)
        plt.imshow(img)
        plt.show()

    """



    if type(names) != list or type(values) != list:
        raise TypeError('names and values must be lists not {} and {}'.format(type(names), type(values)))
    elif len(names) != len(values):
        raise ValueError('names and values must have the same length')
    elif type(backgroundTransparent) != bool:
        raise TypeError('backgroundTransparent must be bool not {}'.format(type(backgroundTransparent)))
    if type(percent) != bool:
        raise TypeError('percent must be bool not {}'.format(type(percent)))


    if percent == True:
        for i in values:
            if sum(values) != 100:
                last = 100 - sum(values)
                values.append(last)
                names.append("None")


    #Create pie chart
    fig, ax = plt.subplots()

    if percent == True:
        lables = [f'{name}: {value}%' for name, value in zip(names, values)]
    else:
        lables = [f'{name}: {value}' for name, value in zip(names, values)]

    # Plot the pie chart
    try :ax.pie(
        values,
        labels=lables,
        startangle=90,
        colors=[
            'green',
            'red',
            'blue',
            'black',
            'purple'
            ],
        textprops={
            'color': 'black',
            'size': '10',
            'verticalalignment': 'center',
            'horizontalalignment': 'center',
            'clip_on': False
            },
        labeldistance=1.2,
        rotatelabels = True
        )
    except ValueError:
        raise ValueError('All values don\'t add up to 100%')

    # Show percentage values
    for t in ax.texts:
        if t.get_text().startswith('None'):
            t.set(rotation="horizontal")
        else:
            t.set_color('black')

    # Change Background color
    if backgroundTransparent == True:
        fig.patch.set_alpha(0.0)
    else:
        fig.patch.set_color('white')

    # Ajust plot size
    fig.set_size_inches(8, 6)

    # Convert plot to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0, transparent=backgroundTransparent)
    buffer.seek(0)
    if image == True:
        return buffer
    image = base64.b64encode(buffer.getvalue()).decode()

    return image #return plot in base64



