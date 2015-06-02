#!/bin/bash

out=`cat parametros | grep "out_dir:" | cut -d":" -f2`
neo_dir=`cat parametros | grep "neo_dir:" | cut -d":" -f2`
module=`cat parametros | grep "module:" | cut -d":" -f2`
target=`cat parametros | grep "target:" | cut -d":" -f2`

echo "- - - - - - - - - - - - - - - - -"
echo "Modulo: "$module
echo "Saida:  "$out
echo "Target: "$target
echo "- - - - - - - - - - - - - - - - -"

curr_dir=`pwd`
cd $neo_dir/src
./Main -i../samples/$module -o$out --target=$target
cd $curr_dir

