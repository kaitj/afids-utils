"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceType as _BaseTraceType

class Image(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def colormodel(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Color model used to map the numerical color components
        described in `z` into colors. If `source` is specified, this
        attribute will be set to `rgba256` otherwise it defaults to
        `rgb`.

        The 'colormodel' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['rgb', 'rgba', 'rgba256', 'hsl', 'hsla']

        Returns
        -------
        Any
        """
        ...
    
    @colormodel.setter
    def colormodel(self, val): # -> None:
        ...
    
    @property
    def customdata(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

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
    def customdatasrc(self): # -> tuple[Unknown, ...] | Image | None:
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
    def dx(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Set the pixel's horizontal size.

        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @dx.setter
    def dx(self, val): # -> None:
        ...
    
    @property
    def dy(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Set the pixel's vertical size

        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @dy.setter
    def dy(self, val): # -> None:
        ...
    
    @property
    def hoverinfo(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'color', 'name', 'text'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @hoverinfo.setter
    def hoverinfo(self, val): # -> None:
        ...
    
    @property
    def hoverinfosrc(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @hoverinfosrc.setter
    def hoverinfosrc(self, val): # -> None:
        ...
    
    @property
    def hoverlabel(self): # -> tuple[Unknown, ...] | Image | None:
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.image.Hoverlabel`
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
        plotly.graph_objs.image.Hoverlabel
        """
        ...
    
    @hoverlabel.setter
    def hoverlabel(self, val): # -> None:
        ...
    
    @property
    def hovertemplate(self): # -> tuple[Unknown, ...] | Image | None:
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
        (the ones that are `arrayOk: true`) are available. Finally, the
        template string has access to variables `z`, `color` and
        `colormodel`. Anything contained in tag `<extra>` is displayed
        in the secondary box, for example
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
    def hovertemplatesrc(self): # -> tuple[Unknown, ...] | Image | None:
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
    def hovertext(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Same as `text`.

        The 'hovertext' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @hovertext.setter
    def hovertext(self, val): # -> None:
        ...
    
    @property
    def hovertextsrc(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.

        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @hovertextsrc.setter
    def hovertextsrc(self, val): # -> None:
        ...
    
    @property
    def ids(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @ids.setter
    def ids(self, val): # -> None:
        ...
    
    @property
    def idssrc(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @idssrc.setter
    def idssrc(self, val): # -> None:
        ...
    
    @property
    def legend(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as the string 'legend'
        optionally followed by an integer >= 1
        (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        ...
    
    @legend.setter
    def legend(self, val): # -> None:
        ...
    
    @property
    def legendgrouptitle(self): # -> tuple[Unknown, ...] | Image | None:
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.image.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

            Supported dict properties:

                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.image.Legendgrouptitle
        """
        ...
    
    @legendgrouptitle.setter
    def legendgrouptitle(self, val): # -> None:
        ...
    
    @property
    def legendrank(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @legendrank.setter
    def legendrank(self, val): # -> None:
        ...
    
    @property
    def legendwidth(self): # -> tuple[Unknown, ...] | Image | None:
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
    def meta(self): # -> tuple[Unknown, ...] | Image | None:
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
    def metasrc(self): # -> tuple[Unknown, ...] | Image | None:
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
    def name(self): # -> tuple[Unknown, ...] | Image | None:
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
    def opacity(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the opacity of the trace.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        ...
    
    @opacity.setter
    def opacity(self, val): # -> None:
        ...
    
    @property
    def source(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Specifies the data URI of the image to be visualized. The URI
        consists of "data:image/[<media subtype>][;base64],<data>"

        The 'source' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @source.setter
    def source(self, val): # -> None:
        ...
    
    @property
    def stream(self): # -> tuple[Unknown, ...] | Image | None:
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.image.Stream`
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
        plotly.graph_objs.image.Stream
        """
        ...
    
    @stream.setter
    def stream(self, val): # -> None:
        ...
    
    @property
    def text(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the text elements associated with each z value.

        The 'text' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @text.setter
    def text(self, val): # -> None:
        ...
    
    @property
    def textsrc(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the source reference on Chart Studio Cloud for `text`.

        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @textsrc.setter
    def textsrc(self, val): # -> None:
        ...
    
    @property
    def uid(self): # -> tuple[Unknown, ...] | Image | None:
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
    def uirevision(self): # -> tuple[Unknown, ...] | Image | None:
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
    def visible(self): # -> tuple[Unknown, ...] | Image | None:
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
    def x0(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Set the image's x position. The left edge of the image (or the
        right edge if the x axis is reversed or dx is negative) will be
        found at xmin=x0-dx/2

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @x0.setter
    def x0(self, val): # -> None:
        ...
    
    @property
    def xaxis(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.

        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as the string 'x'
        optionally followed by an integer >= 1
        (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        ...
    
    @xaxis.setter
    def xaxis(self, val): # -> None:
        ...
    
    @property
    def y0(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Set the image's y position. The top edge of the image (or the
        bottom edge if the y axis is NOT reversed or if dy is negative)
        will be found at ymin=y0-dy/2. By default when an image trace
        is included, the y axis will be reversed so that the image is
        right-side-up, but you can disable this by setting
        yaxis.autorange=true or by providing an explicit y axis range.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @y0.setter
    def y0(self, val): # -> None:
        ...
    
    @property
    def yaxis(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.

        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as the string 'y'
        optionally followed by an integer >= 1
        (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        ...
    
    @yaxis.setter
    def yaxis(self, val): # -> None:
        ...
    
    @property
    def z(self): # -> tuple[Unknown, ...] | Image | None:
        """
        A 2-dimensional array in which each element is an array of 3 or
        4 numbers representing a color.

        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        ...
    
    @z.setter
    def z(self, val): # -> None:
        ...
    
    @property
    def zmax(self): # -> tuple[Unknown, ...] | Image | None:
        """
            Array defining the higher bound for each color component. Note
            that the default value will depend on the colormodel. For the
            `rgb` colormodel, it is [255, 255, 255]. For the `rgba`
            colormodel, it is [255, 255, 255, 1]. For the `rgba256`
            colormodel, it is [255, 255, 255, 255]. For the `hsl`
            colormodel, it is [360, 100, 100]. For the `hsla` colormodel,
            it is [360, 100, 100, 1].

            The 'zmax' property is an info array that may be specified as:

            * a list or tuple of 4 elements where:
        (0) The 'zmax[0]' property is a number and may be specified as:
              - An int or float
        (1) The 'zmax[1]' property is a number and may be specified as:
              - An int or float
        (2) The 'zmax[2]' property is a number and may be specified as:
              - An int or float
        (3) The 'zmax[3]' property is a number and may be specified as:
              - An int or float

            Returns
            -------
            list
        """
        ...
    
    @zmax.setter
    def zmax(self, val): # -> None:
        ...
    
    @property
    def zmin(self): # -> tuple[Unknown, ...] | Image | None:
        """
            Array defining the lower bound for each color component. Note
            that the default value will depend on the colormodel. For the
            `rgb` colormodel, it is [0, 0, 0]. For the `rgba` colormodel,
            it is [0, 0, 0, 0]. For the `rgba256` colormodel, it is [0, 0,
            0, 0]. For the `hsl` colormodel, it is [0, 0, 0]. For the
            `hsla` colormodel, it is [0, 0, 0, 0].

            The 'zmin' property is an info array that may be specified as:

            * a list or tuple of 4 elements where:
        (0) The 'zmin[0]' property is a number and may be specified as:
              - An int or float
        (1) The 'zmin[1]' property is a number and may be specified as:
              - An int or float
        (2) The 'zmin[2]' property is a number and may be specified as:
              - An int or float
        (3) The 'zmin[3]' property is a number and may be specified as:
              - An int or float

            Returns
            -------
            list
        """
        ...
    
    @zmin.setter
    def zmin(self, val): # -> None:
        ...
    
    @property
    def zsmooth(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Picks a smoothing algorithm used to smooth `z` data. This only
        applies for image traces that use the `source` attribute.

        The 'zsmooth' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fast', False]

        Returns
        -------
        Any
        """
        ...
    
    @zsmooth.setter
    def zsmooth(self, val): # -> None:
        ...
    
    @property
    def zsrc(self): # -> tuple[Unknown, ...] | Image | None:
        """
        Sets the source reference on Chart Studio Cloud for `z`.

        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @zsrc.setter
    def zsrc(self, val): # -> None:
        ...
    
    @property
    def type(self):
        ...
    
    def __init__(self, arg=..., colormodel=..., customdata=..., customdatasrc=..., dx=..., dy=..., hoverinfo=..., hoverinfosrc=..., hoverlabel=..., hovertemplate=..., hovertemplatesrc=..., hovertext=..., hovertextsrc=..., ids=..., idssrc=..., legend=..., legendgrouptitle=..., legendrank=..., legendwidth=..., meta=..., metasrc=..., name=..., opacity=..., source=..., stream=..., text=..., textsrc=..., uid=..., uirevision=..., visible=..., x0=..., xaxis=..., y0=..., yaxis=..., z=..., zmax=..., zmin=..., zsmooth=..., zsrc=..., **kwargs) -> None:
        """
        Construct a new Image object

        Display an image, i.e. data on a 2D regular raster. By default,
        when an image is displayed in a subplot, its y axis will be
        reversed (ie. `autorange: 'reversed'`), constrained to the
        domain (ie. `constrain: 'domain'`) and it will have the same
        scale as its x axis (ie. `scaleanchor: 'x,`) in order for
        pixels to be rendered as squares.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Image`
        colormodel
            Color model used to map the numerical color components
            described in `z` into colors. If `source` is specified,
            this attribute will be set to `rgba256` otherwise it
            defaults to `rgb`.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Set the pixel's horizontal size.
        dy
            Set the pixel's vertical size
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.image.Hoverlabel` instance
            or dict with compatible properties
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
            are available. Finally, the template string has access
            to variables `z`, `color` and `colormodel`. Anything
            contained in tag `<extra>` is displayed in the
            secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgrouptitle
            :class:`plotly.graph_objects.image.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
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
        opacity
            Sets the opacity of the trace.
        source
            Specifies the data URI of the image to be visualized.
            The URI consists of "data:image/[<media
            subtype>][;base64],<data>"
        stream
            :class:`plotly.graph_objects.image.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with each z value.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
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
        x0
            Set the image's x position. The left edge of the image
            (or the right edge if the x axis is reversed or dx is
            negative) will be found at xmin=x0-dx/2
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        y0
            Set the image's y position. The top edge of the image
            (or the bottom edge if the y axis is NOT reversed or if
            dy is negative) will be found at ymin=y0-dy/2. By
            default when an image trace is included, the y axis
            will be reversed so that the image is right-side-up,
            but you can disable this by setting
            yaxis.autorange=true or by providing an explicit y axis
            range.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        z
            A 2-dimensional array in which each element is an array
            of 3 or 4 numbers representing a color.
        zmax
            Array defining the higher bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [255,
            255, 255]. For the `rgba` colormodel, it is [255, 255,
            255, 1]. For the `rgba256` colormodel, it is [255, 255,
            255, 255]. For the `hsl` colormodel, it is [360, 100,
            100]. For the `hsla` colormodel, it is [360, 100, 100,
            1].
        zmin
            Array defining the lower bound for each color
            component. Note that the default value will depend on
            the colormodel. For the `rgb` colormodel, it is [0, 0,
            0]. For the `rgba` colormodel, it is [0, 0, 0, 0]. For
            the `rgba256` colormodel, it is [0, 0, 0, 0]. For the
            `hsl` colormodel, it is [0, 0, 0]. For the `hsla`
            colormodel, it is [0, 0, 0, 0].
        zsmooth
            Picks a smoothing algorithm used to smooth `z` data.
            This only applies for image traces that use the
            `source` attribute.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Image
        """
        ...
    


