binaries = Main

all: bnfc lang bin

bin: 
	ghc --make Calc/Lang/TestCalc.hs -package ghc

bnfc: 
	bnfc -haskell -p Calc.Lang Calc.cf

lang:
	happy -gca Calc/Lang/ParCalc.y
	alex -g Calc/Lang/LexCalc.x
#	(cd NeoIDL/Lang/; latex -output-format=pdf DocNeoIDL.tex; dvips DocNeoIDL.dvi -o DocNeoIDL.ps)
	ghc --make Calc/Lang/TestCalc.hs -o Calc/Lang/TestCalc

clean:
	-rm -f *.log *.aux *.hi *.o *.dvi

distclean: clean
	-rm -f DocCalc.* LexCalc.* ParCalc.* LayoutCalc.* SkelCalc.* PrintCalc.* TestCalc.* AbsCalc.* TestCalc ErrM.* SharedString.* ComposOp.* Calc.dtd XMLCalc.* Makefile*
	

