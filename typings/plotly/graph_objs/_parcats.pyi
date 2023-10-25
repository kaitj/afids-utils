"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceType as _BaseTraceType

class Parcats(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def arrangement(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the drag interaction mode for categories and dimensions.
        If `perpendicular`, the categories can only move along a line
        perpendicular to the paths. If `freeform`, the categories can
        freely move on the plane. If `fixed`, the categories and
        dimensions are stationary.

        The 'arrangement' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['perpendicular', 'freeform', 'fixed']

        Returns
        -------
        Any
        """
        ...
    
    @arrangement.setter
    def arrangement(self, val): # -> None:
        ...
    
    @property
    def bundlecolors(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sort paths so that like colors are bundled together within each
        category.

        The 'bundlecolors' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @bundlecolors.setter
    def bundlecolors(self, val): # -> None:
        ...
    
    @property
    def counts(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The number of observations represented by each state. Defaults
        to 1 so that each state represents one observation

        The 'counts' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        ...
    
    @counts.setter
    def counts(self, val): # -> None:
        ...
    
    @property
    def countssrc(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the source reference on Chart Studio Cloud for `counts`.

        The 'countssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @countssrc.setter
    def countssrc(self, val): # -> None:
        ...
    
    @property
    def dimensions(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The dimensions (variables) of the parallel categories diagram.

        The 'dimensions' property is a tuple of instances of
        Dimension that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.parcats.Dimension
          - A list or tuple of dicts of string/value properties that
            will be passed to the Dimension constructor

            Supported dict properties:

                categoryarray
                    Sets the order in which categories in this
                    dimension appear. Only has an effect if
                    `categoryorder` is set to "array". Used with
                    `categoryorder`.
                categoryarraysrc
                    Sets the source reference on Chart Studio Cloud
                    for `categoryarray`.
                categoryorder
                    Specifies the ordering logic for the categories
                    in the dimension. By default, plotly uses
                    "trace", which specifies the order that is
                    present in the data supplied. Set
                    `categoryorder` to *category ascending* or
                    *category descending* if order should be
                    determined by the alphanumerical order of the
                    category names. Set `categoryorder` to "array"
                    to derive the ordering from the attribute
                    `categoryarray`. If a category is not found in
                    the `categoryarray` array, the sorting behavior
                    for that attribute will be identical to the
                    "trace" mode. The unspecified categories will
                    follow the categories in `categoryarray`.
                displayindex
                    The display index of dimension, from left to
                    right, zero indexed, defaults to dimension
                    index.
                label
                    The shown name of the dimension.
                ticktext
                    Sets alternative tick labels for the categories
                    in this dimension. Only has an effect if
                    `categoryorder` is set to "array". Should be an
                    array the same length as `categoryarray` Used
                    with `categoryorder`.
                ticktextsrc
                    Sets the source reference on Chart Studio Cloud
                    for `ticktext`.
                values
                    Dimension values. `values[n]` represents the
                    category value of the `n`th point in the
                    dataset, therefore the `values` vector for all
                    dimensions must be the same (longer vectors
                    will be truncated).
                valuessrc
                    Sets the source reference on Chart Studio Cloud
                    for `values`.
                visible
                    Shows the dimension when set to `true` (the
                    default). Hides the dimension for `false`.

        Returns
        -------
        tuple[plotly.graph_objs.parcats.Dimension]
        """
        ...
    
    @dimensions.setter
    def dimensions(self, val): # -> None:
        ...
    
    @property
    def dimensiondefaults(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        When used in a template (as
        layout.template.data.parcats.dimensiondefaults), sets the
        default property values to use for elements of
        parcats.dimensions

        The 'dimensiondefaults' property is an instance of Dimension
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Dimension`
          - A dict of string/value properties that will be passed
            to the Dimension constructor

            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.parcats.Dimension
        """
        ...
    
    @dimensiondefaults.setter
    def dimensiondefaults(self, val): # -> None:
        ...
    
    @property
    def domain(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

            Supported dict properties:

                column
                    If there is a layout grid, use the domain for
                    this column in the grid for this parcats trace
                    .
                row
                    If there is a layout grid, use the domain for
                    this row in the grid for this parcats trace .
                x
                    Sets the horizontal domain of this parcats
                    trace (in plot fraction).
                y
                    Sets the vertical domain of this parcats trace
                    (in plot fraction).

        Returns
        -------
        plotly.graph_objs.parcats.Domain
        """
        ...
    
    @domain.setter
    def domain(self, val): # -> None:
        ...
    
    @property
    def hoverinfo(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['count', 'probability'] joined with '+' characters
            (e.g. 'count+probability')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')

        Returns
        -------
        Any
        """
        ...
    
    @hoverinfo.setter
    def hoverinfo(self, val): # -> None:
        ...
    
    @property
    def hoveron(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the hover interaction mode for the parcats diagram. If
        `category`, hover interaction take place per category. If
        `color`, hover interactions take place per color per category.
        If `dimension`, hover interactions take place across all
        categories per dimension.

        The 'hoveron' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['category', 'color', 'dimension']

        Returns
        -------
        Any
        """
        ...
    
    @hoveron.setter
    def hoveron(self, val): # -> None:
        ...
    
    @property
    def hovertemplate(self): # -> tuple[Unknown, ...] | Parcats | None:
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
        (the ones that are `arrayOk: true`) are available.  This value
        here applies when hovering over dimensions. Note that
        `*categorycount`, "colorcount" and "bandcolorcount" are only
        available when `hoveron` contains the "color" flagFinally, the
        template string has access to variables `count`, `probability`,
        `category`, `categorycount`, `colorcount` and `bandcolorcount`.
        Anything contained in tag `<extra>` is displayed in the
        secondary box, for example "<extra>{fullData.name}</extra>". To
        hide the secondary box completely, use an empty tag
        `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @hovertemplate.setter
    def hovertemplate(self, val): # -> None:
        ...
    
    @property
    def labelfont(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the font for the `dimension` labels.

        The 'labelfont' property is an instance of Labelfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Labelfont`
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
        plotly.graph_objs.parcats.Labelfont
        """
        ...
    
    @labelfont.setter
    def labelfont(self, val): # -> None:
        ...
    
    @property
    def legendgrouptitle(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

            Supported dict properties:

                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.parcats.Legendgrouptitle
        """
        ...
    
    @legendgrouptitle.setter
    def legendgrouptitle(self, val): # -> None:
        ...
    
    @property
    def legendwidth(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @legendwidth.setter
    def legendwidth(self, val): # -> None:
        ...
    
    @property
    def line(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

            Supported dict properties:

                autocolorscale
                    Determines whether the colorscale is a default
                    palette (`autocolorscale: true`) or the palette
                    determined by `line.colorscale`. Has an effect
                    only if in `line.color` is set to a numerical
                    array. In case `colorscale` is unspecified or
                    `autocolorscale` is true, the default palette
                    will be chosen according to whether numbers in
                    the `color` array are all positive, all
                    negative or mixed.
                cauto
                    Determines whether or not the color domain is
                    computed with respect to the input data (here
                    in `line.color`) or the bounds set in
                    `line.cmin` and `line.cmax` Has an effect only
                    if in `line.color` is set to a numerical array.
                    Defaults to `false` when `line.cmin` and
                    `line.cmax` are set by the user.
                cmax
                    Sets the upper bound of the color domain. Has
                    an effect only if in `line.color` is set to a
                    numerical array. Value should have the same
                    units as in `line.color` and if set,
                    `line.cmin` must be set as well.
                cmid
                    Sets the mid-point of the color domain by
                    scaling `line.cmin` and/or `line.cmax` to be
                    equidistant to this point. Has an effect only
                    if in `line.color` is set to a numerical array.
                    Value should have the same units as in
                    `line.color`. Has no effect when `line.cauto`
                    is `false`.
                cmin
                    Sets the lower bound of the color domain. Has
                    an effect only if in `line.color` is set to a
                    numerical array. Value should have the same
                    units as in `line.color` and if set,
                    `line.cmax` must be set as well.
                color
                    Sets the line color. It accepts either a
                    specific color or an array of numbers that are
                    mapped to the colorscale relative to the max
                    and min values of the array or relative to
                    `line.cmin` and `line.cmax` if set.
                coloraxis
                    Sets a reference to a shared color axis.
                    References to these shared color axes are
                    "coloraxis", "coloraxis2", "coloraxis3", etc.
                    Settings for these shared color axes are set in
                    the layout, under `layout.coloraxis`,
                    `layout.coloraxis2`, etc. Note that multiple
                    color scales can be linked to the same color
                    axis.
                colorbar
                    :class:`plotly.graph_objects.parcats.line.Color
                    Bar` instance or dict with compatible
                    properties
                colorscale
                    Sets the colorscale. Has an effect only if in
                    `line.color` is set to a numerical array. The
                    colorscale must be an array containing arrays
                    mapping a normalized value to an rgb, rgba,
                    hex, hsl, hsv, or named color string. At
                    minimum, a mapping for the lowest (0) and
                    highest (1) values are required. For example,
                    `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`.
                    To control the bounds of the colorscale in
                    color space, use `line.cmin` and `line.cmax`.
                    Alternatively, `colorscale` may be a palette
                    name string of the following list: Blackbody,Bl
                    uered,Blues,Cividis,Earth,Electric,Greens,Greys
                    ,Hot,Jet,Picnic,Portland,Rainbow,RdBu,Reds,Viri
                    dis,YlGnBu,YlOrRd.
                colorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `color`.
                hovertemplate
                    Template string used for rendering the
                    information that appear on hover box. Note that
                    this will override `hoverinfo`. Variables are
                    inserted using %{variable}, for example "y:
                    %{y}" as well as %{xother}, {%_xother},
                    {%_xother_}, {%xother_}. When showing info for
                    several points, "xother" will be added to those
                    with different x positions from the first
                    point. An underscore before or after
                    "(x|y)other" will add a space on that side,
                    only when this field is shown. Numbers are
                    formatted using d3-format's syntax
                    %{variable:d3-format}, for example "Price:
                    %{y:$.2f}". https://github.com/d3/d3-
                    format/tree/v1.4.5#d3-format for details on the
                    formatting syntax. Dates are formatted using
                    d3-time-format's syntax %{variable|d3-time-
                    format}, for example "Day: %{2019-01-01|%A}".
                    https://github.com/d3/d3-time-
                    format/tree/v2.2.3#locale_format for details on
                    the date formatting syntax. The variables
                    available in `hovertemplate` are the ones
                    emitted as event data described at this link
                    https://plotly.com/javascript/plotlyjs-
                    events/#event-data. Additionally, every
                    attributes that can be specified per-point (the
                    ones that are `arrayOk: true`) are available.
                    This value here applies when hovering over
                    lines.Finally, the template string has access
                    to variables `count` and `probability`.
                    Anything contained in tag `<extra>` is
                    displayed in the secondary box, for example
                    "<extra>{fullData.name}</extra>". To hide the
                    secondary box completely, use an empty tag
                    `<extra></extra>`.
                reversescale
                    Reverses the color mapping if true. Has an
                    effect only if in `line.color` is set to a
                    numerical array. If true, `line.cmin` will
                    correspond to the last color in the array and
                    `line.cmax` will correspond to the first color.
                shape
                    Sets the shape of the paths. If `linear`, paths
                    are composed of straight lines. If `hspline`,
                    paths are composed of horizontal curved splines
                showscale
                    Determines whether or not a colorbar is
                    displayed for this trace. Has an effect only if
                    in `line.color` is set to a numerical array.

        Returns
        -------
        plotly.graph_objs.parcats.Line
        """
        ...
    
    @line.setter
    def line(self, val): # -> None:
        ...
    
    @property
    def meta(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @meta.setter
    def meta(self, val): # -> None:
        ...
    
    @property
    def metasrc(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @metasrc.setter
    def metasrc(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @name.setter
    def name(self, val): # -> None:
        ...
    
    @property
    def sortpaths(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the path sorting algorithm. If `forward`, sort paths based
        on dimension categories from left to right. If `backward`, sort
        paths based on dimensions categories from right to left.

        The 'sortpaths' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['forward', 'backward']

        Returns
        -------
        Any
        """
        ...
    
    @sortpaths.setter
    def sortpaths(self, val): # -> None:
        ...
    
    @property
    def stream(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

            Supported dict properties:

                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.parcats.Stream
        """
        ...
    
    @stream.setter
    def stream(self, val): # -> None:
        ...
    
    @property
    def tickfont(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Sets the font for the `category` labels.

        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.parcats.Tickfont`
          - A dict of string/value properties that will be passed
            to the Tickfont constructor

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
        plotly.graph_objs.parcats.Tickfont
        """
        ...
    
    @tickfont.setter
    def tickfont(self, val): # -> None:
        ...
    
    @property
    def uid(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @uid.setter
    def uid(self, val): # -> None:
        ...
    
    @property
    def uirevision(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @uirevision.setter
    def uirevision(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Unknown, ...] | Parcats | None:
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    @property
    def type(self):
        ...
    
    def __init__(self, arg=..., arrangement=..., bundlecolors=..., counts=..., countssrc=..., dimensions=..., dimensiondefaults=..., domain=..., hoverinfo=..., hoveron=..., hovertemplate=..., labelfont=..., legendgrouptitle=..., legendwidth=..., line=..., meta=..., metasrc=..., name=..., sortpaths=..., stream=..., tickfont=..., uid=..., uirevision=..., visible=..., **kwargs) -> None:
        """
        Construct a new Parcats object

        Parallel categories diagram for multidimensional categorical
        data.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Parcats`
        arrangement
            Sets the drag interaction mode for categories and
            dimensions. If `perpendicular`, the categories can only
            move along a line perpendicular to the paths. If
            `freeform`, the categories can freely move on the
            plane. If `fixed`, the categories and dimensions are
            stationary.
        bundlecolors
            Sort paths so that like colors are bundled together
            within each category.
        counts
            The number of observations represented by each state.
            Defaults to 1 so that each state represents one
            observation
        countssrc
            Sets the source reference on Chart Studio Cloud for
            `counts`.
        dimensions
            The dimensions (variables) of the parallel categories
            diagram.
        dimensiondefaults
            When used in a template (as
            layout.template.data.parcats.dimensiondefaults), sets
            the default property values to use for elements of
            parcats.dimensions
        domain
            :class:`plotly.graph_objects.parcats.Domain` instance
            or dict with compatible properties
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoveron
            Sets the hover interaction mode for the parcats
            diagram. If `category`, hover interaction take place
            per category. If `color`, hover interactions take place
            per color per category. If `dimension`, hover
            interactions take place across all categories per
            dimension.
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
            are available.  This value here applies when hovering
            over dimensions. Note that `*categorycount`,
            "colorcount" and "bandcolorcount" are only available
            when `hoveron` contains the "color" flagFinally, the
            template string has access to variables `count`,
            `probability`, `category`, `categorycount`,
            `colorcount` and `bandcolorcount`. Anything contained
            in tag `<extra>` is displayed in the secondary box, for
            example "<extra>{fullData.name}</extra>". To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        labelfont
            Sets the font for the `dimension` labels.
        legendgrouptitle
            :class:`plotly.graph_objects.parcats.Legendgrouptitle`
            instance or dict with compatible properties
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        line
            :class:`plotly.graph_objects.parcats.Line` instance or
            dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        sortpaths
            Sets the path sorting algorithm. If `forward`, sort
            paths based on dimension categories from left to right.
            If `backward`, sort paths based on dimensions
            categories from right to left.
        stream
            :class:`plotly.graph_objects.parcats.Stream` instance
            or dict with compatible properties
        tickfont
            Sets the font for the `category` labels.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).

        Returns
        -------
        Parcats
        """
        ...
    


