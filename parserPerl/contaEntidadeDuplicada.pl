#!/usr/bin/perl

use JSON;
 
binmode STDOUT, ":utf8";
use utf8;

use Data::Dumper;

$arquivo = $ARGV[0];
my $contrato = ( split '/', $arquivo )[ -2 ];

{
  local $/ = undef;
  open (FILE, $arquivo) or die "Couldn't open file: $!";
  binmode FILE;
  $json_file = <FILE>;
  close FILE;
}

$text = decode_json($json_file);

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


for $modelo (keys $text->{'models'}){
	if (exists $contador->{'models'}->{$modelo}){
		#atualizar quantidade
		$contador->{'models'}->{$modelo}->{'qtd'}  += 1;
	} else {
		$contador->{'models'}->{$modelo}->{'qtd'}   = 1;
	}
	$contador->{'models'}->{$modelo}->{'contrato'}->{$contrato} = "ok";
}

open my $fh, ">", $base_path;
print $fh encode_json($contador);
close $fh;
