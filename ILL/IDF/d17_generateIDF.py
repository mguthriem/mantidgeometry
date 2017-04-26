#!/usr/bin/python
# change to the directory of this file and run it on command line with python d17_generateIDF.py
import sys
# user dependent path
user_path = "/home/cs/reimund/"
# insert path to find module helper (to be modified by user)
sys.path.insert(1, user_path + "geometry_description/mantidgeometry")
from helper import MantidGeom

# using metre as unit
instrumentName = 'D17'
validFrom = "2017-01-31 23:59:59"
pixelWidth = 0.001195
detectorHeight = 0.48
numberOfPixelsPerTube = 256
chop1_source = -4.164  # chopper sample distance (from Nexus file VirtualChopper.dist_chop_samp) in meter
detValue = 3.1  # sample - detector distance (from Nexus file det.target_value)
# 2 Monitors
zMon1 = 0.0181
zMon2 = -0.5
# definition of the rectangular detector
xstart = repr(- (pixelWidth * (numberOfPixelsPerTube - 1) / 2))
xstep = repr(pixelWidth)
xpixels = repr(numberOfPixelsPerTube)
ystart = "0"
ystep = repr(detectorHeight)
ypixels = "1"
thickness = repr(-0.0001)
# definition of a cuboid pixel
x = pixelWidth / 2
y = detectorHeight / 2
z = 0.0

xml_outfile = user_path + "mantid/instrument/" + instrumentName + "_Definition.xml"
comment = """ This is the instrument definition file of the D17 reflectometer at the ILL.
       Generated file, PLEASE DO NOT EDIT THIS FILE!
       This file was automatically generated by geometry_description/mandidgeometry/ILL/IDF/d17_generatorIDF.py

       z axis defines the direction of the direct beam
       y axis will be the axis used for rotation in the LoadILLReflectometry algorithm
       coordinate system is right-handed

       y axis rotation defined by theta
       x axis rotation defined by phi
       z axis rotation defined by chi

       ILL monoblock tube detector - width x direction, height y direction

       The detector is of size 300 mm x 480 mm and flat, its shape is rectangular
       Its resolution is 2.2 mm x 4.8 mm (width x height FWHM)
       Rotation -2 to 45 degrees

       It consists of 64 horizontal tubes, each has a height of 7.4 mm
       It consists of 256 pixels. each about 1.195 mm wide

       Time-of-flight mode:
       Beam area at sample position 10 mm x 50 mm (width x height)
       Q-range 0.002 - 2 A-1

       For more information, please visit
       https://www.ill.eu/instruments-support/instruments-groups/instruments/d17/characteristics/
       """
d17 = MantidGeom(instrumentName, comment=comment, valid_from=validFrom)
d17.addSnsDefaults()
d17.addComment("SOURCE")
d17.addComponentILL("chopper1", 0.0, 0.0, chop1_source, "Source")
d17.addComment("Sample position")
d17.addComponentILL("sample_position", 0.0, 0.0, 0.0, "SamplePos")
d17.addComment("MONITORS")
d17.addMonitors(names=["monitor1", "monitor2"], distance=[zMon1, zMon2])
d17.addComment("MONITOR SHAPE")
d17.addComment("FIXME: Do something real here.")
d17.addDummyMonitor(0.01, 0.03)
d17.addComment("MONITOR IDs")
d17.addMonitorIds(["0", "1"])
d17.addComment("DETECTORS")
d17.addComment("64 TUBES FORM ONE BANK")  # bank can be renamed to detector
d17.addComponentRectangularDetector("bank", 0.0, 0.0, detValue, idstart="2", idfillbyfirst="x",
                                    idstepbyrow="1")
d17.addComment("PIXEL, EACH PIXEL IS A DETECTOR")
d17.addRectangularDetector("bank", "pixel", xstart, xstep, xpixels, ystart, ystep, ypixels)
d17.addCuboidPixel("pixel", [-x, -y, z], [x, y, z], [-x, -y, thickness], [x, -y, z], shape_id="pixel-shape")
#d17.showGeom()
# write instrument definition to file
d17.writeGeom(xml_outfile)
