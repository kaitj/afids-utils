"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Node(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the `node` color. It can be a single value, or an array
        for specifying color for each `node`. If `node.color` is
        omitted, then the default `Plotly` color palette will be cycled
        through to have a variety of colors. These defaults are not
        fully opaque, to allow some visibility of what is beneath the
        node.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def colorsrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @colorsrc.setter
    def colorsrc(self, val): # -> None:
        ...
    
    @property
    def customdata(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Assigns extra data to each node.

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @customdata.setter
    def customdata(self, val): # -> None:
        ...
    
    @property
    def customdatasrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @customdatasrc.setter
    def customdatasrc(self, val): # -> None:
        ...
    
    @property
    def groups(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Groups of nodes. Each group is defined by an array with the
        indices of the nodes it contains. Multiple groups can be
        specified.

        The 'groups' property is an info array that may be specified as:
        * a 2D list where:
          The 'groups[i][j]' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        list
        """
        ...
    
    @groups.setter
    def groups(self, val): # -> None:
        ...
    
    @property
    def hoverinfo(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Determines which trace information appear when hovering nodes.
        If `none` or `skip` are set, no information is displayed upon
        hovering. But, if `none` is set, click and hover events are
        still fired.

        The 'hoverinfo' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'none', 'skip']

        Returns
        -------
        Any
        """
        ...
    
    @hoverinfo.setter
    def hoverinfo(self, val): # -> None:
        ...
    
    @property
    def hoverlabel(self): # -> tuple[Unknown, ...] | Node | None:
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.node.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

            Supported dict properties:

                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for `align`.
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bordercolor`.
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `namelength`.

        Returns
        -------
        plotly.graph_objs.sankey.node.Hoverlabel
        """
        ...
    
    @hoverlabel.setter
    def hoverlabel(self, val): # -> None:
        ...
    
    @property
    def hovertemplate(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Variables
        `sourceLinks` and `targetLinks` are arrays of link
        objects.Finally, the template string has access to variables
        `value` and `label`. Anything contained in tag `<extra>` is
        displayed in the secondary box, for example
        "<extra>{fullData.name}</extra>". To hide the secondary box
        completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @hovertemplate.setter
    def hovertemplate(self, val): # -> None:
        ...
    
    @property
    def hovertemplatesrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val): # -> None:
        ...
    
    @property
    def label(self): # -> tuple[Unknown, ...] | Node | None:
        """
        The shown name of the node.

        The 'label' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @label.setter
    def label(self, val): # -> None:
        ...
    
    @property
    def labelsrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for `label`.

        The 'labelsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @labelsrc.setter
    def labelsrc(self, val): # -> None:
        ...
    
    @property
    def line(self): # -> tuple[Unknown, ...] | Node | None:
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.node.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                color
                    Sets the color of the `line` around each
                    `node`.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                width
                    Sets the width (in px) of the `line` around
                    each `node`.
                widthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `width`.

        Returns
        -------
        plotly.graph_objs.sankey.node.Line
        """
        ...
    
    @line.setter
    def line(self, val): # -> None:
        ...
    
    @property
    def pad(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the padding (in px) between the `nodes`.

        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @pad.setter
    def pad(self, val): # -> None:
        ...
    
    @property
    def thickness(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the thickness (in px) of the `nodes`.

        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @thickness.setter
    def thickness(self, val): # -> None:
        ...
    
    @property
    def x(self): # -> tuple[Unknown, ...] | Node | None:
        """
        The normalized horizontal position of the node.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def xsrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @xsrc.setter
    def xsrc(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Unknown, ...] | Node | None:
        """
        The normalized vertical position of the node.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def ysrc(self): # -> tuple[Unknown, ...] | Node | None:
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @ysrc.setter
    def ysrc(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., color=..., colorsrc=..., customdata=..., customdatasrc=..., groups=..., hoverinfo=..., hoverlabel=..., hovertemplate=..., hovertemplatesrc=..., label=..., labelsrc=..., line=..., pad=..., thickness=..., x=..., xsrc=..., y=..., ysrc=..., **kwargs) -> None:
        """
        Construct a new Node object

        The nodes of the Sankey plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sankey.Node`
        color
            Sets the `node` color. It can be a single value, or an
            array for specifying color for each `node`. If
            `node.color` is omitted, then the default `Plotly`
            color palette will be cycled through to have a variety
            of colors. These defaults are not fully opaque, to
            allow some visibility of what is beneath the node.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        customdata
            Assigns extra data to each node.
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        groups
            Groups of nodes. Each group is defined by an array with
            the indices of the nodes it contains. Multiple groups
            can be specified.
        hoverinfo
            Determines which trace information appear when hovering
            nodes. If `none` or `skip` are set, no information is
            displayed upon hovering. But, if `none` is set, click
            and hover events are still fired.
        hoverlabel
            :class:`plotly.graph_objects.sankey.node.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Variables `sourceLinks` and
            `targetLinks` are arrays of link objects.Finally, the
            template string has access to variables `value` and
            `label`. Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        label
            The shown name of the node.
        labelsrc
            Sets the source reference on Chart Studio Cloud for
            `label`.
        line
            :class:`plotly.graph_objects.sankey.node.Line` instance
            or dict with compatible properties
        pad
            Sets the padding (in px) between the `nodes`.
        thickness
            Sets the thickness (in px) of the `nodes`.
        x
            The normalized horizontal position of the node.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            The normalized vertical position of the node.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.

        Returns
        -------
        Node
        """
        ...
    


