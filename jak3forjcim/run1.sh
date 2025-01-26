#!/bin/bash
export CUDA_VISIBLE_DEVICES=0


for i in 1 2 3 
do
  mkdir gamd$i
  cd gamd$i 
  pmemd.cuda -O -i ../md.in -p ../comp_wat.prmtop -c ../05-cmd.rst -o md$i.out -r md$i.rst -x md$i.nc -gamd md$i.log
  pmemd.cuda -O -i ../gamd-restart.in -p ../comp_wat.prmtop -c md$i.rst -o gamd$i.out -x gmd$i.nc -r gamd$i.rst -gamd gamd$i.log
  cd ../
done
