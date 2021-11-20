from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *


class IntRes2d_SequenceOfIntersectionPoint:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> IntRes2d_IntersectionPoint: ...
    def Last(self) -> IntRes2d_IntersectionPoint: ...
    def Length(self) -> int: ...
    def Append(self, theItem: IntRes2d_IntersectionPoint) -> IntRes2d_IntersectionPoint: ...
    def Prepend(self, theItem: IntRes2d_IntersectionPoint) -> IntRes2d_IntersectionPoint: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> IntRes2d_IntersectionPoint: ...
    def SetValue(self, theIndex: int, theValue: IntRes2d_IntersectionPoint) -> None: ...

class IntRes2d_SequenceOfIntersectionSegment:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> IntRes2d_IntersectionSegment: ...
    def Last(self) -> IntRes2d_IntersectionSegment: ...
    def Length(self) -> int: ...
    def Append(self, theItem: IntRes2d_IntersectionSegment) -> IntRes2d_IntersectionSegment: ...
    def Prepend(self, theItem: IntRes2d_IntersectionSegment) -> IntRes2d_IntersectionSegment: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> IntRes2d_IntersectionSegment: ...
    def SetValue(self, theIndex: int, theValue: IntRes2d_IntersectionSegment) -> None: ...

class IntRes2d_Position(IntEnum):
    IntRes2d_Head: int = ...
    IntRes2d_Middle: int = ...
    IntRes2d_End: int = ...

IntRes2d_Head = IntRes2d_Position.IntRes2d_Head
IntRes2d_Middle = IntRes2d_Position.IntRes2d_Middle
IntRes2d_End = IntRes2d_Position.IntRes2d_End

class IntRes2d_Situation(IntEnum):
    IntRes2d_Inside: int = ...
    IntRes2d_Outside: int = ...
    IntRes2d_Unknown: int = ...

IntRes2d_Inside = IntRes2d_Situation.IntRes2d_Inside
IntRes2d_Outside = IntRes2d_Situation.IntRes2d_Outside
IntRes2d_Unknown = IntRes2d_Situation.IntRes2d_Unknown

class IntRes2d_TypeTrans(IntEnum):
    IntRes2d_In: int = ...
    IntRes2d_Out: int = ...
    IntRes2d_Touch: int = ...
    IntRes2d_Undecided: int = ...

IntRes2d_In = IntRes2d_TypeTrans.IntRes2d_In
IntRes2d_Out = IntRes2d_TypeTrans.IntRes2d_Out
IntRes2d_Touch = IntRes2d_TypeTrans.IntRes2d_Touch
IntRes2d_Undecided = IntRes2d_TypeTrans.IntRes2d_Undecided

class IntRes2d_Domain:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Pnt1: gp_Pnt2d, Par1: float, Tol1: float, Pnt2: gp_Pnt2d, Par2: float, Tol2: float) -> None: ...
    @overload
    def __init__(self, Pnt: gp_Pnt2d, Par: float, Tol: float, First: bool) -> None: ...
    def EquivalentParameters(self) -> Tuple[float, float]: ...
    def FirstParameter(self) -> float: ...
    def FirstPoint(self) -> gp_Pnt2d: ...
    def FirstTolerance(self) -> float: ...
    def HasFirstPoint(self) -> bool: ...
    def HasLastPoint(self) -> bool: ...
    def IsClosed(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def LastPoint(self) -> gp_Pnt2d: ...
    def LastTolerance(self) -> float: ...
    def SetEquivalentParameters(self, zero: float, period: float) -> None: ...
    @overload
    def SetValues(self, Pnt1: gp_Pnt2d, Par1: float, Tol1: float, Pnt2: gp_Pnt2d, Par2: float, Tol2: float) -> None: ...
    @overload
    def SetValues(self) -> None: ...
    @overload
    def SetValues(self, Pnt: gp_Pnt2d, Par: float, Tol: float, First: bool) -> None: ...

class IntRes2d_Intersection:
    def IsDone(self) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def NbSegments(self) -> int: ...
    def Point(self, N: int) -> IntRes2d_IntersectionPoint: ...
    def Segment(self, N: int) -> IntRes2d_IntersectionSegment: ...
    def SetReversedParameters(self, Reverseflag: bool) -> None: ...

class IntRes2d_IntersectionPoint:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, Uc1: float, Uc2: float, Trans1: IntRes2d_Transition, Trans2: IntRes2d_Transition, ReversedFlag: bool) -> None: ...
    def ParamOnFirst(self) -> float: ...
    def ParamOnSecond(self) -> float: ...
    def SetValues(self, P: gp_Pnt2d, Uc1: float, Uc2: float, Trans1: IntRes2d_Transition, Trans2: IntRes2d_Transition, ReversedFlag: bool) -> None: ...
    def TransitionOfFirst(self) -> IntRes2d_Transition: ...
    def TransitionOfSecond(self) -> IntRes2d_Transition: ...
    def Value(self) -> gp_Pnt2d: ...

class IntRes2d_IntersectionSegment:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P1: IntRes2d_IntersectionPoint, P2: IntRes2d_IntersectionPoint, Oppos: bool, ReverseFlag: bool) -> None: ...
    @overload
    def __init__(self, P: IntRes2d_IntersectionPoint, First: bool, Oppos: bool, ReverseFlag: bool) -> None: ...
    @overload
    def __init__(self, Oppos: bool) -> None: ...
    def FirstPoint(self) -> IntRes2d_IntersectionPoint: ...
    def HasFirstPoint(self) -> bool: ...
    def HasLastPoint(self) -> bool: ...
    def IsOpposite(self) -> bool: ...
    def LastPoint(self) -> IntRes2d_IntersectionPoint: ...

class IntRes2d_Transition:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Tangent: bool, Pos: IntRes2d_Position, Type: IntRes2d_TypeTrans) -> None: ...
    @overload
    def __init__(self, Tangent: bool, Pos: IntRes2d_Position, Situ: IntRes2d_Situation, Oppos: bool) -> None: ...
    @overload
    def __init__(self, Pos: IntRes2d_Position) -> None: ...
    def IsOpposite(self) -> bool: ...
    def IsTangent(self) -> bool: ...
    def PositionOnCurve(self) -> IntRes2d_Position: ...
    def SetPosition(self, Pos: IntRes2d_Position) -> None: ...
    @overload
    def SetValue(self, Tangent: bool, Pos: IntRes2d_Position, Type: IntRes2d_TypeTrans) -> None: ...
    @overload
    def SetValue(self, Tangent: bool, Pos: IntRes2d_Position, Situ: IntRes2d_Situation, Oppos: bool) -> None: ...
    @overload
    def SetValue(self, Pos: IntRes2d_Position) -> None: ...
    def Situation(self) -> IntRes2d_Situation: ...
    def TransitionType(self) -> IntRes2d_TypeTrans: ...

# harray1 classes
# harray2 classes
# hsequence classes

