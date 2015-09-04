#!/usr/bin/perl

use JSON;
 
binmode STDOUT, ":utf8";
use utf8;

use Data::Dumper;

$base_path = "data.json";
my $json;
if ( -e $base_path){
	{
	  local $/; #Enable 'slurp' mode
	  open my $fh, "<", $base_path;
	  $json = <$fh>;
	  close $fh;
	}
        $contador = decode_json($json);
    } else {
        %contador = ();
    }


for $modelo (keys $contador->{'models'}){
	print $modelo."|".$contador->{'models'}->{$modelo}->{'qtd'}."|\t";
	for $contrato (keys $contador->{'models'}->{$modelo}->{'contrato'}){
		print $contrato."(".$contador->{'models'}->{$modelo}->{'contrato'}->{$contrato}."); ";
	}
	print "\n";
}

