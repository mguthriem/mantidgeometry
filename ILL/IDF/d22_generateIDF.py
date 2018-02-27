
import sys
sys.path.insert(1, "../../")
from helper import MantidGeom

# using metre as unit
instrumentName = 'D22'
validFrom = "2017-10-01 23:59:59"
moderator_source = -2.0
# definition of the quadratic detector
numberPixelsVertical = 122
numberPixelsHorizontal = 128
# definition of a quadratic pixel
pixelName = "pixel"
pixelWidth = 0.008
pixelHeight = 0.008
x = pixelWidth / 2.
y = pixelHeight / 2.
z = 0.
thickness = repr(-0.0001)
# detector
zPos = 12.8
# start identification numbers
id0 = repr(0)
# rectangular detector
xstart = repr(-pixelWidth * (numberPixelsHorizontal - 1) / 2)
xstep = repr(pixelWidth)
xpixels = repr(numberPixelsHorizontal)
ystart = repr(-pixelHeight * (numberPixelsVertical - 1) / 2)
ystep = repr(pixelHeight)
ypixels = repr(numberPixelsVertical)
# Choose either FF = "x", SR = repr(numberPixelsRearHorizontal) or FF = "y", SR = repr(numberPixelsRearVertical)
FF = "y"  # idfillbyfirst
SR = repr(numberPixelsVertical)  #idstepbyrow
detector0 = "detector"

comment = """ This is the instrument definition file of the D22 Large dynamic range small-angle diffractometer
       at the ILL.
       Generated file, PLEASE DO NOT EDIT THIS FILE!
       This file was automatically generated by mantidgeometry/ILL/IDF/d22_generateIDF.py

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
       Size 1024 mm x 980 mm
       Pixel size 8 x 8 mm^2 ( 128 x 122 pixels )

       For more information, please visit
       https://www.ill.eu/instruments-support/instruments-groups/instruments/d22/characteristics/
       """
d22 = MantidGeom(instrumentName, comment=comment, valid_from=validFrom)
d22.addSnsDefaults()
d22.addComment("SOURCE")
d22.addComponentILL("moderator", 0., 0., moderator_source, "Source")
d22.addComment("Sample position")
d22.addComponentILL("sample_position", 0., 0., 0., "SamplePos")
d22.addComment("DETECTOR")
d22.addComponentRectangularDetector(detector0, 0., 0., zPos, idstart=id0, idfillbyfirst=FF, idstepbyrow=SR)
d22.addRectangularDetector(detector0, pixelName, xstart, xstep, xpixels, ystart, ystep, ypixels)
d22.addComment("PIXEL, EACH PIXEL IS A DETECTOR")
d22.addCuboidPixel(pixelName, [-x, -y, z], [x, y, z], [-x, -y, thickness], [x, -y, z], shape_id="pixel-shape")
