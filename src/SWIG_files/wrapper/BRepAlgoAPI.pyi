from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BOPAlgo import *
from OCC.Core.TopoDS import *
from OCC.Core.BRepBuilderAPI import *
from OCC.Core.TopTools import *
from OCC.Core.BRepTools import *
from OCC.Core.gp import *
from OCC.Core.Geom import *


class BRepAlgoAPI_Check(BOPAlgo_Options):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theS: TopoDS_Shape, bTestSE: Optional[bool] = True, bTestSI: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, theS1: TopoDS_Shape, theS2: TopoDS_Shape, theOp: Optional[BOPAlgo_Operation] = BOPAlgo_UNKNOWN, bTestSE: Optional[bool] = True, bTestSI: Optional[bool] = True) -> None: ...
    def IsValid(self) -> bool: ...
    def Perform(self) -> None: ...
    def Result(self) -> BOPAlgo_ListOfCheckResult: ...
    @overload
    def SetData(self, theS: TopoDS_Shape, bTestSE: Optional[bool] = True, bTestSI: Optional[bool] = True) -> None: ...
    @overload
    def SetData(self, theS1: TopoDS_Shape, theS2: TopoDS_Shape, theOp: Optional[BOPAlgo_Operation] = BOPAlgo_UNKNOWN, bTestSE: Optional[bool] = True, bTestSI: Optional[bool] = True) -> None: ...

class BRepAlgoAPI_Algo(BRepBuilderAPI_MakeShape, BOPAlgo_Options):
    def Shape(self) -> TopoDS_Shape: ...

class BRepAlgoAPI_BuilderAlgo(BRepAlgoAPI_Algo):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePF: BOPAlgo_PaveFiller) -> None: ...
    def Arguments(self) -> TopTools_ListOfShape: ...
    def Build(self) -> None: ...
    def Builder(self) -> BOPAlgo_PBuilder: ...
    def CheckInverted(self) -> bool: ...
    def DSFiller(self) -> BOPAlgo_PPaveFiller: ...
    def Generated(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def Glue(self) -> BOPAlgo_GlueEnum: ...
    def HasDeleted(self) -> bool: ...
    def HasGenerated(self) -> bool: ...
    def HasHistory(self) -> bool: ...
    def HasModified(self) -> bool: ...
    def History(self) -> BRepTools_History: ...
    def IsDeleted(self, aS: TopoDS_Shape) -> bool: ...
    def Modified(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def NonDestructive(self) -> bool: ...
    def SectionEdges(self) -> TopTools_ListOfShape: ...
    def SetArguments(self, theLS: TopTools_ListOfShape) -> None: ...
    def SetCheckInverted(self, theCheck: bool) -> None: ...
    def SetGlue(self, theGlue: BOPAlgo_GlueEnum) -> None: ...
    def SetNonDestructive(self, theFlag: bool) -> None: ...
    def SetToFillHistory(self, theHistFlag: bool) -> None: ...
    def SimplifyResult(self, theUnifyEdges: Optional[bool] = True, theUnifyFaces: Optional[bool] = True, theAngularTol: Optional[float] = precision_Angular()) -> None: ...

class BRepAlgoAPI_Defeaturing(BRepAlgoAPI_Algo):
    def __init__(self) -> None: ...
    def AddFaceToRemove(self, theFace: TopoDS_Shape) -> None: ...
    def AddFacesToRemove(self, theFaces: TopTools_ListOfShape) -> None: ...
    def Build(self) -> None: ...
    def FacesToRemove(self) -> TopTools_ListOfShape: ...
    def Generated(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def HasDeleted(self) -> bool: ...
    def HasGenerated(self) -> bool: ...
    def HasHistory(self) -> bool: ...
    def HasModified(self) -> bool: ...
    def History(self) -> BRepTools_History: ...
    def InputShape(self) -> TopoDS_Shape: ...
    def IsDeleted(self, theS: TopoDS_Shape) -> bool: ...
    def Modified(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def SetShape(self, theShape: TopoDS_Shape) -> None: ...
    def SetToFillHistory(self, theFlag: bool) -> None: ...

class BRepAlgoAPI_BooleanOperation(BRepAlgoAPI_BuilderAlgo):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePF: BOPAlgo_PaveFiller) -> None: ...
    def Build(self) -> None: ...
    def Operation(self) -> BOPAlgo_Operation: ...
    def SetOperation(self, theBOP: BOPAlgo_Operation) -> None: ...
    def SetTools(self, theLS: TopTools_ListOfShape) -> None: ...
    def Shape1(self) -> TopoDS_Shape: ...
    def Shape2(self) -> TopoDS_Shape: ...
    def Tools(self) -> TopTools_ListOfShape: ...

class BRepAlgoAPI_Splitter(BRepAlgoAPI_BuilderAlgo):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePF: BOPAlgo_PaveFiller) -> None: ...
    def Build(self) -> None: ...
    def SetTools(self, theLS: TopTools_ListOfShape) -> None: ...
    def Tools(self) -> TopTools_ListOfShape: ...

class BRepAlgoAPI_Common(BRepAlgoAPI_BooleanOperation):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PF: BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape, PF: BOPAlgo_PaveFiller) -> None: ...

class BRepAlgoAPI_Cut(BRepAlgoAPI_BooleanOperation):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PF: BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape, aDSF: BOPAlgo_PaveFiller, bFWD: Optional[bool] = True) -> None: ...

class BRepAlgoAPI_Fuse(BRepAlgoAPI_BooleanOperation):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PF: BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape, aDSF: BOPAlgo_PaveFiller) -> None: ...

class BRepAlgoAPI_Section(BRepAlgoAPI_BooleanOperation):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PF: BOPAlgo_PaveFiller) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape, PerformNow: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape, aDSF: BOPAlgo_PaveFiller, PerformNow: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, Pl: gp_Pln, PerformNow: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shape, Sf: Geom_Surface, PerformNow: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, Sf: Geom_Surface, S2: TopoDS_Shape, PerformNow: Optional[bool] = True) -> None: ...
    @overload
    def __init__(self, Sf1: Geom_Surface, Sf2: Geom_Surface, PerformNow: Optional[bool] = True) -> None: ...
    def Approximation(self, B: bool) -> None: ...
    def Build(self) -> None: ...
    def ComputePCurveOn1(self, B: bool) -> None: ...
    def ComputePCurveOn2(self, B: bool) -> None: ...
    def HasAncestorFaceOn1(self, E: TopoDS_Shape, F: TopoDS_Shape) -> bool: ...
    def HasAncestorFaceOn2(self, E: TopoDS_Shape, F: TopoDS_Shape) -> bool: ...
    @overload
    def Init1(self, S1: TopoDS_Shape) -> None: ...
    @overload
    def Init1(self, Pl: gp_Pln) -> None: ...
    @overload
    def Init1(self, Sf: Geom_Surface) -> None: ...
    @overload
    def Init2(self, S2: TopoDS_Shape) -> None: ...
    @overload
    def Init2(self, Pl: gp_Pln) -> None: ...
    @overload
    def Init2(self, Sf: Geom_Surface) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

