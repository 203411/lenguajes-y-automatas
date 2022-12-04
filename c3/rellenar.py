

if __name__ == "__main__":
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
    with open("c3/transiciones.txt", "w") as f:
        
        for i in alfabeto:
            f.write("q1 "+i+".#.# q2 a.R #.S #.S"
                    +"\n"+ "q1 "+i+".#.# q2 a.R #.S #.S"
                    +"\n"+ "q4 "+i+".1.# q5 a.R 1.S #.S" 
                    +"\n"+"q6 "+i+".2.# q7 a.R 2.S #.S"
                    +"\n"+"q8 "+i+".3.# q9 a.R 3.S #.S"
                    +"\n"+ "q10 "+i+".4.# q11 a.R 4.S #.S"
                    +"\n"+"q12 "+i+".5.# q13 a.R 5.S #.S"
                    +"\n"+"q14 "+i+".6.# q15 a.R 6.S #.S"
                    +"\n")
            

"""
q1 a.#.# q2 a.R #.S #.S
q4 a.1.# q5 a.R 1.S #.S
q6 a.2.# q7 a.R 2.S #.S
q8 a.3.# q9 a.R 3.S #.S
q10 a.4.# q11 a.R 4.S #.S
q12 a.5.# q13 a.R 5.S #.S
q14 a.6.# q15 a.R 6.S #.S
"""	