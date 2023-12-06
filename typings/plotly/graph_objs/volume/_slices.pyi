"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Slices(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def x(self): # -> tuple[Unknown, ...] | Slices | None:
        """
        The 'x' property is an instance of X
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.slices.X`
          - A dict of string/value properties that will be passed
            to the X constructor

            Supported dict properties:

                fill
                    Sets the fill ratio of the `slices`. The
                    default fill value of the `slices` is 1 meaning
                    that they are entirely shaded. On the other
                    hand Applying a `fill` ratio less than one
                    would allow the creation of openings parallel
                    to the edges.
                locations
                    Specifies the location(s) of slices on the
                    axis. When not specified slices would be
                    created for all points of the axis x except
                    start and end.
                locationssrc
                    Sets the source reference on Chart Studio Cloud
                    for `locations`.
                show
                    Determines whether or not slice planes about
                    the x dimension are drawn.

        Returns
        -------
        plotly.graph_objs.volume.slices.X
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Unknown, ...] | Slices | None:
        """
        The 'y' property is an instance of Y
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.slices.Y`
          - A dict of string/value properties that will be passed
            to the Y constructor

            Supported dict properties:

                fill
                    Sets the fill ratio of the `slices`. The
                    default fill value of the `slices` is 1 meaning
                    that they are entirely shaded. On the other
                    hand Applying a `fill` ratio less than one
                    would allow the creation of openings parallel
                    to the edges.
                locations
                    Specifies the location(s) of slices on the
                    axis. When not specified slices would be
                    created for all points of the axis y except
                    start and end.
                locationssrc
                    Sets the source reference on Chart Studio Cloud
                    for `locations`.
                show
                    Determines whether or not slice planes about
                    the y dimension are drawn.

        Returns
        -------
        plotly.graph_objs.volume.slices.Y
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def z(self): # -> tuple[Unknown, ...] | Slices | None:
        """
        The 'z' property is an instance of Z
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.volume.slices.Z`
          - A dict of string/value properties that will be passed
            to the Z constructor

            Supported dict properties:

                fill
                    Sets the fill ratio of the `slices`. The
                    default fill value of the `slices` is 1 meaning
                    that they are entirely shaded. On the other
                    hand Applying a `fill` ratio less than one
                    would allow the creation of openings parallel
                    to the edges.
                locations
                    Specifies the location(s) of slices on the
                    axis. When not specified slices would be
                    created for all points of the axis z except
                    start and end.
                locationssrc
                    Sets the source reference on Chart Studio Cloud
                    for `locations`.
                show
                    Determines whether or not slice planes about
                    the z dimension are drawn.

        Returns
        -------
        plotly.graph_objs.volume.slices.Z
        """
        ...
    
    @z.setter
    def z(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., x=..., y=..., z=..., **kwargs) -> None:
        """
        Construct a new Slices object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.volume.Slices`
        x
            :class:`plotly.graph_objects.volume.slices.X` instance
            or dict with compatible properties
        y
            :class:`plotly.graph_objects.volume.slices.Y` instance
            or dict with compatible properties
        z
            :class:`plotly.graph_objects.volume.slices.Z` instance
            or dict with compatible properties

        Returns
        -------
        Slices
        """
        ...
    


