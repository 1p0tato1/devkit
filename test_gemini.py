import google.generativeai as genai
import os

# On récupère la clé
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("--- Liste des modèles disponibles ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Modèle trouvé : {m.name}")
            
    # Tentative d'appel direct
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Réponds 'OK' si tu marches.")
    print(f"\nRéponse de l'IA : {response.text}")

except Exception as e:
    print(f"\n❌ Erreur : {e}")
