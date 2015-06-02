#!/bin/bash

out=`cat parametros | grep "out_dir:" | cut -d":" -f2`

rm  $out/*
echo $out" cleaned"
