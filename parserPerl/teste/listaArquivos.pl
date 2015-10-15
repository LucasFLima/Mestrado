#!/usr/bin/perl

use JSON;
use Data::Dumper;
use utf8;
binmode STDOUT, ":utf8";


$diretorio = $ARGV[0];

opendir(diretorio, "$diretorio");
@lista = readdir(diretorio);
closedir(diretorio);

%acumuladorModelos = ();

foreach $arquivo(@lista)
{
  if ($arquivo ne "." and $arquivo ne ".."){
            	
	$contrato = &carregaContrato($diretorio."/".$arquivo."/synapse.json");
        $nomeContrato = $arquivo;
    
        $acumuladorModelos->{'contrato'}->{$nomeContrato}->{'modelo'} = $contrato->{'models'};
 
  }
}

%avaliadorModelos = ();
foreach $ctrBase (keys $acumuladorModelos->{'contrato'}){

  foreach $mdlBase (keys $acumuladorModelos->{'contrato'}->{$ctrBase}->{'modelo'}){

    &avaliaModelo($ctrBase, $mdlBase, $acumuladorModelos->{'contrato'}->{$ctrBase}->{'modelo'}->{$mdlBase});

  }
}



foreach $estrutura (keys $avaliadorModelos->{'estruturas'}){
    $qi = scalar (keys $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_identico'});
    if (exists $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_semelhante'}){
      $qs = scalar (keys $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_semelhante'});
    } else {
      $qs = 0;
    }
    
    if ($qi > 1){
        print $estrutura."\n";
        foreach $contrato (keys $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_identico'}){
            print "\t".$contrato.".".$avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_identico'}->{$contrato}."\n";
        }
   #    foreach $prop (keys $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo'}->{'properties'}){
   #        print "\t\t".$prop."\n";
   #    }
    }
    #print $estrutura." - ".$qi." - ".$qs."\n";
}


 
sub avaliaModelo {
   $nmContrato = $_[0];
   $nmModelo   = $_[1];
   $Modelo     = $_[2];

   if (exists $avaliadorModelos->{'estruturas'}){
      $qtdEstrutura = keys %{$avaliadorModelos->{'estruturas'}};
      $qtdEstrutura += 1;
      print "Qtd: ". $qtdEstrutura. "\n";    
 
      foreach $estrutura (keys $avaliadorModelos->{'estruturas'}){
        
          my ($cpr, $sizeBase, $sizeComp) = &compararModelos(
                      $Modelo, 
                      $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo'});
         
          if ($cpr == 1 and $sizeBase == $sizeComp){
  #            print "igual: ".$qtdEstrutura."\n";
              $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_identico'}->{$nmContrato}=$nmModelo;
          } 
       #   elsif ($cpr >= .75){
       #      $avaliadorModelos->{'estruturas'}->{$estrutura}->{'modelo_semelhante'}->{$nmContrato}->{$nmModelo}=$cpr;
       #   }
          else {
   #          print "diferente: ".$qtdEstrutura."\n";
             $avaliadorModelos->{'estruturas'}->{'estrutura'.$qtdEstrutura}->{'modelo'}=$Modelo;
             $avaliadorModelos->{'estruturas'}->{'estrutura'.$qtdEstrutura}->{'modelo_identico'}->{$nmContrato}=$nmModelo;
          
          }

      }


   } else {
      $avaliadorModelos->{'estruturas'}->{'estrutura1'}->{'modelo'}=$Modelo;
      $avaliadorModelos->{'estruturas'}->{'estrutura1'}->{'modelo_identico'}->{$nmContrato}=$nmModelo;
   }

   

} 

# foreach $ctrBase (keys $acumuladorModelos->{'contrato'}){
#     
#     foreach $ctrCompara (keys $acumuladorModelos->{'contrato'}){
# 
#         foreach $mdlBase (keys $acumuladorModelos->{'contrato'}->{$ctrBase}->{'modelo'}){
#                
#             foreach $mdlCompara (keys $acumuladorModelos->{'contrato'}->{$ctrCompara}->{'modelo'}){
#                     
#                 if ($ctrCompara ne $ctrBase or $mdlBase ne $mdlCompara){
# 
#                     my ($cpr, $sizeBase, $sizeComp) = &compararModelos(
#                                   $acumuladorModelos->{'contrato'}->{$ctrBase}->{'modelo'}->{$mdlBase},
#                                   $acumuladorModelos->{'contrato'}->{$ctrCompara}->{'modelo'}->{$mdlCompara});
#                       
#                     if ($cpr == 1 and $sizeBase == $sizeComp and $sizeBase > 1 and $mdlBase ne $mdlCompara){
#                        print $ctrBase." - ".$mdlBase."(".$sizeBase.")".
#                              "\t/\t".
#                              $ctrCompara." - ".$mdlCompara."(".$sizeComp.")"." - ".$cpr."\n";
#                     }
#                  }
#              }
#          }
#      }
#     
# }         
  
sub compararModelos {
    $modelo1=$_[0];
    $modelo2=$_[1];

    $i = keys %{$modelo1->{'properties'}};
    $j = keys %{$modelo2->{'properties'}};
    $t = 0;

    foreach $atbM1 (keys $modelo1->{'properties'}){
       if (exists $modelo2->{'properties'}->{$atbM1}) {
           $t += 1;
           # print "\t\t".$atbM1."\n";
       }
    }

    return ($t / $i, $i, $j);
}


sub carregaContrato {
  
    local $/ = undef;
    open (FILE, $_[0]) or die "Couldn't open file: $!";
    binmode FILE;
    $json_file = <FILE>;
    close FILE;
    
    decode_json($json_file);
}
