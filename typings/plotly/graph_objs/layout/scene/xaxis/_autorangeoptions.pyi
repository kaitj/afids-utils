"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Autorangeoptions(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def clipmax(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Clip autorange maximum if it goes beyond this value. Has no
        effect when `autorangeoptions.maxallowed` is provided.

        The 'clipmax' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @clipmax.setter
    def clipmax(self, val): # -> None:
        ...
    
    @property
    def clipmin(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Clip autorange minimum if it goes beyond this value. Has no
        effect when `autorangeoptions.minallowed` is provided.

        The 'clipmin' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @clipmin.setter
    def clipmin(self, val): # -> None:
        ...
    
    @property
    def include(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Ensure this value is included in autorange.

        The 'include' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @include.setter
    def include(self, val): # -> None:
        ...
    
    @property
    def includesrc(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Sets the source reference on Chart Studio Cloud for `include`.

        The 'includesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @includesrc.setter
    def includesrc(self, val): # -> None:
        ...
    
    @property
    def maxallowed(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Use this value exactly as autorange maximum.

        The 'maxallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @maxallowed.setter
    def maxallowed(self, val): # -> None:
        ...
    
    @property
    def minallowed(self): # -> tuple[Unknown, ...] | Autorangeoptions | None:
        """
        Use this value exactly as autorange minimum.

        The 'minallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @minallowed.setter
    def minallowed(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., clipmax=..., clipmin=..., include=..., includesrc=..., maxallowed=..., minallowed=..., **kwargs) -> None:
        """
        Construct a new Autorangeoptions object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.scene.x
            axis.Autorangeoptions`
        clipmax
            Clip autorange maximum if it goes beyond this value.
            Has no effect when `autorangeoptions.maxallowed` is
            provided.
        clipmin
            Clip autorange minimum if it goes beyond this value.
            Has no effect when `autorangeoptions.minallowed` is
            provided.
        include
            Ensure this value is included in autorange.
        includesrc
            Sets the source reference on Chart Studio Cloud for
            `include`.
        maxallowed
            Use this value exactly as autorange maximum.
        minallowed
            Use this value exactly as autorange minimum.

        Returns
        -------
        Autorangeoptions
        """
        ...
    


