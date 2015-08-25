#!/usr/bin/perl

use JSON;
 
binmode STDOUT, ":utf8";
use utf8;

use Data::Dumper;

$arquivo = $ARGV[0];
$modulo_pesquisa = $ARGV[1];
my $contrato = ( split '/', $arquivo )[ -2 ];

{
  local $/ = undef;
  open (FILE, $arquivo) or die "Couldn't open file: $!";
  binmode FILE;
  $json_file = <FILE>;
  close FILE;
}

$text = decode_json($json_file);


for $modelo (keys $text->{'models'}){

        if ($modulo_pesquisa eq $modelo){
		print "Contrato: ".$contrato."\n";
		for $atributo (keys $text->{'models'}->{$modelo}->{'properties'}){
			print "\t\t".$atributo;
			if (exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} and
			    exists $text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'required'} ){
				print "(*)";
			}
			print ": ".$text->{'models'}->{$modelo}->{'properties'}->{$atributo}->{'type'}."\n";
		}
	}
}
