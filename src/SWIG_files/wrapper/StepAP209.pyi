from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.STEPConstruct import *
from OCC.Core.XSControl import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *
from OCC.Core.StepFEA import *
from OCC.Core.StepRepr import *
from OCC.Core.StepElement import *
from OCC.Core.StepShape import *


class StepAP209_Construct(STEPConstruct_Tool):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, WS: XSControl_WorkSession) -> None: ...
    def CreateAP203Structure(self) -> StepData_StepModel: ...
    def CreateAdding203Entities(self, PD: StepBasic_ProductDefinition, aModel: StepData_StepModel) -> bool: ...
    def CreateAddingEntities(self, AnaPD: StepBasic_ProductDefinition) -> bool: ...
    def CreateAnalysStructure(self, Prod: StepBasic_Product) -> bool: ...
    def CreateFeaStructure(self, Prod: StepBasic_Product) -> bool: ...
    @overload
    def FeaModel(self, Prod: StepBasic_Product) -> StepFEA_FeaModel: ...
    @overload
    def FeaModel(self, PDF: StepBasic_ProductDefinitionFormation) -> StepFEA_FeaModel: ...
    @overload
    def FeaModel(self, PDS: StepRepr_ProductDefinitionShape) -> StepFEA_FeaModel: ...
    @overload
    def FeaModel(self, PD: StepBasic_ProductDefinition) -> StepFEA_FeaModel: ...
    def GetCurElemSection(self, ElemRepr: StepFEA_Curve3dElementRepresentation) -> StepElement_HSequenceOfCurveElementSectionDefinition: ...
    def GetElemGeomRelat(self) -> StepFEA_HSequenceOfElementGeometricRelationship: ...
    def GetElementMaterial(self) -> StepElement_HSequenceOfElementMaterial: ...
    def GetElements1D(self, theFeaModel: StepFEA_FeaModel) -> StepFEA_HSequenceOfElementRepresentation: ...
    def GetElements2D(self, theFEAModel: StepFEA_FeaModel) -> StepFEA_HSequenceOfElementRepresentation: ...
    def GetElements3D(self, theFEAModel: StepFEA_FeaModel) -> StepFEA_HSequenceOfElementRepresentation: ...
    def GetFeaAxis2Placement3d(self, theFeaModel: StepFEA_FeaModel) -> StepFEA_FeaAxis2Placement3d: ...
    def GetShReprForElem(self, ElemRepr: StepFEA_ElementRepresentation) -> StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self, Prod: StepBasic_Product) -> StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self, PDF: StepBasic_ProductDefinitionFormation) -> StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self, PD: StepBasic_ProductDefinition) -> StepShape_ShapeRepresentation: ...
    @overload
    def IdealShape(self, PDS: StepRepr_ProductDefinitionShape) -> StepShape_ShapeRepresentation: ...
    def Init(self, WS: XSControl_WorkSession) -> bool: ...
    def IsAnalys(self, PD: StepBasic_ProductDefinitionFormation) -> bool: ...
    def IsDesing(self, PD: StepBasic_ProductDefinitionFormation) -> bool: ...
    @overload
    def NominShape(self, Prod: StepBasic_Product) -> StepShape_ShapeRepresentation: ...
    @overload
    def NominShape(self, PDF: StepBasic_ProductDefinitionFormation) -> StepShape_ShapeRepresentation: ...
    def ReplaceCcDesingToApplied(self) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

