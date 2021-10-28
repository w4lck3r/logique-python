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
        return

    def variables(self):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return

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
        return "(" + self.gauche.to_string() + " ∨ " + self.droite.to_string() + ")"

    def hauteur(self) :
        return


    def variables(self):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return


class Non:
    """Classe permettant de construire des négations de formules"""
    def __init__(self,formule):
        self.formule = formule

    def f_formule(self):
        return self.formule

    def to_string(self):
        return "¬" + self.f_formule().to_string()

    def hauteur(self) :
        return

    def variables(self):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return




class Vrai:
    """Classe des tautologies"""
    def __init__(self):
        return

    def to_string(self):
        return "T"

    def hauteur(self) :
        return

    def variables(self):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return


class Faux:
    """Classe des contradictions"""
    def __init__(self):
        return

    def to_string(self):
        return "⊥"

    def hauteur(self) :
        return

    def variables(self):
        return

    def eval(self,valuation):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return



class Variable:
    """Classe permettant de construire des variables propositionnelles"""
    def __init__(self,variable):
        self.nom_variable = variable

    def nom(self):
        return self.nom_variable

    def to_string(self):
        return self.nom()

    def hauteur(self) :
        return

    def variables(self):
        return

    def eval(self,valuation):
        return

    def pousse_negation(self,neg):
        return
