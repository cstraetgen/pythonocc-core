from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *

#the following typedef cannot be wrapped as is
TopTrans_Array2OfOrientation = NewType('TopTrans_Array2OfOrientation', Any)

class TopTrans_CurveTransition:
    def __init__(self) -> None: ...
    def Compare(self, Tole: float, Tang: gp_Dir, Norm: gp_Dir, Curv: float, S: TopAbs_Orientation, Or: TopAbs_Orientation) -> None: ...
    @overload
    def Reset(self, Tgt: gp_Dir, Norm: gp_Dir, Curv: float) -> None: ...
    @overload
    def Reset(self, Tgt: gp_Dir) -> None: ...
    def StateAfter(self) -> TopAbs_State: ...
    def StateBefore(self) -> TopAbs_State: ...

class TopTrans_SurfaceTransition:
    def __init__(self) -> None: ...
    @overload
    def Compare(self, Tole: float, Norm: gp_Dir, MaxD: gp_Dir, MinD: gp_Dir, MaxCurv: float, MinCurv: float, S: TopAbs_Orientation, O: TopAbs_Orientation) -> None: ...
    @overload
    def Compare(self, Tole: float, Norm: gp_Dir, S: TopAbs_Orientation, O: TopAbs_Orientation) -> None: ...
    @staticmethod
    def GetAfter(Tran: TopAbs_Orientation) -> TopAbs_State: ...
    @staticmethod
    def GetBefore(Tran: TopAbs_Orientation) -> TopAbs_State: ...
    @overload
    def Reset(self, Tgt: gp_Dir, Norm: gp_Dir, MaxD: gp_Dir, MinD: gp_Dir, MaxCurv: float, MinCurv: float) -> None: ...
    @overload
    def Reset(self, Tgt: gp_Dir, Norm: gp_Dir) -> None: ...
    def StateAfter(self) -> TopAbs_State: ...
    def StateBefore(self) -> TopAbs_State: ...

# harray1 classes
# harray2 classes
# hsequence classes

TopTrans_SurfaceTransition_GetAfter = TopTrans_SurfaceTransition.GetAfter
TopTrans_SurfaceTransition_GetBefore = TopTrans_SurfaceTransition.GetBefore
