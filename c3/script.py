from turingEnds import TuringMachine

tm = TuringMachine.parse('c3/test.tm')
print(tm.accepts('{a,b,{c},d,{{{e}}}}'))