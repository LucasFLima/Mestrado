#!/bin/bash

contratosSwagger="/home/lucas/workspace/mestrado/contratosExercito"
contratosNeoIDL="/home/lucas/workspace/mestrado/parserPerl/converteSwaggerNeoIDL/out"

cd $contratosSwagger;

qtdSwagger=0;
qtdNeo=0;

ls -1 | while read contrato 
do
     qtdLinhaSwagger=`egrep '[a-zA-Z]' $contrato/synapse.json | wc -l`;
     qtdSwagger=$(($qtdSwagger+$qtdLinhaSwagger));

     qtdLinhaNeoIDL=`egrep '[a-zA-Z]' $contratosNeoIDL/$contrato.neo | wc -l`;
     qtdNeo=$(($qtdNeo+$qtdLinhaNeoIDL));

#     echo $contrato         $qtdLinhaSwagger $qtdLinhaNeoIDL $totalLinhaSwagger $(($qtdLinhaNeoIDL*100/$qtdLinhaSwagger))\% $qtdSwagger $qtdNeo $(($qtdNeo*100/$qtdSwagger))\%;
     echo $contrato \&  $qtdLinhaSwagger \&  $qtdLinhaNeoIDL \&  $(($qtdLinhaNeoIDL*100/$qtdLinhaSwagger))\% \\\\;

done

