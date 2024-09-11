import matplotlib.pyplot as plt
from io import BytesIO
import base64


def pie(names: list, values: list, backgroundTransparent: bool = True, percent: bool = True) -> str:
    """
    Return a pie chart using matplotlib.pyplot library
    encoding in base64 for HTML usage.

    Usage: pie(names, values)

    Parameters
    ----------
        - "names" : list of str
        - "values" : list of float or int

    Returns
    -------
        - image : str
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

    # Plot the pie chart
    ax.pie(
        values,
        labels=[f'{name}: {value}%' for name, value in zip(names, values)],
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
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = base64.b64encode(buffer.getvalue()).decode()

    return image #return plot in base64