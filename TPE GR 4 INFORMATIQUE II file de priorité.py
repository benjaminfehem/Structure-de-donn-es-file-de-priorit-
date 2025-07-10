emails = []

priorite_valeurs = {
    "critique": 3,
    "important": 2,
    "normal": 1
}

print("🟢 Bienvenue dans le système de tri des messages par priorité !\n")

compteur = 1

while True:
    print(f"--- Message {compteur} ---")
    message = input("📝 Entre ton message (ou 'fin' pour terminer) : ").strip()
    if message.lower() == "fin":
        break

    niveau = input("🚨 Niveau d'urgence (critique / important / normal) : ").strip().lower()
    if niveau not in priorite_valeurs:
        print("❌ Niveau invalide. Réessaie.\n")
        continue

    emails.append((priorite_valeurs[niveau], message, niveau))
    print("✅ Message enregistré avec succès !\n")
    compteur += 1

# Tri des messages
emails.sort()

# Affichage
print("\n📋 Voici la liste des messages triés par ordres de priorité :\n")
for i, (_, message, niveau) in enumerate(emails, 1):
    print(f"{i}. [{niveau.upper()}] {message}")

# Pause finale
input("\n✅ Appuie sur Entrée pour fermer le programme...")