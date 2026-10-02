import math


class Noeud:
    """
    Classe permettant de représenter un noeud dans un arbre d'expression mathématique.
    """
    def __init__(self, val, liste=None):
        self.val = val
        self.liste = liste if liste is not None else []

    def ajouter_noeud(self, noeud):
        """
        Ajoute un noeud enfant à la liste des enfants du noeud actuel.
        """
        self.liste.append(noeud)

    def affichage_polonais(self):
        """
        Affiche l'expression mathématique du noeud et de ses enfants en notation polonaise.
        """
        a_explorer = [self]
        deja_visites = []

        while a_explorer:
            noeud = a_explorer.pop()

            if noeud not in deja_visites:
                deja_visites.append(noeud)

                print(noeud.val, end=" ")

                for enfant in reversed(noeud.liste):
                    if enfant not in deja_visites:
                        a_explorer.append(enfant)

    def evaluer(self, variables):
        # Cas d'une constante
        try:
            return float(self.val)
        except ValueError:
            pass

        # Cas d'une variable
        if self.val not in ["+", "-", "*", "/", "exp", "log", "sin", "cos"]:
            if self.val in variables:
                return float(variables[self.val])
            else:
                raise ValueError(
                    f"La variable '{self.val}' n'a pas de valeur."
                )

        # Opérateur +
        if self.val == "+":
            return self.liste[0].evaluer(variables) + self.liste[1].evaluer(variables)

        # Opérateur -
        if self.val == "-":
            return self.liste[0].evaluer(variables) - self.liste[1].evaluer(variables)

        # Opérateur *
        if self.val == "*":
            return self.liste[0].evaluer(variables) * self.liste[1].evaluer(variables)

        # Opérateur /
        if self.val == "/":
            return self.liste[0].evaluer(variables) / self.liste[1].evaluer(variables)

        # Fonctions
        if self.val == "exp":
            return math.exp(self.liste[0].evaluer(variables))

        if self.val == "log":
            return math.log(self.liste[0].evaluer(variables))

        if self.val == "sin":
            return math.sin(self.liste[0].evaluer(variables))

        if self.val == "cos":
            return math.cos(self.liste[0].evaluer(variables))
