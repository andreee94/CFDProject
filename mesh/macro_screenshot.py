#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

meshOpenFOAM = GetActiveSource()
meshOpenFOAMDisplay = GetDisplayProperties(meshOpenFOAM, view=renderView1)

# Properties modified on meshOpenFOAM
meshOpenFOAM.UseVTKPolyhedron = 1
# change representation type
meshOpenFOAMDisplay.SetRepresentationType('Surface With Edges')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2160, 1135]

# current camera placement for renderView1
renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
#renderView1.CameraPosition = [-4.991888999938965e-07, 0.0, 1.0138898381384234]
#renderView1.CameraFocalPoint = [-4.991888999938965e-07, 0.0, 0.11000000312924385]
#renderView1.CameraParallelScale = 0.2830721238096907

# save screenshot
SaveScreenshot('/home/andrea/Project/mesh/screenshots/all_mesh.png', renderView1, ImageResolution=[4320, 2270], TransparentBackground=1)

######################################################33

renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-0.00010231917086957684, 0.0669569661122999, 1.2037067034903473]
renderView1.CameraFocalPoint = [-0.00010231917086957684, 0.0669569661122999, 0.11000000312924385]
renderView1.CameraViewUp = [0.009028867782141547, 0.9999592389425545, 0.0]
renderView1.CameraParallelScale = 0.00353047862165632

SaveScreenshot('/home/andrea/Project/mesh/screenshots/boundary_layer.png', renderView1, ImageResolution=[4320, 2270], TransparentBackground=1)

######################################################33

renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.05051770430840953, -0.025186858122551763, 1.2235031378760821]
renderView1.CameraFocalPoint = [0.05051770430840953, -0.025186858122551763, 0.12999999895691872]
renderView1.CameraParallelScale = 0.02374687414100329

SaveScreenshot('/home/andrea/Project/mesh/screenshots/blade0.png', renderView1, ImageResolution=[4320, 2270], TransparentBackground=1)

######################################################33

renderView1.ResetCamera()
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-0.07697123832687232, -0.011091462691906548, 1.2235031378760821]
renderView1.CameraFocalPoint = [-0.07697123832687232, -0.011091462691906548, 0.12999999895691872]
renderView1.CameraParallelScale = 0.005168011697023971

SaveScreenshot('/home/andrea/Project/mesh/screenshots/blade2_LE.png', renderView1, ImageResolution=[4320, 2270], TransparentBackground=1)




