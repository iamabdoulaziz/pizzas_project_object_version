import time
import sys

# Fonction pour afficher chaque caractère du texte lentement
def type_effect(content, delay=0.1):
    for char in content:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ajoute une nouvelle ligne à la fin

# Introduction
type_effect("Aller... ça va commencer... accroche-toi, j'ai une surprise pour toi!", 0.1)
time.sleep(1)

# Question 1 - Prénom
type_effect("Alors, dis-moi, comment tu t'appelles, reine de mon cœur ? 👑", 0.1)
name = input()

# Message en fonction de la réponse
type_effect(f"Ah, donc c'est bien toi, {name}! 😏 J'ai une surprise bien spéciale pour toi... 💖", 0.1)
time.sleep(1)

# Afficher un cœur ASCII
heart = """
    ******       ******
   **      **   **      **
  **        ** **        **
 **          ***          **
 **           *           **
 **                       **
  **                     **
    **                 **
      **             **
        **         **
          **     **
            ** **
              *
"""
type_effect(heart, delay=0.2)

# Message doux et personnel
type_effect(f"Food is bae, et toi t'es mon food préférée, Babe ! 🍔💖", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("J'adore passer du temps avec toi, c'est tellement agréable. 😌💖", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Je t'aime tellement, Babe, merci de m'aimer. 🥺💖", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Merci pour tout, t'es juste merveilleuse. 😘💖", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

# Conclusion
type_effect("Tu rends tout tellement mieux, t'es mon bonheur à chaque instant. 💕", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Impossible de sortir de ma tête, j'suis accro, tu sais que je t'admire de fou haha trop fan de toi, Babe 😍💖", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Partage moi tes joies et tes peines, je trouverais pas vraiment les mots souvent mais je t'écouterais", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Je ferai pareil avec toi babe, je voudrais être là pour toi", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Tu sais quoi babe ?..", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("On est trop beau ensemble !", 0.1)
time.sleep(1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Eumh, dis-moi, ça te dis de faire une partie de glace avec moi ? Oui ou Oui", 0.1)
glace = input()
glace.lower()
type_effect("Haha let's go !!", 0.1)

# Séparation
type_effect("\n" + "-"*40 + "\n", 0.1)

type_effect("Kinshanaa ... 💖", 0.1)
