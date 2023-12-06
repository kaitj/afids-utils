"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Tickformatstop(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def dtickrange(self): # -> tuple[Unknown, ...] | Tickformatstop | None:
        """
            range [*min*, *max*], where "min", "max" - dtick values which
            describe some zoom level, it is possible to omit "min" or "max"
            value by passing "null"

            The 'dtickrange' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'dtickrange[0]' property accepts values of any type
        (1) The 'dtickrange[1]' property accepts values of any type

            Returns
            -------
            list
        """
        ...
    
    @dtickrange.setter
    def dtickrange(self, val): # -> None:
        ...
    
    @property
    def enabled(self): # -> tuple[Unknown, ...] | Tickformatstop | None:
        """
        Determines whether or not this stop is used. If `false`, this
        stop is ignored even within its `dtickrange`.

        The 'enabled' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @enabled.setter
    def enabled(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Unknown, ...] | Tickformatstop | None:
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

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
    def templateitemname(self): # -> tuple[Unknown, ...] | Tickformatstop | None:
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @templateitemname.setter
    def templateitemname(self, val): # -> None:
        ...
    
    @property
    def value(self): # -> tuple[Unknown, ...] | Tickformatstop | None:
        """
        string - dtickformat for described zoom level, the same as
        "tickformat"

        The 'value' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., dtickrange=..., enabled=..., name=..., templateitemname=..., value=..., **kwargs) -> None:
        """
        Construct a new Tickformatstop object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scatterpolar.m
            arker.colorbar.Tickformatstop`
        dtickrange
            range [*min*, *max*], where "min", "max" - dtick values
            which describe some zoom level, it is possible to omit
            "min" or "max" value by passing "null"
        enabled
            Determines whether or not this stop is used. If
            `false`, this stop is ignored even within its
            `dtickrange`.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        value
            string - dtickformat for described zoom level, the same
            as "tickformat"

        Returns
        -------
        Tickformatstop
        """
        ...
    


