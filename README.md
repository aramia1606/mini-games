# 🎮 Python Mini-Games

**#Python #TerminalGames #BeginnerProjects #Hangman #SonarTreasure #CLIgames**

Ce dépôt rassemble plusieurs mini-jeux en **Python**, conçus pour être joués directement dans le **terminal**. Ils sont inspirés des exercices du site [Invent With Python](https://inventwithpython.com/invent4thed/chapter0.html#calibre_link-39), parfaits pour apprendre les bases de la programmation tout en s’amusant.

---

## 🕹️ Projets inclus

### 🔡 Hangman (Jeu du Pendu)
Un classique : devinez le mot en proposant une lettre à la fois, avant que le personnage ne soit entièrement pendu.

- 📄 Liste de mots utilisée : [wordlist.txt](https://github.com/Tom25/Hangman/blob/master/wordlist.txt)
- 🧠 Utilisation de la logique de jeu, gestion des erreurs, boucle principale
- 📦 Librairies : `random`

#### Exemple :
```
a
a _ _ _ 
   +---+
       |
       |
       |
      ===
b
a _ _ _ 
   +---+
   O   |
       |
       |
      ===
e
a _ e _ 
   +---+
   O   |
       |
       |
      ===
d
a _ e _ 
   +---+
   O   |
   |   |
       |
      ===
i
a _ e _ 
   +---+
   O   |
  /|   |
       |
      ===
y
a _ e _ 
   +---+
   O   |
  /|\  |
       |
      ===
f
a _ e _ 
   +---+
   O   |
  /|\  |
  /    |
      ===
q
a _ e _ 
   +---+
   O   |
  /|\  |
  / \  |
      ===
p
YOU LOOSE
Want to play again ? (yes or no)
```


---

### 🧭 Sonar Treasure Hunt
Un jeu de chasse au trésor sur une grille. Vous disposez d’un nombre limité de sonars pour localiser des coffres cachés.

- 📍 Grille générée aléatoirement à chaque partie
- 🎯 Distance des coffres mesurée et affichée
- 📦 Librairies : `random`, `math`

#### Exemple :
![image](https://github.com/user-attachments/assets/ec237575-a23c-4580-be33-e645d8213870)


---

## 🛠️ Technologies

- 🐍 Python 3
- 🧪 Librairies standards : `random`, `math`
- 💻 Interface en ligne de commande (CLI)

---

## 🚀 Installation & Lancement

```bash
git clone https://github.com/tonpseudo/python-mini-games.git
cd python-mini-games
python hangman.py       # ou
python sonar.py
```
