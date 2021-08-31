# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:00:53 2021

@author: alexa
"""


#!/home/sree/Python-2.7.18/activate/bin/python
from __future__ import print_function, division
import sys
sys.path.append('/scr/sree/FUN3D/EPYC/Python_GCC_9.3/lib/python2.7/site-packages')
import numpy as np
from mpi4py import MPI
from fun3d.solvers import Flow
from fun3d import interface

def get_total_pressure_ratio(step):
    """
    step changes till we get to target
    """
    pressure_ratio = 2.5
    if (step >= 1000): pressure_ratio = 5.0
    if (step >= 2000): pressure_ratio = 7.5
    if (step >= 3000): pressure_ratio = 8.845928
    if (step >= 4000): pressure_ratio = 12.5
    if (step >= 5000): pressure_ratio = 15.0
    if (step >= 6000): pressure_ratio = 17.5
    if (step >= 7000): pressure_ratio = 20.0
    if (step >= 8000): pressure_ratio = 22.5
    if (step >= 9000): pressure_ratio = 25.0
    if (step >= 10000): pressure_ratio = 30.0
    if (step >= 11000): pressure_ratio = 35.0
    if (step >= 12000): pressure_ratio = 45.0
    if (step >= 13000): pressure_ratio = 50.0
    if (step >= 14000): pressure_ratio = 55.0
    if (step >= 15000): pressure_ratio = 60.0
    if (step >= 16000): pressure_ratio = 65.0
    if (step >= 17000): pressure_ratio = 70.0
    if (step >= 18000): pressure_ratio = 75.0
    if (step >= 19000): pressure_ratio = 80.0
    if (step >= 20000): pressure_ratio = 85.0
    return pressure_ratio

def get_total_temperature_ratio(step):
    """
    sinusoidal variation
    """
    temperature_ratio = 1.5034722222222222222222222222222

    return temperature_ratio

if __name__ == '__main__':
    # Demo script options
    prior_steps = 0000                 # if restarting set to number of steps in the restart file
    nsteps = 20000                   # match value set in fun3d.nml

    #===========================================================================
    # Initialize the fun3d flow solver - read namelist, partion mesh, etc.
    #===========================================================================
    comm = MPI.COMM_WORLD

    flow = Flow()

    flow.initialize_project(comm=comm)

    # limited support for options typically read from command line. See list at top of Python/flow/interface.py
    command_line_options = {}
    flow.setOptions(kwargs=command_line_options)

    flow.initialize_data()
    flow.initialize_grid()
    flow.initialize_solution()

    #===========================================================================
    # Time step loop
    #===========================================================================
    for step in range(prior_steps+1,prior_steps+1+nsteps):

        # update the pressure and temperature ratio
        ibc = 1 # corresponds to BC 7011 in the mapbc file
        pressure_ratio = get_total_pressure_ratio(step)
        interface.bc_input_total_pressure_ratio(ibc,pressure_ratio)

        temperature_ratio = get_total_temperature_ratio(step)
        interface.bc_input_total_temperature_ratio(ibc,temperature_ratio)

        # take a step of fun3d
        flow.iterate()

    #===========================================================================
    # Finish the fun3d analysis. Write restart files, hist files, etc
    #===========================================================================
