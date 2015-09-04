#!/usr/bin/perl

use JSON;

$prices{"pizza"} = 12.00;
$prices{"coke"} = 1.25;
$prices{"sandwich"} = 3.00;

$size = keys %prices;

print "tamanho: ".$size."\n";

my %rec_hash = ('a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5);
my $json = encode_json \%rec_hash;

for $x (keys $json){
	print "\t$x\n";	
}

print "tamanho: $qtd\n";

    my $student = {
        name => 'Foo Bar',
        email => 'foo@bar.com',
        gender => undef,
        classes => [
            'Chemistry',
            'Math',
            'Literature',
        ],
        address => {
            city => 'Fooville',
            planet => 'Earth',
        },
    };

print "Students: ".keys %student->{'address'}."\n";
print "$json\n";
