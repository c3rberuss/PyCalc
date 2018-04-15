class Acciones():


    def add_n0(self):
        self.txtOperando.insert("0")
    
    def add_n1(self):
        self.txtOperando.insert("1")

    def add_n2(self):
        self.txtOperando.insert("2")

    def add_n3(self):
        self.txtOperando.insert("3")

    def add_n4(self):
        self.txtOperando.insert("4")

    def add_n5(self):
        self.txtOperando.insert("5")
    
    def add_n6(self):
        self.txtOperando.insert("6")

    def add_n7(self):
        self.txtOperando.insert("7")

    def add_n8(self):
        self.txtOperando.insert("8")

    def add_n9(self):
        self.txtOperando.insert("9")

    
    def add_raiz(self):
        
        self.txtOperando.insert("sqrt(  )")
  
    def add_potencia(self):
        self.txtOperando.insert("Pow(  )")
       
    def add_notacion(self):
        self.txtOperando.insert("1e")

    def add_modulo(self):
        self.txtOperando.insert(" mod ")

    def add_simplificar(self):
        self.txtOperando.insert("simplify(  )")
    
    def add_cos(self):
        self.txtOperando.insert("cos(  )")
    
    def add_atan(self):
        self.txtOperando.insert("atan(  )")

    def add_abs(self):
        self.txtOperando.insert("abs(  )")

    def add_entre(self):
        self.txtOperando.insert(" / ")

    def add_factorizar(self):
        self.txtOperando.insert("factor(  )")

    
    def add_sin(self):
        self.txtOperando.insert("sin(  )")
    
    def add_cosh(self):
        self.txtOperando.insert("cosh(  )")
       
    def add_ln(self):
        self.txtOperando.insert("ln(  )")

    def add_por(self):
        self.txtOperando.insert(" * ")

    def add_exp(self):
        self.txtOperando.insert("exp(  )")
    
    def add_tan(self):
        self.txtOperando.insert("tan(  )")
    
    def add_sinh(self):
        self.txtOperando.insert("sinh(  )")

    def add_log(self):
        self.txtOperando.insert("log(  )")

    def add_menos(self):
        self.txtOperando.insert(" - ")

    def add_pi(self):
        self.txtOperando.insert(" pi ")

    def add_acos(self):
        self.txtOperando.insert("acos(  )")
    
    def add_tanh(self):
        self.txtOperando.insert("tanh(  )")

    def add_derivada(self):
        self.txtOperando.insert("derivate(  )")

    def add_punto(self):
        self.txtOperando.insert(".")

    def add_parentesis(self):
        self.txtOperando.insert("(  )")

    
    def add_mas(self):
        self.txtOperando.insert(" + ")

    def add_asin(self):
        self.txtOperando.insert("asin(  )")

    def add_factorial(self):
        self.txtOperando.insert("factorial(  )")

    def add_integral(self):
        self.txtOperando.insert("integrate(  )")


    """def add_n0(self):
        self.txtOperando.insert("0")
    
    def add_n1(self):
        self.txtOperando.insert("1")

    def add_n2(self):
        self.txtOperando.insert("2")

    def add_n3(self):
        self.txtOperando.insert("3")

    def add_n4(self):
        self.txtOperando.insert("4")

    def add_n5(self):
        self.txtOperando.insert("5")
    
    def add_n6(self):
        self.txtOperando.insert("6")

    def add_n7(self):
        self.txtOperando.insert("7")

    def add_n8(self):
        self.txtOperando.insert("8")

    def add_n9(self):
        self.txtOperando.insert("9")

    
    def add_raiz(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            print(eq.selectedText())
            print(eq.selectedText())
            eq.insert("sqrt(  )")
        else:
            print("no se seleccionó nada")
            eq.insert("sqrt( "+eq.selectedText()+" )")
    
    def add_potencia(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("Pow(  )")
        else:
            eq.insert("Pow( "+eq.selectedText()+" )")

    def add_notacion(self):
        self.txtOperando.insert("1e")

    def add_modulo(self):
        self.txtOperando.insert(" mod ")

    def add_simplificar(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("simplify(  )")
        else:
            eq.insert("simplify( "+eq.selectedText()+" )")
    
    def add_cos(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("cos(  )")
        else:
            eq.insert("cos( "+eq.selectedText()+" )")    
    
    def add_atan(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("atan(  )")
        else:
            eq.insert("atan( "+eq.selectedText()+" )")

    def add_abs(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("abs(  )")
        else:
            eq.insert("abs( "+eq.selectedText()+" )")

    def add_entre(self):
        self.txtOperando.insert(" / ")

    def add_factorizar(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("factor(  )")
        else:
            eq.insert("factor( "+eq.selectedText()+" )")

    
    def add_sin(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("sin(  )")
        else:
            eq.insert("sin( "+eq.selectedText()+" )")
    
    def add_cosh(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("cosh(  )")
        else:
            eq.insert("cosh( "+eq.selectedText()+" )")

    def add_ln(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("ln(  )")
        else:
            eq.insert("ln( "+culnrsor.selectedText()+" )")

    def add_por(self):
        self.txtOperando.insert(" * ")


    def add_exp(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("exp(  )")
        else:
            eq.insert("exp( "+eq.selectedText()+" )")
    
    def add_tan(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("tan(  )")
        else:
            eq.insert("tan( "+eq.selectedText()+" )")
    
    def add_sinh(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("sinh(  )")
        else:
            eq.insert("sinh( "+eq.selectedText()+" )")

    def add_log(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("log(  )")
        else:
            eq.insert("log( "+eq.selectedText()+" )")

    def add_menos(self):
        self.txtOperando.insert(" - ")


    def add_pi(self):
        self.txtOperando.insert(" pi ")


    def add_acos(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("acos(  )")
        else:
            eq.insert("acos( "+eq.selectedText()+" )")
    
    def add_tanh(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("tanh(  )")
        else:
            eq.insert("tanh( "+eq.selectedText()+" )")

    def add_derivada(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("derivate(  )")
        else:
            eq.insert("derivate( "+eq.selectedText()+" )")

    def add_punto(self):
        self.txtOperando.insert(".")


    def add_parentesis(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("(  )")
        else:
            eq.insert("( "+eq.selectedText()+" )")

    
    def add_mas(self):
        self.txtOperando.insert(" + ")

    def add_asin(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("asin(  )")
        else:
            eq.insert("asin( "+eq.selectedText()+" )")

    def add_factorial(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("factorial(  )")
        else:
            eq.insert("factorial( "+eq.selectedText()+" )")

    def add_integral(self):
        eq = self.txtOperando

        if eq.selectedText() == "":
            eq.insert("integrate(  )")
        else:
            eq.insert("integrate( "+eq.selectedText()+" )")"""