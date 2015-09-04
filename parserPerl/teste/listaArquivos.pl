#!/usr/bin/perl

use JSON;
use Data::Dumper;
use utf8;
binmode STDOUT, ":utf8";


$diretorio = $ARGV[0];

opendir(diretorio, "$diretorio");
@lista = readdir(diretorio);
closedir(diretorio);

%matrizModelos = ();

foreach $arquivo(@lista)
{
  if ($arquivo ne "." and $arquivo ne ".."){
            	
	$contrato = &carregaContrato($diretorio."/".$arquivo."/synapse.json");
        
        for $modeloBase (keys $contrato->{'models'}){

          for $modeloReferencia (keys $contrato->{'models'}){
  
            $fatorSemelhanca = &compararModelos(
                                    $contrato->{'models'}->{$modeloBase},
                                    $contrato->{'models'}->{$modeloReferencia});
       
            if ($fatorSemelhanca > .5){
	      if (exists $matrizModelos->{$modeloBase}){
                $matrizModelos->{$modeloBase}->{'qtd'} += 1;
              } else {
                $matrizModelos->{$modeloBase}->{'qtd'}  = 0;
              }
            }
          }
          

#          if (exists $comparaModelos->{$modelo}){
#             $comparaModelos->{$modelo}->{'qtd'} += 1;
#          } else {
#             $comparaModelos->{$modelo}->{'qtd'}  = 1;
#          }

  #      if ($modulo_pesquisa eq $modelo){
  #              print "Contrato: ".$contrato."\n";
  #              for $atributo (keys $text->{'models'}->{$modelo}->{'properties'}){
  #                      print "\t\t".$atributo;
  #                      if (exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} and
  #                          exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} ){
  #                              print "(*)";
  #                      }
  #                      print ": ".$text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'type'}."\n";
  #              }
  #      }
       }

	
  #      print qq~$contrato->{id}~. "\n";
  }
}

foreach $ml (keys $matrizModelos){
    print qq~$ml~."\t".$matrizModelos->{$ml}->{'qtd'}."\n";
}


sub compararModelos {
  1;
}


sub carregaContrato {
  {
    local $/ = undef;
    open (FILE, $_[0]) or die "Couldn't open file: $!";
    binmode FILE;
    $json_file = <FILE>;
    close FILE;
  }

  decode_json($json_file);
}
