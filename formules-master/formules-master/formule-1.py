class Et:
    """Classe permettant de construire des conjonctions de formules"""
    def __init__(self,gauche,droite):
        self.gauche = gauche
        self.droite  = droite

    def f_gauche(self):
        return self.gauche

    def f_droite(self):
        return self.droite

    def to_string(self):
        return "(" + self.f_gauche().to_string() + " ∧ " + self.f_droite().to_string() + ")"

    def hauteur(self) :
        return 1 + max(self.f_gauche().hauteur(), self.f_droite().hauteur())

    def variables(self):
        return self.f_gauche().variables() | self.f_droite().variables()

    def eval(self,valuation):
        return min(self.f_gauche().eval(valuation), self.f_droite().eval(valuation))

    def pousse_negation(self,neg):
        if neg==True:
            return Ou(self.f_gauche().pousse_negation(True),self.f_droite().pousse_negation(True))
        else:
            return Et(self.f_gauche().pousse_negation(False),self.f_droite().pousse_negation(False))

class Ou:
    """Classe pemettant de construire des disjonctions de formules"""
    def __init__(self,gauche,droite):
        self.gauche = gauche
        self.droite  = droite

    def f_gauche(self):
        return self.gauche

    def f_droite(self):
        return self.droite

    def to_string(self):
        return  "(" + self.f_gauche().to_string() + " v " + self.f_droite().to_string() + ")"

    def hauteur(self) :
        return 1 + max(self.f_gauche().hauteur(), self.f_droite().hauteur())


    def variables(self):
        return self.f_gauche().variables() | self.f_droite().variables()

    def eval(self,valuation):
        return max(self.f_gauche().eval(valuation), self.f_droite().eval(valuation))

    def pousse_negation(self,neg):
        if neg==True:
            return Et(self.f_gauche().pousse_negation(True),self.f_droite().pousse_negation(True))
        else:
            return Ou(self.f_gauche().pousse_negation(False),self.f_droite().pousse_negation(False))


class Non:
    """Classe permettant de construire des négations de formules"""
    def __init__(self,formule):
        self.formule = formule

    def f_formule(self):
        return self.formule

    def to_string(self):
        return "¬" + self.f_formule().to_string()

    def hauteur(self) :
        return 1 + self.f_formule().hauteur()

    def variables(self):
        return set(self.f_formule().variables())

    def eval(self,valuation):
        res =  True - self.f_formule().eval(valuation)
        if res == 1:
            return True
        else:
            return False

    def pousse_negation(self,neg):
        if neg==True:
            return self.f_formule()
        else:
            return self.f_formule().pousse_negation(True)
            



class Vrai:
    """Classe des tautologies"""
    def __init__(self):
        return

    def to_string(self):
        return "T"

    def hauteur(self) :
        return 0

    def variables(self):
        return set()

    def eval(self,valuation):
        return True

    def pousse_negation(self,neg):
        if neg==False:
            return Faux()
        else:
            return Vrai()


class Faux:
    """Classe des contradictions"""
    def __init__(self):
        return

    def to_string(self):
        return "⊥"

    def hauteur(self) :
        return 0

    def variables(self):
        return set()

    def eval(self,valuation):
        return False

    def pousse_negation(self,neg):
        if neg==True:
            return Vrai()
        else:
            return Faux()



class Variable:
    """Classe permettant de construire des variables propositionnelles"""
    def __init__(self,variable):
        self.nom_variable = variable

    def nom(self):
        return self.nom_variable

    def to_string(self):
        return self.nom()

    def hauteur(self) :
        return 0

    def variables(self):
        return set(self.nom())

    def eval(self,valuation):
        return valuation[self.nom()]

    def pousse_negation(self,neg):
        if neg==False:
            return Variable(self.nom())
        else:
            return Non(Variable(self.nom()))