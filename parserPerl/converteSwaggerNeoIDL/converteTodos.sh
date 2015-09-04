#!/bin/bash

diretorioAtual=`pwd`
contratosSwagger="/home/lucas/workspace/mestrado/contratosExercito"
contratosNeoIDL="$diretorioAtual/out"
`rm $contratosNeoIDL/*`

cd $contratosSwagger;

ls -1 | while read contrato 
do
     echo -n "Convertendo $contrato . . .";
     `$diretorioAtual/swagger2NeoIDL.pl $contratosSwagger/$contrato/synapse.json > $diretorioAtual/out/$contrato.neo`;
     echo "ok";

done

