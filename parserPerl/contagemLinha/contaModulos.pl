#!/usr/bin/perl

use JSON;
 
binmode STDOUT, ":utf8";
use utf8;

use Data::Dumper;

if ($ARGV[0] eq "help"){
  print "Ordem dos campos:\n\tModulos, Servicos, Capacidades\n";
  exit;
}

$arquivo = $ARGV[0];
$separador = $ARGV[1];
my $contrato = ( split '/', $arquivo )[ -2 ];

{
  local $/ = undef;
  open (FILE, $arquivo) or die "Couldn't open file: $!";
  binmode FILE;
  $json_file = <FILE>;
  close FILE;
}

$text = decode_json($json_file);

$qtdModulos = keys %{$text->{models}};

$qtdAtributos = 0;
$qtdServicos = 0;
$qtdCapacidades = 0;
$qtdParametros = 0;

foreach $modelo (keys $text->{'models'}){
  $qtdAtributos += %{$text->{'models'}->{$modelo}->{'properties'}};
}

foreach $service (@{$text->{'apis'}}){
   $qtdServicos += 1;
   foreach $capacidade (@{$service->{'operations'}}){
      $qtdCapacidades += 1;
      foreach $atributos (@{$capacidade->{'parameters'}}){
         $qtdParametros += 1;
      }
   }
}

print $qtdModulos.    $separador.
#      $qtdAtributos.  $separador.
      $qtdServicos.   $separador.
      $qtdCapacidades.
#      $separador.$qtdParametros.
      "\n";


#for $modelo (keys $text->{'models'}){
#
#        if ($modulo_pesquisa eq $modelo){
#		print "Contrato: ".$contrato."\n";
#		for $atributo (keys $text->{'models'}->{$modelo}->{'properties'}){
#			print "\t\t".$atributo;
#			if (exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} and
#			    exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} ){
#				print "(*)";
#			}
#			print ": ".$text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'type'}."\n";
#		}
#	}
#}
