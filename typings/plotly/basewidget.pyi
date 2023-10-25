"""
This type stub file was generated by pyright.
"""

import ipywidgets as widgets
from .basedatatypes import BaseFigure

@widgets.register
class BaseFigureWidget(BaseFigure, widgets.DOMWidget):
    """
    Base class for FigureWidget. The FigureWidget class is code-generated as a
    subclass
    """
    _view_name = ...
    _view_module = ...
    _view_module_version = ...
    _model_name = ...
    _model_module = ...
    _model_module_version = ...
    _layout = ...
    _data = ...
    _config = ...
    _py2js_addTraces = ...
    _py2js_restyle = ...
    _py2js_relayout = ...
    _py2js_update = ...
    _py2js_animate = ...
    _py2js_deleteTraces = ...
    _py2js_moveTraces = ...
    _py2js_removeLayoutProps = ...
    _py2js_removeTraceProps = ...
    _js2py_traceDeltas = ...
    _js2py_layoutDelta = ...
    _js2py_restyle = ...
    _js2py_relayout = ...
    _js2py_update = ...
    _js2py_pointsCallback = ...
    _last_layout_edit_id = ...
    _last_trace_edit_id = ...
    _set_trace_uid = ...
    _allow_disable_validation = ...
    def __init__(self, data=..., layout=..., frames=..., skip_invalid=..., **kwargs) -> None:
        ...
    
    def on_edits_completed(self, fn): # -> None:
        """
        Register a function to be called after all pending trace and layout
        edit operations have completed

        If there are no pending edit operations then function is called
        immediately

        Parameters
        ----------
        fn : callable
            Function of zero arguments to be called when all pending edit
            operations have completed
        """
        ...
    
    @property
    def frames(self): # -> list[Unknown]:
        ...
    
    @frames.setter
    def frames(self, new_frames): # -> None:
        ...
    


