#!/bin/bash

utilPath="/home/lucas/workspace/mestrado/util/commands"

out=`cat $utilPath/parametros | grep "out_dir:" | cut -d":" -f2`
neo_dir=`cat $utilPath/parametros | grep "neo_dir:" | cut -d":" -f2`
module=`cat $utilPath/parametros | grep "module:" | cut -d":" -f2`
target=`cat $utilPath/parametros | grep "target:" | cut -d":" -f2`

echo "- - - - - - - - - - - - - - - - -"
echo "Modulo: "$module
echo "Saida:  "$out
echo "Target: "$target
echo "- - - - - - - - - - - - - - - - -"

curr_dir=`pwd`
cd $neo_dir/src
./Main -i../samples/$module -o$out --target=$target
cd $curr_dir

