'''
Created on 20/01/2017

@author: vardanyan@ill.fr

Run as:

cd mantidgeometry/ILL/IDF; python d4_generateIDF.py | tidy -utf8 -xml -w 255 -i -c -q -asxml > D4C_Definition.xml

'''

import time

instrumentName = 'D4C_hr'
#nCellsPerPlate = 64 # D4C
nCellsPerPlate = 128 # D4C_hr
#cellWidth = 0.0025 # D4C
cellWidth = 0.00125 # D4C_hr

nPlates = 9
radius = 1.146
cellHeight = 0.1
cellDepth = 0.03
starting2Theta = 5.5
panel2Theta = 8
gap2Theta = 7
L1 = 2.61
monitorZ = 0.71
monitorSize = 0.01

def printHeader():

    print """<?xml version="1.0" encoding="UTF-8"?>
    <!-- For help on the notation used to specify an
    Instrument Definition File see http://www.mantidproject.org/IDF
    -->
    <instrument xmlns="http://www.mantidproject.org/IDF/1.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.mantidproject.org/IDF/1.0
    Schema/IDFSchema.xsd"
    name="{0}" valid-from="1900-01-31 23:59:59"
    valid-to="2100-01-31 23:59:59" last-modified="{1}">"""\
        .format(instrumentName,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

    print """<!-- Author: vardanyan@ill.fr -->"""

    print """<defaults>
      <length unit="meter" />
      <angle unit="degree" />
      <reference-frame>
        <!-- The z-axis is set parallel to and in the direction of the beam.
        the y-axis points up and the coordinate system is right handed. -->
        <along-beam axis="z" />
        <pointing-up axis="y" />
        <handedness val="right" />
        <theta-sign axis="x" />
      </reference-frame>
    </defaults>
    """

    print """<!-- Source position -->
    <component type="monochromator">
        <location z="-{0}" />
    </component>
    <type name="monochromator" is="Source">
      <properties />
    </type>""".format(L1)

    print """<!-- Monitor position -->
    <component type="monitor" idlist="monitors">
        <location z="-{0}" name="monitor" />
    </component>

    <type name="monitor" is="monitor">
      <cuboid id="shape">
        <left-front-bottom-point  x="-{1}"  y="-{1}" z="-{1}"   />
        <left-front-top-point     x="-{1}"  y="{1}" z="-{1}" />
        <left-back-bottom-point   x="-{1}" y="-{1}" z="{1}"   />
        <right-front-bottom-point x="{1}"  y="-{1}"  z="-{1}"   />
      </cuboid>
      <algebra val="shape" />
    </type>
    <idlist idname="monitors">
        <id val="0" />
    </idlist>
    """.format(monitorZ, monitorSize / 2.)

    print """<!-- Sample position -->
    <component type="sample-position">
      <location y="0.0" x="0.0" z="0.0" />
    </component>
    <type name="sample-position" is="SamplePos" />
    """


def printDetector():
    print """<!-- Detector IDs -->
    <idlist idname="detectors">
        <id start="1" end="{0}" />
    </idlist>
    <!-- Detector list def -->
    <component type="detector" idlist="detectors">
        <location name="detector"/>
    </component>
    <!-- Detector Panels -->
    <type name="detector">
      <component type="panel">""".format(nCellsPerPlate * nPlates)

    for panel in range(nPlates):
        print """       <location name="panel_{0}" r="{1}" t="{2}" p="0.0">
                    <facing r="0.0" t="0.0" p="0.0"/>
                </location>
        """.format(panel+1, radius,
                   starting2Theta + panel * (panel2Theta + gap2Theta))

    print """   </component>
    </type>
    """


def printPanelType():
    print """<!-- Standard Panel -->
    <type name="panel">
        <component type="cell">
    """

    for cell in range(nCellsPerPlate):
        print """       <location name="cell_{0}" x="{1}" />
        """.format(cell+1, (cell - nCellsPerPlate / 2 + 0.5) * cellWidth)

    print """   </component>
    </type>
    """


def printCellType():
    print """<!-- Standard Cell -->
    <type is="detector" name="cell">
        <cuboid id="cell-shape">"""
    print """   <left-front-bottom-point x="{0}" y="{1}" z="{2}"/>"""\
        .format(-cellWidth/2., -cellHeight/2., -cellDepth/2.)

    print """   <left-front-top-point x="{0}" y="{1}" z="{2}"/>"""\
        .format(-cellWidth/2., cellHeight/2., -cellDepth/2.)

    print """   <left-back-bottom-point x="{0}" y="{1}" z="{2}"/>"""\
        .format(-cellWidth/2., -cellHeight/2., cellDepth/2.)

    print """   <right-front-bottom-point x="{0}" y="{1}" z="{2}"/>"""\
        .format(cellWidth/2., -cellHeight/2., -cellDepth/2.)
    print """   </cuboid>
      <algebra val="cell-shape"/>
    </type>
    """


def printEnd():
    print "</instrument>"


if __name__ == '__main__':
    printHeader()
    printDetector()
    printPanelType()
    printCellType()
    printEnd()
