# This script runs by first setting the attributes of a pulsar as it's variables to be used later
# Then, based on variables being input from our GUI will edit the common file and the file corresponding
# to the type of star the user selects on the GUI
# Finally, This script will call the rsp program using the Unix command line
# Created by the Radiation Hydrodynamic Pulsar enthusiasts
import os


class Pulsar:
    # Sets the parameters for a pulsar object
    def __init__(self, m, lum, x, z, crr, maxA, maxP, temp):
        self.mass = m
        self.luminosity = lum
        self.xComp = x
        self.zComp = z
        self.cOrRR = crr
        self.maxAmp = maxA
        self.maxPeriodNum = maxP
        self.temperature = temp


# Variables are to be updated by the GUI. This will automatically update the pulsar1 object variables
# along with the chosen file when the script is run.

# Andrew, this is the area you're concerned with
mass = 42.5678
lum = 251.3214
x = 45.2345
z = 42.3456
corr = "RR"
maxA = 45.4321
maxP = 46.8765
temp = 47.9012

# Pulsar object
pulsar1 = Pulsar(mass, lum, x, z, corr, maxA, maxP, temp)

# edit common file
filePath = "inlist_rsp_common"  # File path for Common File here
ogFilePath = "commonFormat.txt"  # Duplicate file path for Common File here
commonFile = open(filePath, "w")
ogCommon = open(ogFilePath, "r")

# Takes input from duplicate file and scans it, then writes it to the file we are editing.
# If we don't do this, then everything leading up to our variables is deleted
for ln in range(0, 41):
    commonScan = ogCommon.readline()
    commonFile.write("%s" % commonScan)
ogCommon.readline()
# This statement processes the equivalent line in ogCommon file to the line we are editing in
# working common file edit our variables in the common file file
commonFile.write("         RSP_mass = %f ! (Msun)\n" % pulsar1.mass)
ogCommon.readline()
commonFile.write("         RSP_Teff = %f ! (K)\n" % pulsar1.temperature)
ogCommon.readline()
commonFile.write("         RSP_L = %f ! (Lsun)\n" % pulsar1.luminosity)
ogCommon.readline()
commonFile.write("         RSP_X = %f ! hydrogen mass fraction\n" % pulsar1.xComp)
ogCommon.readline()
commonFile.write("         RSP_Z = %f ! metals mass fraction\n" % pulsar1.zComp)

# Find end of file so I can scan from the original file and write it to the file we are editing
# If we don't do this it will delete everything after our variables
scanned = ogCommon.readline()
while scanned != "":
    commonFile.write("%s" % scanned)
    scanned = ogCommon.readline()

# close files
commonFile.close()
ogCommon.close()


# check which file is used and edit


# if file selected is RR:
if pulsar1.cOrRR == "RR":
    filePath = "inlist_rsp_RR_Lyrae"  # File path for cepheid here
    ogFilePath = "RRLyraeFormat.txt"  # Duplicate file path for Cepheid here
    file = open(filePath, "w")
    ogFile = open(ogFilePath, "r")

    # Takes input from duplicate file and scans it, then writes it to the file we are editing.
    # If we don't do this, then everything leading up to our variables is deleted
    for line in range(0, 23):
        scanned = ogFile.readline()
        file.write("%s" % scanned)
    ogFile.readline()
    # edit the variables in our RR_Leary file
    file.write("   RSP_mass = %fd0\n" % pulsar1.mass)
    ogFile.readline()  # This statement processes the equivalent line in ogFile to the line we are editing in file
    file.write("   RSP_Teff = %f\n" % pulsar1.temperature)
    ogFile.readline()
    file.write("   RSP_L = %fd0\n" % pulsar1.luminosity)
    ogFile.readline()
    file.write("   RSP_X = %fd0\n" % pulsar1.xComp)
    ogFile.readline()
    file.write("   RSP_Z = %fd0\n" % pulsar1.zComp)

    # Find end of file so I can scan from the original file and write it to the file we are editing
    # If we don't do this it will delete everything after our variables
    scanned = ogFile.readline()
    while scanned != "":
        file.write("%s" % scanned)
        scanned = ogFile.readline()

    # close files
    file.close()
    ogFile.close()


# If file selected is Cepheid
elif pulsar1.cOrRR == "C":
    filePath = "inlist_rsp_Cepheid"  # File path for cepheid here
    ogFilePath = "cepheidFormat.txt"  # Duplicate file path for Cepheid here
    file = open(filePath, "w")
    ogFile = open(ogFilePath, "r")

    # Takes input from duplicate file and scans it, then writes it to the file we are editing.
    # If we don't do this, then everything leading up to our variables is deleted
    for line in range(0, 29):
        scanned = ogFile.readline()
        file.write("%s" % scanned)
    ogFile.readline()  # This statement processes the equivalent line in ogFile to the line we are editing in file
    # edit the our variables in the Cepheid files
    file.write("   RSP_mass = %fd0\n" % pulsar1.mass)
    ogFile.readline()  # This statement processes the equivalent line in ogFile to the line we are editing in file
    file.write("   RSP_Teff = %f\n" % pulsar1.temperature)
    ogFile.readline()
    file.write("   RSP_L = %fd0\n" % pulsar1.luminosity)
    ogFile.readline()
    file.write("   RSP_X = %fd0\n" % pulsar1.xComp)
    ogFile.readline()
    file.write("   RSP_Z = %fd0\n" % pulsar1.zComp)

    # Find end of duplicate file so I can scan from the original file and write it to the file we are
    # editing If we don't do this it will delete everything after our variables
    scanned = ogFile.readline()
    while scanned != "":
        file.write("%s" % scanned)
        scanned = ogFile.readline()
    # Close files
    file.close()
    ogFile.close()


