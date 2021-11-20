from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor2d import *
from OCC.Core.math import *

Adaptor3d_CurveOnSurfacePtr = NewType('Adaptor3d_CurveOnSurfacePtr', Adaptor3d_CurveOnSurface)
Adaptor3d_CurvePtr = NewType('Adaptor3d_CurvePtr', Adaptor3d_Curve)
Adaptor3d_SurfacePtr = NewType('Adaptor3d_SurfacePtr', Adaptor3d_Surface)

class Adaptor3d_Curve:
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def OffsetCurve(self) -> Geom_OffsetCurve: ...
    def Parabola(self) -> gp_Parab: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
    def Value(self, U: float) -> gp_Pnt: ...

class Adaptor3d_HCurve(Standard_Transient):
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def Curve(self) -> Adaptor3d_Curve: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetCurve(self) -> Adaptor3d_Curve: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def OffsetCurve(self) -> Geom_OffsetCurve: ...
    def Parabola(self) -> gp_Parab: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
    def Value(self, U: float) -> gp_Pnt: ...

class Adaptor3d_HSurface(Standard_Transient):
    def AxeOfRevolution(self) -> gp_Ax1: ...
    def BSpline(self) -> Geom_BSplineSurface: ...
    def BasisCurve(self) -> Adaptor3d_HCurve: ...
    def BasisSurface(self) -> Adaptor3d_HSurface: ...
    def Bezier(self) -> Geom_BezierSurface: ...
    def Cone(self) -> gp_Cone: ...
    def Cylinder(self) -> gp_Cylinder: ...
    def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
    def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
    def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
    def Direction(self) -> gp_Dir: ...
    def FirstUParameter(self) -> float: ...
    def FirstVParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_SurfaceType: ...
    def IsUClosed(self) -> bool: ...
    def IsUPeriodic(self) -> bool: ...
    def IsURational(self) -> bool: ...
    def IsVClosed(self) -> bool: ...
    def IsVPeriodic(self) -> bool: ...
    def IsVRational(self) -> bool: ...
    def LastUParameter(self) -> float: ...
    def LastVParameter(self) -> float: ...
    def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbUKnots(self) -> int: ...
    def NbUPoles(self) -> int: ...
    def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVKnots(self) -> int: ...
    def NbVPoles(self) -> int: ...
    def OffsetValue(self) -> float: ...
    def Plane(self) -> gp_Pln: ...
    def Sphere(self) -> gp_Sphere: ...
    def Surface(self) -> Adaptor3d_Surface: ...
    def Torus(self) -> gp_Torus: ...
    def UContinuity(self) -> GeomAbs_Shape: ...
    def UDegree(self) -> int: ...
    def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def UPeriod(self) -> float: ...
    def UResolution(self, R3d: float) -> float: ...
    def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    def VContinuity(self) -> GeomAbs_Shape: ...
    def VDegree(self) -> int: ...
    def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def VPeriod(self) -> float: ...
    def VResolution(self, R3d: float) -> float: ...
    def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    def Value(self, U: float, V: float) -> gp_Pnt: ...

class Adaptor3d_HSurfaceTool:
    @staticmethod
    def AxeOfRevolution(S: Adaptor3d_HSurface) -> gp_Ax1: ...
    @staticmethod
    def BSpline(S: Adaptor3d_HSurface) -> Geom_BSplineSurface: ...
    @staticmethod
    def BasisCurve(S: Adaptor3d_HSurface) -> Adaptor3d_HCurve: ...
    @staticmethod
    def BasisSurface(S: Adaptor3d_HSurface) -> Adaptor3d_HSurface: ...
    @staticmethod
    def Bezier(S: Adaptor3d_HSurface) -> Geom_BezierSurface: ...
    @staticmethod
    def Cone(S: Adaptor3d_HSurface) -> gp_Cone: ...
    @staticmethod
    def Cylinder(S: Adaptor3d_HSurface) -> gp_Cylinder: ...
    @staticmethod
    def D0(S: Adaptor3d_HSurface, u: float, v: float, P: gp_Pnt) -> None: ...
    @staticmethod
    def D1(S: Adaptor3d_HSurface, u: float, v: float, P: gp_Pnt, D1u: gp_Vec, D1v: gp_Vec) -> None: ...
    @staticmethod
    def D2(S: Adaptor3d_HSurface, u: float, v: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
    @staticmethod
    def D3(S: Adaptor3d_HSurface, u: float, v: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
    @staticmethod
    def DN(S: Adaptor3d_HSurface, u: float, v: float, Nu: int, Nv: int) -> gp_Vec: ...
    @staticmethod
    def Direction(S: Adaptor3d_HSurface) -> gp_Dir: ...
    @staticmethod
    def FirstUParameter(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def FirstVParameter(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def GetType(S: Adaptor3d_HSurface) -> GeomAbs_SurfaceType: ...
    @staticmethod
    def IsUClosed(S: Adaptor3d_HSurface) -> bool: ...
    @staticmethod
    def IsUPeriodic(S: Adaptor3d_HSurface) -> bool: ...
    @staticmethod
    def IsVClosed(S: Adaptor3d_HSurface) -> bool: ...
    @staticmethod
    def IsVPeriodic(S: Adaptor3d_HSurface) -> bool: ...
    @staticmethod
    def LastUParameter(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def LastVParameter(S: Adaptor3d_HSurface) -> float: ...
    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_HSurface) -> int: ...
    @overload
    @staticmethod
    def NbSamplesU(S: Adaptor3d_HSurface, u1: float, u2: float) -> int: ...
    @overload
    @staticmethod
    def NbSamplesV(S: Adaptor3d_HSurface) -> int: ...
    @overload
    @staticmethod
    def NbSamplesV(S: Adaptor3d_HSurface, v1: float, v2: float) -> int: ...
    @staticmethod
    def NbUIntervals(S: Adaptor3d_HSurface, Sh: GeomAbs_Shape) -> int: ...
    @staticmethod
    def NbVIntervals(S: Adaptor3d_HSurface, Sh: GeomAbs_Shape) -> int: ...
    @staticmethod
    def OffsetValue(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def Plane(S: Adaptor3d_HSurface) -> gp_Pln: ...
    @staticmethod
    def Sphere(S: Adaptor3d_HSurface) -> gp_Sphere: ...
    @staticmethod
    def Torus(S: Adaptor3d_HSurface) -> gp_Torus: ...
    @staticmethod
    def UIntervals(S: Adaptor3d_HSurface, T: TColStd_Array1OfReal, Sh: GeomAbs_Shape) -> None: ...
    @staticmethod
    def UPeriod(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def UResolution(S: Adaptor3d_HSurface, R3d: float) -> float: ...
    @staticmethod
    def UTrim(S: Adaptor3d_HSurface, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    @staticmethod
    def VIntervals(S: Adaptor3d_HSurface, T: TColStd_Array1OfReal, Sh: GeomAbs_Shape) -> None: ...
    @staticmethod
    def VPeriod(S: Adaptor3d_HSurface) -> float: ...
    @staticmethod
    def VResolution(S: Adaptor3d_HSurface, R3d: float) -> float: ...
    @staticmethod
    def VTrim(S: Adaptor3d_HSurface, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    @staticmethod
    def Value(S: Adaptor3d_HSurface, u: float, v: float) -> gp_Pnt: ...

class Adaptor3d_HVertex(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, Ori: TopAbs_Orientation, Resolution: float) -> None: ...
    def IsSame(self, Other: Adaptor3d_HVertex) -> bool: ...
    def Orientation(self) -> TopAbs_Orientation: ...
    def Parameter(self, C: Adaptor2d_HCurve2d) -> float: ...
    def Resolution(self, C: Adaptor2d_HCurve2d) -> float: ...
    def Value(self) -> gp_Pnt2d: ...

class Adaptor3d_InterFunc(math_FunctionWithDerivative):
    def __init__(self, C: Adaptor2d_HCurve2d, FixVal: float, Fix: int) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Adaptor3d_Surface:
    def AxeOfRevolution(self) -> gp_Ax1: ...
    def BSpline(self) -> Geom_BSplineSurface: ...
    def BasisCurve(self) -> Adaptor3d_HCurve: ...
    def BasisSurface(self) -> Adaptor3d_HSurface: ...
    def Bezier(self) -> Geom_BezierSurface: ...
    def Cone(self) -> gp_Cone: ...
    def Cylinder(self) -> gp_Cylinder: ...
    def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
    def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
    def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
    def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
    def Direction(self) -> gp_Dir: ...
    def FirstUParameter(self) -> float: ...
    def FirstVParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_SurfaceType: ...
    def IsUClosed(self) -> bool: ...
    def IsUPeriodic(self) -> bool: ...
    def IsURational(self) -> bool: ...
    def IsVClosed(self) -> bool: ...
    def IsVPeriodic(self) -> bool: ...
    def IsVRational(self) -> bool: ...
    def LastUParameter(self) -> float: ...
    def LastVParameter(self) -> float: ...
    def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbUKnots(self) -> int: ...
    def NbUPoles(self) -> int: ...
    def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbVKnots(self) -> int: ...
    def NbVPoles(self) -> int: ...
    def OffsetValue(self) -> float: ...
    def Plane(self) -> gp_Pln: ...
    def Sphere(self) -> gp_Sphere: ...
    def Torus(self) -> gp_Torus: ...
    def UContinuity(self) -> GeomAbs_Shape: ...
    def UDegree(self) -> int: ...
    def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def UPeriod(self) -> float: ...
    def UResolution(self, R3d: float) -> float: ...
    def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    def VContinuity(self) -> GeomAbs_Shape: ...
    def VDegree(self) -> int: ...
    def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def VPeriod(self) -> float: ...
    def VResolution(self, R3d: float) -> float: ...
    def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
    def Value(self, U: float, V: float) -> gp_Pnt: ...

class Adaptor3d_TopolTool(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Surface: Adaptor3d_HSurface) -> None: ...
    def BSplSamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None: ...
    def Classify(self, P: gp_Pnt2d, Tol: float, ReacdreOnPeriodic: Optional[bool] = True) -> TopAbs_State: ...
    def ComputeSamplePoints(self) -> None: ...
    def DomainIsInfinite(self) -> bool: ...
    def Edge(self) -> None: ...
    def Has3d(self) -> bool: ...
    def Identical(self, V1: Adaptor3d_HVertex, V2: Adaptor3d_HVertex) -> bool: ...
    def Init(self) -> None: ...
    def InitVertexIterator(self) -> None: ...
    @overload
    def Initialize(self) -> None: ...
    @overload
    def Initialize(self, S: Adaptor3d_HSurface) -> None: ...
    @overload
    def Initialize(self, Curve: Adaptor2d_HCurve2d) -> None: ...
    def IsThePointOn(self, P: gp_Pnt2d, Tol: float, ReacdreOnPeriodic: Optional[bool] = True) -> bool: ...
    def IsUniformSampling(self) -> bool: ...
    def More(self) -> bool: ...
    def MoreVertex(self) -> bool: ...
    def NbSamples(self) -> int: ...
    def NbSamplesU(self) -> int: ...
    def NbSamplesV(self) -> int: ...
    def Next(self) -> None: ...
    def NextVertex(self) -> None: ...
    @overload
    def Orientation(self, C: Adaptor2d_HCurve2d) -> TopAbs_Orientation: ...
    @overload
    def Orientation(self, V: Adaptor3d_HVertex) -> TopAbs_Orientation: ...
    def Pnt(self, V: Adaptor3d_HVertex) -> gp_Pnt: ...
    def SamplePnts(self, theDefl: float, theNUmin: int, theNVmin: int) -> None: ...
    def SamplePoint(self, Index: int, P2d: gp_Pnt2d, P3d: gp_Pnt) -> None: ...
    @overload
    def Tol3d(self, C: Adaptor2d_HCurve2d) -> float: ...
    @overload
    def Tol3d(self, V: Adaptor3d_HVertex) -> float: ...
    def UParameters(self, theArray: TColStd_Array1OfReal) -> None: ...
    def VParameters(self, theArray: TColStd_Array1OfReal) -> None: ...
    def Value(self) -> Adaptor2d_HCurve2d: ...
    def Vertex(self) -> Adaptor3d_HVertex: ...

class Adaptor3d_CurveOnSurface(Adaptor3d_Curve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_HSurface) -> None: ...
    @overload
    def __init__(self, C: Adaptor2d_HCurve2d, S: Adaptor3d_HSurface) -> None: ...
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def ChangeCurve(self) -> Adaptor2d_HCurve2d: ...
    def ChangeSurface(self) -> Adaptor3d_HSurface: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetCurve(self) -> Adaptor2d_HCurve2d: ...
    def GetSurface(self) -> Adaptor3d_HSurface: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    @overload
    def Load(self, S: Adaptor3d_HSurface) -> None: ...
    @overload
    def Load(self, C: Adaptor2d_HCurve2d) -> None: ...
    @overload
    def Load(self, C: Adaptor2d_HCurve2d, S: Adaptor3d_HSurface) -> None: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def Parabola(self) -> gp_Parab: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
    def Value(self, U: float) -> gp_Pnt: ...

class Adaptor3d_HCurveOnSurface(Adaptor3d_HCurve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_CurveOnSurface) -> None: ...
    def ChangeCurve(self) -> Adaptor3d_CurveOnSurface: ...
    def Curve(self) -> Adaptor3d_Curve: ...
    def GetCurve(self) -> Adaptor3d_Curve: ...
    def Set(self, C: Adaptor3d_CurveOnSurface) -> None: ...

class Adaptor3d_HIsoCurve(Adaptor3d_HCurve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Adaptor3d_IsoCurve) -> None: ...
    def ChangeCurve(self) -> Adaptor3d_IsoCurve: ...
    def Curve(self) -> Adaptor3d_Curve: ...
    def GetCurve(self) -> Adaptor3d_Curve: ...
    def Set(self, C: Adaptor3d_IsoCurve) -> None: ...

class Adaptor3d_IsoCurve(Adaptor3d_Curve):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_HSurface) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_HSurface, Iso: GeomAbs_IsoType, Param: float) -> None: ...
    @overload
    def __init__(self, S: Adaptor3d_HSurface, Iso: GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None: ...
    def BSpline(self) -> Geom_BSplineCurve: ...
    def Bezier(self) -> Geom_BezierCurve: ...
    def Circle(self) -> gp_Circ: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def D0(self, U: float, P: gp_Pnt) -> None: ...
    def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
    def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
    def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips: ...
    def FirstParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def Iso(self) -> GeomAbs_IsoType: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin: ...
    @overload
    def Load(self, S: Adaptor3d_HSurface) -> None: ...
    @overload
    def Load(self, Iso: GeomAbs_IsoType, Param: float) -> None: ...
    @overload
    def Load(self, Iso: GeomAbs_IsoType, Param: float, WFirst: float, WLast: float) -> None: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def Parabola(self) -> gp_Parab: ...
    def Parameter(self) -> float: ...
    def Period(self) -> float: ...
    def Resolution(self, R3d: float) -> float: ...
    def Surface(self) -> Adaptor3d_HSurface: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
    def Value(self, U: float) -> gp_Pnt: ...

# harray1 classes
# harray2 classes
# hsequence classes

Adaptor3d_HSurfaceTool_AxeOfRevolution = Adaptor3d_HSurfaceTool.AxeOfRevolution
Adaptor3d_HSurfaceTool_BSpline = Adaptor3d_HSurfaceTool.BSpline
Adaptor3d_HSurfaceTool_BasisCurve = Adaptor3d_HSurfaceTool.BasisCurve
Adaptor3d_HSurfaceTool_BasisSurface = Adaptor3d_HSurfaceTool.BasisSurface
Adaptor3d_HSurfaceTool_Bezier = Adaptor3d_HSurfaceTool.Bezier
Adaptor3d_HSurfaceTool_Cone = Adaptor3d_HSurfaceTool.Cone
Adaptor3d_HSurfaceTool_Cylinder = Adaptor3d_HSurfaceTool.Cylinder
Adaptor3d_HSurfaceTool_D0 = Adaptor3d_HSurfaceTool.D0
Adaptor3d_HSurfaceTool_D1 = Adaptor3d_HSurfaceTool.D1
Adaptor3d_HSurfaceTool_D2 = Adaptor3d_HSurfaceTool.D2
Adaptor3d_HSurfaceTool_D3 = Adaptor3d_HSurfaceTool.D3
Adaptor3d_HSurfaceTool_DN = Adaptor3d_HSurfaceTool.DN
Adaptor3d_HSurfaceTool_Direction = Adaptor3d_HSurfaceTool.Direction
Adaptor3d_HSurfaceTool_FirstUParameter = Adaptor3d_HSurfaceTool.FirstUParameter
Adaptor3d_HSurfaceTool_FirstVParameter = Adaptor3d_HSurfaceTool.FirstVParameter
Adaptor3d_HSurfaceTool_GetType = Adaptor3d_HSurfaceTool.GetType
Adaptor3d_HSurfaceTool_IsUClosed = Adaptor3d_HSurfaceTool.IsUClosed
Adaptor3d_HSurfaceTool_IsUPeriodic = Adaptor3d_HSurfaceTool.IsUPeriodic
Adaptor3d_HSurfaceTool_IsVClosed = Adaptor3d_HSurfaceTool.IsVClosed
Adaptor3d_HSurfaceTool_IsVPeriodic = Adaptor3d_HSurfaceTool.IsVPeriodic
Adaptor3d_HSurfaceTool_LastUParameter = Adaptor3d_HSurfaceTool.LastUParameter
Adaptor3d_HSurfaceTool_LastVParameter = Adaptor3d_HSurfaceTool.LastVParameter
Adaptor3d_HSurfaceTool_NbSamplesU = Adaptor3d_HSurfaceTool.NbSamplesU
Adaptor3d_HSurfaceTool_NbSamplesU = Adaptor3d_HSurfaceTool.NbSamplesU
Adaptor3d_HSurfaceTool_NbSamplesV = Adaptor3d_HSurfaceTool.NbSamplesV
Adaptor3d_HSurfaceTool_NbSamplesV = Adaptor3d_HSurfaceTool.NbSamplesV
Adaptor3d_HSurfaceTool_NbUIntervals = Adaptor3d_HSurfaceTool.NbUIntervals
Adaptor3d_HSurfaceTool_NbVIntervals = Adaptor3d_HSurfaceTool.NbVIntervals
Adaptor3d_HSurfaceTool_OffsetValue = Adaptor3d_HSurfaceTool.OffsetValue
Adaptor3d_HSurfaceTool_Plane = Adaptor3d_HSurfaceTool.Plane
Adaptor3d_HSurfaceTool_Sphere = Adaptor3d_HSurfaceTool.Sphere
Adaptor3d_HSurfaceTool_Torus = Adaptor3d_HSurfaceTool.Torus
Adaptor3d_HSurfaceTool_UIntervals = Adaptor3d_HSurfaceTool.UIntervals
Adaptor3d_HSurfaceTool_UPeriod = Adaptor3d_HSurfaceTool.UPeriod
Adaptor3d_HSurfaceTool_UResolution = Adaptor3d_HSurfaceTool.UResolution
Adaptor3d_HSurfaceTool_UTrim = Adaptor3d_HSurfaceTool.UTrim
Adaptor3d_HSurfaceTool_VIntervals = Adaptor3d_HSurfaceTool.VIntervals
Adaptor3d_HSurfaceTool_VPeriod = Adaptor3d_HSurfaceTool.VPeriod
Adaptor3d_HSurfaceTool_VResolution = Adaptor3d_HSurfaceTool.VResolution
Adaptor3d_HSurfaceTool_VTrim = Adaptor3d_HSurfaceTool.VTrim
Adaptor3d_HSurfaceTool_Value = Adaptor3d_HSurfaceTool.Value
