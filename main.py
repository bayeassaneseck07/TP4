from Noeud import Noeud

# Construction de 2 et y
noeud_2 = Noeud("2", [])
noeud_y = Noeud("y", [])

# Construction de 2 + y
noeud_plus = Noeud("+", [noeud_2, noeud_y])

# Construction de exp(2 + y)
racine = Noeud("exp", [noeud_plus])

# Affichage polonais
racine.affichage_polonais()
