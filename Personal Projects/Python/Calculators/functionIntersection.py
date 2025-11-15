import math, aTools

class expression:
        def __init__(self, value:str):
                """
                Takes in an expression in the form ax^(n) bx^(n-1) ... cx + d
                """
                exa = "x^2 - x +1"
                value = exa

                repl = {" ": "","^": "**"}

                temp1 = [i for i in [repl[x] if x in repl else x for x in value]]
                temp2 = ""
                for i in temp1: temp2 += i
                self.equation = temp2


        def equate(self, Input:int|float|list[int|float], mode="s"):
                if not isinstance(Input,int|float) and not isinstance(Input,list):
                        Input = list(Input)
                if isinstance(Input,int|float):
                        x = Input
                        ans = eval(self.equation)
                elif isinstance(Input,list):
                        ans = []
                        for x in Input:
                                out = eval(self.equation)
                                ans.append(out)

                if mode == "v":
                        print(ans)
                return ans

test = expression("")
x = test.equate(7, "v")
