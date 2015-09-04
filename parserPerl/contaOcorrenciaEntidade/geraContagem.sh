#!/bin/bash

diretorioAtual=`pwd`
contratosSwagger="/home/lucas/workspace/mestrado/contratosExercito"

rm data.json;
cd $contratosSwagger;

ls -1 | while read contrato 
do
     cd $diretorioAtual
     `$diretorioAtual/contaEntidadeDuplicada.pl $contratosSwagger/$contrato/synapse.json`;

done

echo "Concluido";
