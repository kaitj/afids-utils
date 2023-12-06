"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Contours(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def coloring(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Determines the coloring method showing the contour values. If
        "fill", coloring is done evenly between each contour level If
        "heatmap", a heatmap gradient coloring is applied between each
        contour level. If "lines", coloring is done on the contour
        lines. If "none", no coloring is applied on this trace.

        The 'coloring' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fill', 'heatmap', 'lines', 'none']

        Returns
        -------
        Any
        """
        ...
    
    @coloring.setter
    def coloring(self, val): # -> None:
        ...
    
    @property
    def end(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the end contour level value. Must be more than
        `contours.start`

        The 'end' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @end.setter
    def end(self, val): # -> None:
        ...
    
    @property
    def labelfont(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the font used for labeling the contour levels. The default
        color comes from the lines, if shown. The default family and
        size come from `layout.font`.

        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.contour.contours.Labelfont`
          - A dict of string/value properties that will be passed
            to the Labelfont constructor

            Supported dict properties:

                color

                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.contour.contours.Labelfont
        """
        ...
    
    @labelfont.setter
    def labelfont(self, val): # -> None:
        ...
    
    @property
    def labelformat(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the contour label formatting rule using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format.

        The 'labelformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @labelformat.setter
    def labelformat(self, val): # -> None:
        ...
    
    @property
    def operation(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the constraint operation. "=" keeps regions equal to
        `value` "<" and "<=" keep regions less than `value` ">" and
        ">=" keep regions greater than `value` "[]", "()", "[)", and
        "(]" keep regions inside `value[0]` to `value[1]` "][", ")(",
        "](", ")[" keep regions outside `value[0]` to value[1]` Open
        vs. closed intervals make no difference to constraint display,
        but all versions are allowed for consistency with filter
        transforms.

        The 'operation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['=', '<', '>=', '>', '<=', '[]', '()', '[)', '(]', '][',
                ')(', '](', ')[']

        Returns
        -------
        Any
        """
        ...
    
    @operation.setter
    def operation(self, val): # -> None:
        ...
    
    @property
    def showlabels(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Determines whether to label the contour lines with their
        values.

        The 'showlabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @showlabels.setter
    def showlabels(self, val): # -> None:
        ...
    
    @property
    def showlines(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Determines whether or not the contour lines are drawn. Has an
        effect only if `contours.coloring` is set to "fill".

        The 'showlines' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @showlines.setter
    def showlines(self, val): # -> None:
        ...
    
    @property
    def size(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the step between each contour level. Must be positive.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @size.setter
    def size(self, val): # -> None:
        ...
    
    @property
    def start(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the starting contour level value. Must be less than
        `contours.end`

        The 'start' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @start.setter
    def start(self, val): # -> None:
        ...
    
    @property
    def type(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        If `levels`, the data is represented as a contour plot with
        multiple levels displayed. If `constraint`, the data is
        represented as constraints with the invalid region shaded as
        specified by the `operation` and `value` parameters.

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['levels', 'constraint']

        Returns
        -------
        Any
        """
        ...
    
    @type.setter
    def type(self, val): # -> None:
        ...
    
    @property
    def value(self): # -> tuple[Unknown, ...] | Contours | None:
        """
        Sets the value or values of the constraint boundary. When
        `operation` is set to one of the comparison values
        (=,<,>=,>,<=) "value" is expected to be a number. When
        `operation` is set to one of the interval values
        ([],(),[),(],][,)(,](,)[) "value" is expected to be an array of
        two numbers where the first is the lower bound and the second
        is the upper bound.

        The 'value' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., coloring=..., end=..., labelfont=..., labelformat=..., operation=..., showlabels=..., showlines=..., size=..., start=..., type=..., value=..., **kwargs) -> None:
        """
        Construct a new Contours object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.contour.Contours`
        coloring
            Determines the coloring method showing the contour
            values. If "fill", coloring is done evenly between each
            contour level If "heatmap", a heatmap gradient coloring
            is applied between each contour level. If "lines",
            coloring is done on the contour lines. If "none", no
            coloring is applied on this trace.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        labelfont
            Sets the font used for labeling the contour levels. The
            default color comes from the lines, if shown. The
            default family and size come from `layout.font`.
        labelformat
            Sets the contour label formatting rule using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
        operation
            Sets the constraint operation. "=" keeps regions equal
            to `value` "<" and "<=" keep regions less than `value`
            ">" and ">=" keep regions greater than `value` "[]",
            "()", "[)", and "(]" keep regions inside `value[0]` to
            `value[1]` "][", ")(", "](", ")[" keep regions outside
            `value[0]` to value[1]` Open vs. closed intervals make
            no difference to constraint display, but all versions
            are allowed for consistency with filter transforms.
        showlabels
            Determines whether to label the contour lines with
            their values.
        showlines
            Determines whether or not the contour lines are drawn.
            Has an effect only if `contours.coloring` is set to
            "fill".
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        type
            If `levels`, the data is represented as a contour plot
            with multiple levels displayed. If `constraint`, the
            data is represented as constraints with the invalid
            region shaded as specified by the `operation` and
            `value` parameters.
        value
            Sets the value or values of the constraint boundary.
            When `operation` is set to one of the comparison values
            (=,<,>=,>,<=) "value" is expected to be a number. When
            `operation` is set to one of the interval values
            ([],(),[),(],][,)(,](,)[) "value" is expected to be an
            array of two numbers where the first is the lower bound
            and the second is the upper bound.

        Returns
        -------
        Contours
        """
        ...
    


