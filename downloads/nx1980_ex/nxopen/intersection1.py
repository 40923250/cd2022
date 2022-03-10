

import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 
 
    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Block...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
 
 
    if not workPart.Preferences.Modeling.GetHistoryMode() :
        raise NXOpen.NXException("Create or edit of a Feature was recorded in History Mode but playback is in History-Free Mode.")
    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
 
    blockFeatureBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
 
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    blockFeatureBuilder1.BooleanOption.SetTargetBodies(targetBodies1)
 
    blockFeatureBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
 
    theSession.SetUndoMarkName(markId1, "Block Dialog")
 
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
 
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Block")
 
    blockFeatureBuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
 
    blockFeatureBuilder1.OriginPoint = point1
 
    originPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "100", "50", "20")
 
    blockFeatureBuilder1.SetBooleanOperationAndTarget(NXOpen.Features.Feature.BooleanType.Create, NXOpen.Body.Null)
 
    feature1 = blockFeatureBuilder1.CommitFeature()
 
    theSession.DeleteUndoMark(markId3, None)
 
    theSession.SetUndoMarkName(markId1, "Block")
 
    blockFeatureBuilder1.Destroy()
 
    # ----------------------------------------------
    #   Menu: Insert->Datum/Point->Datum Plane...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
 
    datumPlaneBuilder1 = workPart.Features.CreateDatumPlaneBuilder(NXOpen.Features.Feature.Null)
 
    plane1 = datumPlaneBuilder1.GetPlane()
 
    theSession.SetUndoMarkName(markId4, "Datum Plane Dialog")
 
    plane1.SetUpdateOption(NXOpen.SmartObject.UpdateOption.WithinModeling)
 
    plane1.SetMethod(NXOpen.PlaneTypes.MethodType.Distance)
 
    block1 = feature1
    face1 = block1.FindObject("FACE 3 {(0,25,10) BLOCK(3)}")
    face2 = block1.FindObject("FACE 6 {(100,25,10) BLOCK(3)}")
 
    plane1.SetMethod(NXOpen.PlaneTypes.MethodType.Center)
 
    plane1.SetGeometry([face1, face2])
 
    plane1.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
 
    plane1.Evaluate()
 
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Datum Plane")
 
    plane1.RemoveOffsetData()
 
    plane1.Evaluate()
 
    corner1_1 = NXOpen.Point3d(50.0, -1.25, -1.25)
    corner2_1 = NXOpen.Point3d(50.0, -1.25, 21.25)
    corner3_1 = NXOpen.Point3d(50.0, 51.25, 21.25)
    corner4_1 = NXOpen.Point3d(50.0, 51.25, -1.25)
    datumPlaneBuilder1.SetCornerPoints(corner1_1, corner2_1, corner3_1, corner4_1)
 
    datumPlaneBuilder1.ResizeDuringUpdate = True
 
    feature2 = datumPlaneBuilder1.CommitFeature()
 
    datumPlaneFeature1 = feature2
    datumPlane1 = datumPlaneFeature1.DatumPlane
 
    datumPlane1.SetReverseSection(False)
 
    theSession.DeleteUndoMark(markId6, None)
 
    theSession.SetUndoMarkName(markId4, "Datum Plane")
 
    datumPlaneBuilder1.Destroy()
 
    # ----------------------------------------------
    #   Menu: Insert->Derived Curve->Intersect...
    # ----------------------------------------------
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
 
    intersectionCurveBuilder1 = workPart.Features.CreateIntersectionCurveBuilder(NXOpen.Features.Feature.Null)
 
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
 
    intersectionCurveBuilder1.CurveFitData.Tolerance = 0.01
 
    intersectionCurveBuilder1.CurveFitData.AngleTolerance = 0.5
 
    theSession.SetUndoMarkName(markId7, "Intersection Curve Dialog")
 
    body1 = feature1.GetBodies()[0]
    faceBodyRule1 = workPart.ScRuleFactory.CreateRuleFaceBody(body1)
 
    rules1 = [None] * 1 
    rules1[0] = faceBodyRule1
    intersectionCurveBuilder1.FirstFace.ReplaceRules(rules1, False)
 
    objects1 = body1.GetFaces()
    added1 = intersectionCurveBuilder1.FirstSet.Add(objects1)
 
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Distance)
 
    plane3.SetGeometry([datumPlane1])
 
    plane3.Evaluate()
 
    intersectionCurveBuilder1.SecondPlane = plane3
 
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Intersection Curve")
 
    nXObject1 = intersectionCurveBuilder1.Commit()
 
    theSession.DeleteUndoMark(markId9, None)
 
    theSession.SetUndoMarkName(markId7, "Intersection Curve")
 
    intersectionCurveBuilder1.Destroy()
 
 
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
 
if __name__ == '__main__':
    main()