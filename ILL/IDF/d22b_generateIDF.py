import os
path = os.path.abspath("")
import sys
sys.path.insert(0, path)
from helper import MantidGeom

# using metre as unit
instrumentName = 'D22'
validFrom = "2020-12-01 00:00:00"
moderator_source = -2.0
# 2 Monitors
zMon1 = -16.7
zMon2 = -1.2
# Resolutions 1 (lr), 2
factor = 2
# definition of the quadratic detector
numberPixelsVertical = 128 * factor
numberPixelsHorizontal = 128
numberTubesRightDetector = 96
# definition of a quadratic pixel
pixelName = "pixel"
pixelWidth = 0.008
pixelHeight = 0.008 / factor
x = pixelWidth / 2.
y = pixelHeight / 2.
z = 0.
thickness = 0.0001
# detector
zPos = 12.8
# start identification numbers
id0 = repr(0)
id1 = repr(numberPixelsVertical*numberPixelsHorizontal)
# rectangular detector
xstart = repr(pixelWidth * (numberPixelsHorizontal - 1) / 2)
xstep = repr(-pixelWidth)
xpixels = repr(numberPixelsHorizontal)
ystart = repr(-pixelHeight * (numberPixelsVertical - 1) / 2)
ystep = repr(pixelHeight)
ypixels = repr(numberPixelsVertical)
x_gap = 0. # TO BE CHECKED
z_gap = 0. # TO BE CHECKED
xstart_right = repr((pixelWidth * (numberTubesRightDetector - 1) / 2 + x_gap))
xpixels_right = repr(numberTubesRightDetector)
right_center_offset = (numberTubesRightDetector + numberPixelsHorizontal) * pixelWidth / 2
# Choose either FF = "x", SR = repr(numberPixelsRearHorizontal) or FF = "y", SR = repr(numberPixelsRearVertical)
FF = "y"  # idfillbyfirst
SR = repr(numberPixelsVertical)  #idstepbyrow
detector0 = "detector_back"
detector1 = "detector_front"

comment = """ This is the instrument definition file of the D22B Large dynamic range small-angle diffractometer
       at the ILL.
       Generated file, PLEASE DO NOT EDIT THIS FILE!
       This file was automatically generated by mantidgeometry/ILL/IDF/d22b_generateIDF.py
       > python3 ./ILL/IDF/d22b_generateIDF.py

       z axis defines the direction of the beam
       y axis will be the axis used for rotation
       coordinate system is right-handed

       y axis rotation defined by theta
       x axis rotation defined by phi
       z axis rotation defined by chi

       width x direction, height y direction

       Collimation
       8 guide sections of 55 mm x 40 mm
       Source-to-sample distances are 1.4 m; 2.0 m; 2.8 m; 4.0 m; 5.6 m; 8.0 m; 11.2 m; 14.4 m; 17.6 m
       Variable apertures at 19.1 m

       Sample
       Default sample dimension is 10 mm x 300 mm

       Multi-detector:
       Size 1024 mm x 1024 mm
       Nominal resolution:
            128 x 256
            Pixel size 8 x 4 mm2
       Low resolution:
            128 x 128
            Pixel size 8 x 8 mm2

       Right detector:
       Same orientation of tubes, same size of pixels
       Only 96 tubes instead of 128 tubes in the main detector

       For more information, please visit
       https://www.ill.eu/instruments-support/instruments-groups/instruments/d22/characteristics/
       """
d22 = MantidGeom(instrumentName, comment=comment, valid_from=validFrom)
d22.addSnsDefaults(default_view='3D',axis_view_3d='z-')
d22.addComment("SOURCE")
d22.addComponentILL("moderator", 0., 0., moderator_source, "Source")
d22.addComment("Sample position")
d22.addComponentILL("sample_position", 0., 0., 0., "SamplePos")
d22.addComment("MONITORS")
d22.addMonitors(names=["monitor1", "monitor2"], distance=[zMon1, zMon2])
d22.addComment("MONITOR SHAPE")
d22.addDummyMonitor(0.01, 0.03)
d22.addComment("MONITOR IDs")
d22.addMonitorIds([repr(100000), repr(100001)])
d22.addComment("DETECTOR")
d22.addComponentILL("detector", 0., 0., 0.)
detector = d22.makeTypeElement("detector")
d22.addComponentRectangularDetector(detector0, 0., 0., zPos, idstart=id0, idfillbyfirst=FF, idstepbyrow=SR, root=detector)
d22.addComponentRectangularDetector(detector1, -right_center_offset, 0., zPos-z_gap, idstart=id1, idfillbyfirst=FF, idstepbyrow=SR, root=detector)
d22.addRectangularDetector(detector0, pixelName, xstart, xstep, xpixels, ystart, ystep, ypixels)
d22.addRectangularDetector(detector1, pixelName, xstart_right, xstep, xpixels_right, ystart, ystep, ypixels)
d22.addComment("PIXEL, EACH PIXEL IS A DETECTOR")
d22.addCuboidPixel(pixelName, [-x, -y, thickness/2.], [-x, y, thickness/2.], [-x, -y, -thickness/2.], [x, -y, thickness/2.], shape_id="pixel-shape")
d22.writeGeom("./ILL/IDF/" + instrumentName + "B_Definition.xml")
