#!/bin/bash 
#
sbatch firefly.run.fun3d 

sed -i 's/restart_read = 'off'/restart_read = 'on'/'fun3d.nml   
sed -i 's/total_pressure_ratio(1) = 2.5/total_pressure_ratio(1) = 5/'fun3d.nml   
sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 5/total_pressure_ratio(1) = 7.5/'fun3d.nml   

sbatch firefly.run.fun3d
sed -i 's/total_pressure_ratio(1) = 7.5/total_pressure_ratio(1) = 10.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 10.0/total_pressure_ratio(1) = 12.5/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 12.5/total_pressure_ratio(1) = 15.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 15.0/total_pressure_ratio(1) = 20.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 20.0/total_pressure_ratio(1) = 25.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 25.0/total_pressure_ratio(1) = 30.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 30.0/total_pressure_ratio(1) = 40.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 40.0/total_pressure_ratio(1) = 50.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 50.0/total_pressure_ratio(1) = 60.0/'fun3d.nml   

sbatch fly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 60.0/total_pressure_ratio(1) = 70.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 70.0/total_pressure_ratio(1) = 80.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 80.0/total_pressure_ratio(1) = 90.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 90.0/total_pressure_ratio(1) = 100.0/'fun3d.nml   

sbatch firefly.run.fun3d

sed -i 's/total_pressure_ratio(1) = 100.0/total_pressure_ratio(1) = 110.0/'fun3d.nml   

sbatch  firefly.run.fun3d
