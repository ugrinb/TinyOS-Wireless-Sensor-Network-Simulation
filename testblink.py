#!/usr/bin/python
from TOSSIM import *
import sys

# Create a TOSSIM instance
t = Tossim([])
r = t.radio()

# Add a channel to see the debug output
# This matches the "BlinkC" component in the nesC code
t.addChannel("BlinkC", sys.stdout)

# Setup a single node (Mote) with ID 1
m = t.getNode(1)
m.bootAtTime(100) # Boot the node at time 100

print("Starting TinyOS Simulation...")

# Run simulation until the node turns on
while (m.isOn() == 0):
    t.runNextEvent()

# Run 100 events in the simulation
for i in range(0, 100):
    t.runNextEvent()

print("Simulation finished.")