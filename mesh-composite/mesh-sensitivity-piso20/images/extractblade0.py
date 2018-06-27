#### import the simple module from the paraview
from paraview.simple import *
from random import randint
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
mainOpenFOAM = GetActiveSource()

# Properties modified on mainOpenFOAM
mainOpenFOAM.IncludeZones = 1
mainOpenFOAM.MeshParts = []

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1763, 1132]

# update the view to ensure updated data information
renderView1.Update()

# get display properties
mainOpenFOAMDisplay = GetDisplayProperties(mainOpenFOAM, view=renderView1)

# Properties modified on mainOpenFOAM
mainOpenFOAM.UseVTKPolyhedron = 1
mainOpenFOAM.MeshParts = []

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on mainOpenFOAM
mainOpenFOAM.MeshParts = ['cellZone-blade0 - cellZone']

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# reset view to fit data
renderView1.ResetCamera()

# change representation type
mainOpenFOAMDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.047621378442272544, -0.027499999850988388, 0.4779319785926696]
renderView1.CameraFocalPoint = [0.047621378442272544, -0.027499999850988388, 0.0]
renderView1.CameraParallelScale = 0.04769089461508987

# save screenshot
SaveScreenshot('/media/andrea/MyPassport/CFDProject/mesh-composite/mesh-sensitivity-piso20/images/mesh20-blade0-noregion' + str(randint(0, 1000)) +  '.png', renderView1, ImageResolution=[1920, 1080])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.047621378442272544, -0.027499999850988388, 0.4779319785926696]
renderView1.CameraFocalPoint = [0.047621378442272544, -0.027499999850988388, 0.0]
renderView1.CameraParallelScale = 0.04769089461508987

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
