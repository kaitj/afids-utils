"""
This type stub file was generated by pyright.
"""

np = ...
def map_face2color(face, colormap, scale, vmin, vmax): # -> LiteralString:
    """
    Normalize facecolor values by vmin/vmax and return rgb-color strings

    This function takes a tuple color along with a colormap and a minimum
    (vmin) and maximum (vmax) range of possible mean distances for the
    given parametrized surface. It returns an rgb color based on the mean
    distance between vmin and vmax

    """
    ...

def trisurf(x, y, z, simplices, show_colorbar, edges_color, scale, colormap=..., color_func=..., plot_edges=..., x_edge=..., y_edge=..., z_edge=..., facecolor=...): # -> list[Mesh3d | Scatter3d | Unbound] | list[Mesh3d] | list[Mesh3d | Scatter3d]:
    """
    Refer to FigureFactory.create_trisurf() for docstring
    """
    ...

def create_trisurf(x, y, z, simplices, colormap=..., show_colorbar=..., scale=..., color_func=..., title=..., plot_edges=..., showbackground=..., backgroundcolor=..., gridcolor=..., zerolinecolor=..., edges_color=..., height=..., width=..., aspectratio=...): # -> Figure:
    """
    Returns figure for a triangulated surface plot

    :param (array) x: data values of x in a 1D array
    :param (array) y: data values of y in a 1D array
    :param (array) z: data values of z in a 1D array
    :param (array) simplices: an array of shape (ntri, 3) where ntri is
        the number of triangles in the triangularization. Each row of the
        array contains the indicies of the verticies of each triangle
    :param (str|tuple|list) colormap: either a plotly scale name, an rgb
        or hex color, a color tuple or a list of colors. An rgb color is
        of the form 'rgb(x, y, z)' where x, y, z belong to the interval
        [0, 255] and a color tuple is a tuple of the form (a, b, c) where
        a, b and c belong to [0, 1]. If colormap is a list, it must
        contain the valid color types aforementioned as its members
    :param (bool) show_colorbar: determines if colorbar is visible
    :param (list|array) scale: sets the scale values to be used if a non-
        linearly interpolated colormap is desired. If left as None, a
        linear interpolation between the colors will be excecuted
    :param (function|list) color_func: The parameter that determines the
        coloring of the surface. Takes either a function with 3 arguments
        x, y, z or a list/array of color values the same length as
        simplices. If None, coloring will only depend on the z axis
    :param (str) title: title of the plot
    :param (bool) plot_edges: determines if the triangles on the trisurf
        are visible
    :param (bool) showbackground: makes background in plot visible
    :param (str) backgroundcolor: color of background. Takes a string of
        the form 'rgb(x,y,z)' x,y,z are between 0 and 255 inclusive
    :param (str) gridcolor: color of the gridlines besides the axes. Takes
        a string of the form 'rgb(x,y,z)' x,y,z are between 0 and 255
        inclusive
    :param (str) zerolinecolor: color of the axes. Takes a string of the
        form 'rgb(x,y,z)' x,y,z are between 0 and 255 inclusive
    :param (str) edges_color: color of the edges, if plot_edges is True
    :param (int|float) height: the height of the plot (in pixels)
    :param (int|float) width: the width of the plot (in pixels)
    :param (dict) aspectratio: a dictionary of the aspect ratio values for
        the x, y and z axes. 'x', 'y' and 'z' take (int|float) values

    Example 1: Sphere

    >>> # Necessary Imports for Trisurf
    >>> import numpy as np
    >>> from scipy.spatial import Delaunay

    >>> from plotly.figure_factory import create_trisurf
    >>> from plotly.graph_objs import graph_objs

    >>> # Make data for plot
    >>> u = np.linspace(0, 2*np.pi, 20)
    >>> v = np.linspace(0, np.pi, 20)
    >>> u,v = np.meshgrid(u,v)
    >>> u = u.flatten()
    >>> v = v.flatten()

    >>> x = np.sin(v)*np.cos(u)
    >>> y = np.sin(v)*np.sin(u)
    >>> z = np.cos(v)

    >>> points2D = np.vstack([u,v]).T
    >>> tri = Delaunay(points2D)
    >>> simplices = tri.simplices

    >>> # Create a figure
    >>> fig1 = create_trisurf(x=x, y=y, z=z, colormap="Rainbow",
    ...                       simplices=simplices)

    Example 2: Torus

    >>> # Necessary Imports for Trisurf
    >>> import numpy as np
    >>> from scipy.spatial import Delaunay

    >>> from plotly.figure_factory import create_trisurf
    >>> from plotly.graph_objs import graph_objs

    >>> # Make data for plot
    >>> u = np.linspace(0, 2*np.pi, 20)
    >>> v = np.linspace(0, 2*np.pi, 20)
    >>> u,v = np.meshgrid(u,v)
    >>> u = u.flatten()
    >>> v = v.flatten()

    >>> x = (3 + (np.cos(v)))*np.cos(u)
    >>> y = (3 + (np.cos(v)))*np.sin(u)
    >>> z = np.sin(v)

    >>> points2D = np.vstack([u,v]).T
    >>> tri = Delaunay(points2D)
    >>> simplices = tri.simplices

    >>> # Create a figure
    >>> fig1 = create_trisurf(x=x, y=y, z=z, colormap="Viridis",
    ...                       simplices=simplices)

    Example 3: Mobius Band

    >>> # Necessary Imports for Trisurf
    >>> import numpy as np
    >>> from scipy.spatial import Delaunay

    >>> from plotly.figure_factory import create_trisurf
    >>> from plotly.graph_objs import graph_objs

    >>> # Make data for plot
    >>> u = np.linspace(0, 2*np.pi, 24)
    >>> v = np.linspace(-1, 1, 8)
    >>> u,v = np.meshgrid(u,v)
    >>> u = u.flatten()
    >>> v = v.flatten()

    >>> tp = 1 + 0.5*v*np.cos(u/2.)
    >>> x = tp*np.cos(u)
    >>> y = tp*np.sin(u)
    >>> z = 0.5*v*np.sin(u/2.)

    >>> points2D = np.vstack([u,v]).T
    >>> tri = Delaunay(points2D)
    >>> simplices = tri.simplices

    >>> # Create a figure
    >>> fig1 = create_trisurf(x=x, y=y, z=z, colormap=[(0.2, 0.4, 0.6), (1, 1, 1)],
    ...                       simplices=simplices)

    Example 4: Using a Custom Colormap Function with Light Cone

    >>> # Necessary Imports for Trisurf
    >>> import numpy as np
    >>> from scipy.spatial import Delaunay

    >>> from plotly.figure_factory import create_trisurf
    >>> from plotly.graph_objs import graph_objs

    >>> # Make data for plot
    >>> u=np.linspace(-np.pi, np.pi, 30)
    >>> v=np.linspace(-np.pi, np.pi, 30)
    >>> u,v=np.meshgrid(u,v)
    >>> u=u.flatten()
    >>> v=v.flatten()

    >>> x = u
    >>> y = u*np.cos(v)
    >>> z = u*np.sin(v)

    >>> points2D = np.vstack([u,v]).T
    >>> tri = Delaunay(points2D)
    >>> simplices = tri.simplices

    >>> # Define distance function
    >>> def dist_origin(x, y, z):
    ...     return np.sqrt((1.0 * x)**2 + (1.0 * y)**2 + (1.0 * z)**2)

    >>> # Create a figure
    >>> fig1 = create_trisurf(x=x, y=y, z=z,
    ...                       colormap=['#FFFFFF', '#E4FFFE',
    ...                                 '#A4F6F9', '#FF99FE',
    ...                                 '#BA52ED'],
    ...                       scale=[0, 0.6, 0.71, 0.89, 1],
    ...                       simplices=simplices,
    ...                       color_func=dist_origin)

    Example 5: Enter color_func as a list of colors

    >>> # Necessary Imports for Trisurf
    >>> import numpy as np
    >>> from scipy.spatial import Delaunay
    >>> import random

    >>> from plotly.figure_factory import create_trisurf
    >>> from plotly.graph_objs import graph_objs

    >>> # Make data for plot
    >>> u=np.linspace(-np.pi, np.pi, 30)
    >>> v=np.linspace(-np.pi, np.pi, 30)
    >>> u,v=np.meshgrid(u,v)
    >>> u=u.flatten()
    >>> v=v.flatten()

    >>> x = u
    >>> y = u*np.cos(v)
    >>> z = u*np.sin(v)

    >>> points2D = np.vstack([u,v]).T
    >>> tri = Delaunay(points2D)
    >>> simplices = tri.simplices


    >>> colors = []
    >>> color_choices = ['rgb(0, 0, 0)', '#6c4774', '#d6c7dd']

    >>> for index in range(len(simplices)):
    ...     colors.append(random.choice(color_choices))

    >>> fig = create_trisurf(
    ...     x, y, z, simplices,
    ...     color_func=colors,
    ...     show_colorbar=True,
    ...     edges_color='rgb(2, 85, 180)',
    ...     title=' Modern Art'
    ... )
    """
    ...

