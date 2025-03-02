import time

def surprise_game():
    # Introduction
    print("Coucou ma chère, t'es prête pour un petit jeu ? 😏🎉")
    time.sleep(1)
    print("C'est un jeu de questions pas vraiment... surprenantes 😜 Prête ? 😘")
    time.sleep(1)

    # Question 1
    print("\nSi tu devais décrire notre relation en un plat, ce serait lequel ? 🍽️💖")
    time.sleep(1)
    plat = input("Réponse : ")

    # Question 2
    print("\nImagine que tu sois une super-héroïne, quel serait ton super-pouvoir ? 🦸‍♀️✨")
    time.sleep(1)
    pouvoir = input("Réponse : ")

    # Question 3
    print("\nSi tu pouvais choisir n'importe quel endroit dans le monde, où est-ce qu'on irait ensemble ? 🌍💕")
    time.sleep(1)
    endroit = input("Réponse : ")

    # Question 4
    print("\nEt là, si tu devais me décrire en trois mots, ce serait quoi ? 😏💘")
    time.sleep(1)
    description = input("Réponse : ")

    # Conclusion
    print("\nAllez, c'est l'heure de la révélation de ton verdict... 🕵️‍♀️")
    time.sleep(1)

    print(f"\nTu as choisi {plat} comme plat pour notre relation... MDR, je m'attendais à du Chô ! 😋💖")
    time.sleep(1)
    print(f"Ton super-pouvoir c'est {pouvoir}, c'est beautiful je vais dire !")
    time.sleep(1)
    print(f"Et notre destination idéale serait {endroit}... Je suis 100% partant ! Bon je voyais ta chambre aussi mdr ✈️🌴")
    time.sleep(1)
    print(f"Et pour finir, si tu me décris comme {description}, bahaha m'y attendais bon un peu, je suis Cute boy nan m'a dit celle que j'aime?! 😍💖")
    time.sleep(3)

    print("\nTu sais, peu importe ce que tu choisis, t'es déjà mon héroïne. 💘 Tu es unique à mes yeux et parfaite !")
    time.sleep(1)
    print("Merci d'être toi, merci d'être incroyable, je t'aime tellement ! 😘💖")

surprise_game()
