#!/bin/bash

diretorioAtual=`pwd`
contratosSwagger="/home/lucas/workspace/mestrado/contratosExercito"

cd $contratosSwagger;

ls -1 | while read contrato 
do
     $diretorioAtual/modulosRelacionados.pl $contratosSwagger/$contrato/synapse.json;

done
