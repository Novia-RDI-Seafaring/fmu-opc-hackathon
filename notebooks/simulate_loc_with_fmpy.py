# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:01:21 2024

@author: emrkay
"""

""" 


"""

from matplotlib import pyplot as plt
%matplotlib qt
from fmpy import read_model_description, extract

from fmpy.fmi2 import FMU2Slave


import numpy as np

import shutil




#def simulate_custom_input(show_plot=True):


    # define the model name and simulation parameters

fmu_filename = '../fmus/loc/LOC_FMI2.fmu'
input_csv = "../fmus/loc/LOC_in.csv"
start_time = 0.0


stop_time = 1000.0
step_size = 1

nsteps = int((stop_time-start_time)//step_size)
# read the model description

model_description = read_model_description(fmu_filename)

print(model_description)

# collect the value references

vrs = {}

for variable in model_description.modelVariables:

    vrs[variable.name] = variable.valueReference

    print(variable.name + ':' +str(variable.valueReference))

# get the value references for the variables we want to get/set

#############################################
vr_inputs   = []#vrs['inputs']      # normalized force on the 3rd clutch
#nsteps= 1000
with open(input_csv, "r") as f:
    raw_input = f.read()

raw_input2 = raw_input.split('\n')
inpkeys = raw_input2[0].replace('"','').split(',')
nrows = len(raw_input2)-2

inpdata = np.zeros((nrows,len(inpkeys)))
n_inputs = len(inpkeys)
for irow in range(nrows):
    for icol in range(n_inputs):
        inpdata[irow,icol] =  int(raw_input2[irow+1].split(',')[icol])


inpdict = {}
for i,inpkey in enumerate(inpkeys[1:]):
    inparr = np.zeros(nsteps)
    for irow in range(nrows-1):
        inparr[int(inpdata[irow,0]):int(inpdata[irow+1,0])]=inpdata[irow,i+1]
    inparr[int(inpdata[nrows-1,0]):]=inpdata[nrows-1,i+1]
    inpdict[inpkey] = inparr#inpdata[:,i]

#grdgdgr
#thfhfth
output_vars = []
for varname in list(vrs.keys()):
    if 'OUTPUT' in varname:
        output_vars.append(varname)

input_vars = inpkeys[1:]
#gdrgdgd

   
vr_inputs = []

for var in input_vars:

    vr_inputs.append(vrs[var])
    
#vr_outputs4 = vrs['outputs[4]']  # angular velocity of the 4th inertia

vr_outputs = []

for var in output_vars:

    vr_outputs.append(vrs[var])

n_outputs = len(output_vars)
# extract the FMU

unzipdir = extract(fmu_filename)


fmu = FMU2Slave(guid=model_description.guid,

                unzipDirectory=unzipdir,

                modelIdentifier=model_description.coSimulation.modelIdentifier,

                instanceName='instance1')



# initialize

fmu.instantiate()

fmu.setupExperiment(startTime=start_time)



# for iinpvar,input_var in enumerate(input_vars):
#     vr_inp = vr_inputs[iinpvar]
    
#     inp_value =  inpdict[input_var][0]
#     fmu.setReal([vr_inp,],[inp_value,])

fmu.enterInitializationMode()

fmu.exitInitializationMode()


time = start_time


#rows = []  # list to record the results

data = np.zeros((nsteps,n_outputs+1))

# simulation loop

itime = 0

while time < stop_time:


    # NOTE: the FMU.get*() and FMU.set*() functions take lists of

    # value references as arguments and return lists of values


    # set the input
    for iinpvar,input_var in enumerate(input_vars):
        vr_inp = vr_inputs[iinpvar]
        
        inp_value =  inpdict[input_var][itime]
        fmu.setReal([vr_inp,],[inp_value,])


    # perform one step

    fmu.doStep(currentCommunicationPoint=time, communicationStepSize=step_size)


    # advance the time

    time += step_size


    # get the values for 'inputs' and 'outputs[4]'

    outputs = fmu.getReal(vr_outputs)

    inputs = fmu.getReal(vr_inputs)

    # append the results

    #rows.append(outputs)

    data[itime,0] = time

    #for i in range(4):

    #    data[itime,i+1] = inputs[i]

    for i in range(n_outputs):

        data[itime,i+1] = outputs[i]

    itime=itime+1


fmu.terminate()

fmu.freeInstance()


# clean up

shutil.rmtree(unzipdir, ignore_errors=True)


# convert the results to a structured NumPy array

#result = np.array(rows, dtype=np.dtype([('time', np.float64), ('inputs', np.float64), ('outputs[4]', np.float64)]))

print(data[0:10,:])



fig,ax = plt.subplots()

for i_input in range(n_inputs-1):
    ax.plot(data[:,0],inpdict[input_vars[i_input]],'*',label=input_vars[i_input])

ax.legend()
ax.grid()
plt.xlabel('Time(s)')
plt.title("inputs")


# plot the results


fig,ax = plt.subplots()

for i_output in range(n_outputs):
    ax.plot(data[:,0],data[:,i_output+1],'*',label=output_vars[i_output])

ax.legend()
ax.grid()
plt.xlabel('Time(s)')

