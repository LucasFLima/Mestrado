#!/bin/bash

modulo=$1;
diretorioAtual=`pwd`
contratosSwagger="/home/lucas/workspace/mestrado/contratosExercito"

cd $contratosSwagger;

ls -1 | while read contrato 
do
     $diretorioAtual/detalhaModulo.pl $contratosSwagger/$contrato/synapse.json $modulo;

done

echo "Concluido";
