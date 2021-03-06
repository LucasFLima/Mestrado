#!/usr/bin/perl

use JSON;

use Data::Dumper;

$arquivo = $ARGV[0];
my $model_name = ( split '/', $arquivo )[ -2 ];

{
  local $/ = undef;
  open (FILE, $arquivo) or die "Couldn't open file: $!";
  binmode FILE;
  $json_file = <FILE>;
  close FILE;
}

$text = decode_json($json_file);
#$dumped = Dumper($text);

# cabeçalho
print "module ".lc($model_name)." {\n";
#TODO: Path do modulo não disponível no swagger
print "\n\tpath = \"xxx\";\n\n";

#print "\t/*Linhas de geração das entidades comentadas*/\n\n";
for $models (keys $text->{'models'}){
	print "\tentity ".$models." {\n";

	if (exists $text->{'models'}->{$models}->{'properties'}){
		$lista_models = $text->{'models'}->{$models}->{'properties'};
	} else {
		$lista_models = $text->{'models'}->{$models};
	}
	for $nome_propriedade (keys $lista_models){
	
	        if (exists $lista_models->{$nome_propriedade}){
			$atributos_propriedade = $lista_models->{$nome_propriedade};		
		} else {
			$atributos_propriedade = $lista_models->{'data'}[0]->{$nome_propriedade};
		}
	
		#tratamento para o caso de o campo ser array
		if (exists $atributos_propriedade->{'type'}){
			if ($atributos_propriedade->{'type'} eq "array"){
				if (exists $atributos_propriedade->{'items'}->{'$ref'}){
					print "\t\t[".$atributos_propriedade->{'items'}->{'$ref'}."] : ".
		       		       $nome_propriedade.";";
				} else {
				       print "\t\t[".$atributos_propriedade->{'items'}->{'type'}."] : ".
		       		       $nome_propriedade.";";
				}
			} else
			{
				print "\t\t".$atributos_propriedade->{'type'}." : ".
        	                      $nome_propriedade.";";
			}
		} else #não possui atributo de tipo definido
		{
			print "\t\t".$atributos_propriedade." : ".$nome_propriedade.";";
		}
		#verificar se o dado é obrigatório
		$comentario = "";
		if ($atributos_propriedade->{'required'} != "false") {
			$comentario = "Required.";
		}

		if (exists $atributos_propriedade->{'allowableValues'}){
			$comentario .= " Valores possiveis: ";
			foreach $valores (@{$atributos_propriedade->{'allowableValues'}->{'values'}}){
				$comentario .= $valores." ";	
			}
		}

		#TODO: Descricao dos campos.
		if (length($comentario) > 0){
			print "   /*".$comentario."*/";
		};
		print "\n";
	}
	print "\t};\n\n";
}
#=cut

#print "\t/*Linhas de geração dos servicos comentados*/\n\n";
#imprime a lista de servicos
foreach $service (@{$text->{'apis'}}){
	#TODO: Nome do servico nao disponível no swagger
	print "\tservice <NomeServico> {\n";
	print "\t\tpath = \"".$service->{'path'}."\";\n";
     	
	foreach $capacidades (@{$service->{'operations'}}){
		$capacidade_pp = "\t\t\@".lc($capacidades->{'method'}).
		                   " ".$capacidades->{'type'}.
		                   #TODO: Nome da capacidade não disponível
		                   " "."<NomeCapacidade>".
                                   " (";
		$capacidade_doc_pp = "\n\t\t/**\n";
		$capacidade_doc_pp .= "\t\t* \@ summary: ".$capacidades->{'summary'}."\n";
		$capacidade_doc_pp .= "\t\t* \@ params: \n";
                $parametro_e_tipo = "";

		foreach $parametros (@{$capacidades->{'parameters'}}){
			$parametro_e_tipo .= $parametros->{'type'}." ".$parametros->{'name'}.", ";
			$capacidade_doc_pp .= "\t\t\*\t".$parametros->{'paramType'}." ".$parametros->{'name'};
			if ($parametros->{'required'}) {
                	       $capacidade_doc_pp .= "(*)";
                        }
			$capacidade_doc_pp .= ": ".$parametros->{'description'}."\n";
			if (exists $parametros->{'enum'}){
				$capacidade_doc_pp .= "\t\t\*\t\t\\--> Valores possiveis: ";
				#TODO: Verificar se os parametros com enumeracao sao pre-condicoes
				foreach $enum (@{$parametros->{'enum'}}){
					$capacidade_doc_pp .= $enum." ";
				}
				$capacidade_doc_pp .= "\n";
			}
		 }
		 $capacidade_pp .= substr($parametro_e_tipo, 0, length ($parametro_e_tipo) - 2);
		 $capacidade_pp .= ");\n";
		
	         if (exists $capacidades->{'responseMessages'}) {
		 	$capacidade_doc_pp .= "\t\t* \@ responseCodes: \n";
		 	foreach $respostas (@{$capacidades->{'responseMessages'}}){
		 		$capacidade_doc_pp .= "\t\t*\t".$respostas->{'code'}.
                                                      ": ".$respostas->{'message'};
                                if (exists $respostas->{'responseModel'}){
					$capacidade_doc_pp .= " --Response Model: ".$respostas->{'responseModel'};
				}
                                $capacidade_doc_pp .= "\n";
			}
		 }

		 $capacidade_doc_pp .= "\t\t*/\n";     
		
		 print $capacidade_doc_pp;
		 print $capacidade_pp;
	}

	print "\t}\n\n";
	
}
#=cut

print "\n";
