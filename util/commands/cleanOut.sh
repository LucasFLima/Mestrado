#!/bin/bash

utilPath="/home/lucas/workspace/utilLucasFLima"
out=`cat $utilPath/parametros | grep "out_dir:" | cut -d":" -f2`

find $out/* -maxdepth 1 -exec echo "Removing " {} \; -exec rm {} \;
echo $out" cleaned"
