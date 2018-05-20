########################################################################################
########################################################################################
########################################################################################
########################################################################################

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
meshOpenFOAM = GetActiveSource()

# Properties modified on meshOpenFOAM
meshOpenFOAM.IncludeSets = 1
meshOpenFOAM.IncludeZones = 1
meshOpenFOAM.MeshParts = ['internalMesh', 'cyclicAMI - group', 'AMI-int1 - group', 'wall - group', 'blades - group', 'AMI-int2 - group', 'AMI-int0 - group', 'AMI-ext - group', 'walls - patch', 'inlet - patch', 'front - patch', 'outlet - patch', 'blade0 - patch', 'blade1 - patch', 'blade2 - patch', 'AMI-ext-master - patch', 'AMI-ext-slave - patch', 'AMI-int0-master - patch', 'AMI-int0-slave - patch', 'AMI-int1-master - patch', 'AMI-int1-slave - patch', 'AMI-int2-master - patch', 'AMI-int2-slave - patch']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2004, 1141]

# show data in view
meshOpenFOAMDisplay = Show(meshOpenFOAM, renderView1)
# trace defaults for the display properties.
meshOpenFOAMDisplay.Representation = 'Surface'
meshOpenFOAMDisplay.ColorArrayName = [None, '']
meshOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
meshOpenFOAMDisplay.SelectOrientationVectors = 'None'
meshOpenFOAMDisplay.ScaleFactor = 0.04000000059604645
meshOpenFOAMDisplay.SelectScaleArray = 'None'
meshOpenFOAMDisplay.GlyphType = 'Arrow'
meshOpenFOAMDisplay.GlyphTableIndexArray = 'None'
meshOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
meshOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(meshOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
meshOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# Properties modified on meshOpenFOAM
meshOpenFOAM.UseVTKPolyhedron = 1
meshOpenFOAM.MeshParts = ['internalMesh', 'cyclicAMI - group', 'AMI-int1 - group', 'wall - group', 'blades - group', 'AMI-int2 - group', 'AMI-int0 - group', 'AMI-ext - group', 'walls - patch', 'inlet - patch', 'front - patch', 'outlet - patch', 'blade0 - patch', 'blade1 - patch', 'blade2 - patch', 'AMI-ext-master - patch', 'AMI-ext-slave - patch', 'AMI-int0-master - patch', 'AMI-int0-slave - patch', 'AMI-int1-master - patch', 'AMI-int1-slave - patch', 'AMI-int2-master - patch', 'AMI-int2-slave - patch', 'steady - cellZone', 'cellzone-int0 - cellZone', 'cellzone-int1 - cellZone', 'cellzone-int2 - cellZone', 'facezone-ext - faceZone', 'facezone-int0 - faceZone', 'facezone-int1 - faceZone', 'facezone-int2 - faceZone', 'AMI-ext - faceZone', 'AMI-int0 - faceZone', 'AMI-int1 - faceZone', 'AMI-int2 - faceZone']

# update the view to ensure updated data information
renderView1.Update()

# change representation type
meshOpenFOAMDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 1.0337216013694503]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.12999999895691872]
renderView1.CameraParallelScale = 0.283019438231667

# save screenshot
SaveScreenshot('/home/andrea/OpenFOAM/andrea-5.0/run/CFDProject/mesh/screenshots-week2/main_view_colored.png', renderView1, ImageResolution=[1920, 1080],
    TransparentBackground=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 1.0337216013694503]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.12999999895691872]
renderView1.CameraParallelScale = 0.283019438231667

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################


paraview.simple._DisableFirstRenderCameraReset()

# get active source.
meshOpenFOAM = GetActiveSource()

# Properties modified on meshOpenFOAM
meshOpenFOAM.MeshParts = ['internalMesh', 'blade0 - patch', 'blade1 - patch', 'blade2 - patch', 'AMI-ext-master - patch', 'AMI-ext-slave - patch', 'AMI-int0-master - patch', 'AMI-int0-slave - patch', 'AMI-int1-master - patch', 'AMI-int1-slave - patch', 'AMI-int2-master - patch', 'AMI-int2-slave - patch']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2004, 1139]

# show data in view
meshOpenFOAMDisplay = Show(meshOpenFOAM, renderView1)
# trace defaults for the display properties.
meshOpenFOAMDisplay.Representation = 'Surface'
meshOpenFOAMDisplay.ColorArrayName = [None, '']
meshOpenFOAMDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
meshOpenFOAMDisplay.SelectOrientationVectors = 'None'
meshOpenFOAMDisplay.ScaleFactor = 0.04000000059604645
meshOpenFOAMDisplay.SelectScaleArray = 'None'
meshOpenFOAMDisplay.GlyphType = 'Arrow'
meshOpenFOAMDisplay.GlyphTableIndexArray = 'None'
meshOpenFOAMDisplay.DataAxesGrid = 'GridAxesRepresentation'
meshOpenFOAMDisplay.PolarAxes = 'PolarAxesRepresentation'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
#ColorBy(meshOpenFOAMDisplay, ('FIELD', 'vtkBlockColors'))
#ColorBy(meshOpenFOAMDisplay, ('FIELD', 'Solid Color'))

# show color bar/color legend
meshOpenFOAMDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
#vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=meshOpenFOAM)

# Properties modified on extractBlock1
extractBlock1.BlockIndices = [7, 9, 11, 13]

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1)
# trace defaults for the display properties.
extractBlock1Display.Representation = 'Surface'
extractBlock1Display.ColorArrayName = [None, '']
extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock1Display.SelectOrientationVectors = 'None'
extractBlock1Display.ScaleFactor = 0.02199999988079071
extractBlock1Display.SelectScaleArray = 'None'
extractBlock1Display.GlyphType = 'Arrow'
extractBlock1Display.GlyphTableIndexArray = 'None'
extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(meshOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
#ColorBy(extractBlock1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractBlock1Display.SetScalarBarVisibility(renderView1, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
#HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# change solid color
extractBlock1Display.DiffuseColor = [0.0, 0.6666666666666666, 1.0]

# set active source
SetActiveSource(meshOpenFOAM)

# create a new 'Extract Block'
extractBlock2 = ExtractBlock(Input=meshOpenFOAM)

# Properties modified on extractBlock2
extractBlock2.BlockIndices = [8, 10, 12, 14]

# show data in view
extractBlock2Display = Show(extractBlock2, renderView1)
# trace defaults for the display properties.
extractBlock2Display.Representation = 'Surface'
extractBlock2Display.ColorArrayName = [None, '']
extractBlock2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock2Display.SelectOrientationVectors = 'None'
extractBlock2Display.ScaleFactor = 0.02199999988079071
extractBlock2Display.SelectScaleArray = 'None'
extractBlock2Display.GlyphType = 'Arrow'
extractBlock2Display.GlyphTableIndexArray = 'None'
extractBlock2Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock2Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(meshOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
#ColorBy(extractBlock2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractBlock2Display.SetScalarBarVisibility(renderView1, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
#HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# change solid color
extractBlock2Display.DiffuseColor = [1.0, 0.3333333333333333, 0.0]

# Properties modified on extractBlock2Display
extractBlock2Display.Position = [0.0, 0.0, 0.05]

# Properties modified on extractBlock2Display.DataAxesGrid
extractBlock2Display.DataAxesGrid.Position = [0.0, 0.0, 0.05]

# Properties modified on extractBlock2Display.PolarAxes
extractBlock2Display.PolarAxes.Translation = [0.0, 0.0, 0.05]

# Properties modified on extractBlock2Display
extractBlock2Display.Position = [0.0, 0.0, 0.1]

# Properties modified on extractBlock2Display.DataAxesGrid
extractBlock2Display.DataAxesGrid.Position = [0.0, 0.0, 0.1]

# Properties modified on extractBlock2Display.PolarAxes
extractBlock2Display.PolarAxes.Translation = [0.0, 0.0, 0.1]

# set active source
SetActiveSource(meshOpenFOAM)

# create a new 'Extract Block'
extractBlock3 = ExtractBlock(Input=meshOpenFOAM)

# Properties modified on extractBlock3
extractBlock3.BlockIndices = [4, 5, 6]

# show data in view
extractBlock3Display = Show(extractBlock3, renderView1)
# trace defaults for the display properties.
extractBlock3Display.Representation = 'Surface'
extractBlock3Display.ColorArrayName = [None, '']
extractBlock3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock3Display.SelectOrientationVectors = 'None'
extractBlock3Display.ScaleFactor = 0.015598680078983308
extractBlock3Display.SelectScaleArray = 'None'
extractBlock3Display.GlyphType = 'Arrow'
extractBlock3Display.GlyphTableIndexArray = 'None'
extractBlock3Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock3Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(meshOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
#ColorBy(extractBlock3Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractBlock3Display.SetScalarBarVisibility(renderView1, True)

# Hide the scalar bar for this color map if no visible data is colored by it.
#HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# change solid color
extractBlock3Display.DiffuseColor = [0.3333333333333333, 0.6666666666666666, 0.0]

# Properties modified on extractBlock3Display
extractBlock3Display.Position = [0.0, 0.0, 0.2]

# Properties modified on extractBlock3Display.DataAxesGrid
extractBlock3Display.DataAxesGrid.Position = [0.0, 0.0, 0.2]

# Properties modified on extractBlock3Display.PolarAxes
extractBlock3Display.PolarAxes.Translation = [0.0, 0.0, 0.2]

# change representation type
extractBlock3Display.SetRepresentationType('Surface With Edges')

# set active source
SetActiveSource(extractBlock1)

# set active source
SetActiveSource(extractBlock2)

# set active source
SetActiveSource(extractBlock1)

# change representation type
extractBlock1Display.SetRepresentationType('Surface With Edges')

# set active source
SetActiveSource(extractBlock2)

# change representation type
extractBlock2Display.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [-0.39520630940395857, 0.12222159184484838, 0.5911875343884687]
renderView1.CameraFocalPoint = [0.03696219481237273, -0.0011201443523515889, 0.16808031593345196]
renderView1.CameraViewUp = [0.13932409187147643, 0.9798199676242031, -0.14332350982687384]
renderView1.CameraParallelScale = 0.283019438231667

# save screenshot
SaveScreenshot('/home/andrea/OpenFOAM/andrea-5.0/run/CFDProject/mesh/screenshots-week2/exploded_edges.png', renderView1, ImageResolution=[1920, 1080],
    TransparentBackground=1)

# set active source
SetActiveSource(extractBlock1)

# set active source
SetActiveSource(extractBlock2)

# set active source
SetActiveSource(extractBlock3)

# change representation type
extractBlock3Display.SetRepresentationType('Surface')

# set active source
SetActiveSource(extractBlock2)

# change representation type
extractBlock2Display.SetRepresentationType('Surface')

# set active source
SetActiveSource(extractBlock1)

# change representation type
extractBlock1Display.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.CameraPosition = [-0.39520630940395857, 0.12222159184484838, 0.5911875343884687]
renderView1.CameraFocalPoint = [0.03696219481237273, -0.0011201443523515889, 0.16808031593345196]
renderView1.CameraViewUp = [0.13932409187147643, 0.9798199676242031, -0.14332350982687384]
renderView1.CameraParallelScale = 0.283019438231667

# save screenshot
SaveScreenshot('/home/andrea/OpenFOAM/andrea-5.0/run/CFDProject/mesh/screenshots-week2/exploded.png', renderView1, ImageResolution=[1920, 1080],
    TransparentBackground=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.39520630940395857, 0.12222159184484838, 0.5911875343884687]
renderView1.CameraFocalPoint = [0.03696219481237273, -0.0011201443523515889, 0.16808031593345196]
renderView1.CameraViewUp = [0.13932409187147643, 0.9798199676242031, -0.14332350982687384]
renderView1.CameraParallelScale = 0.283019438231667

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).





