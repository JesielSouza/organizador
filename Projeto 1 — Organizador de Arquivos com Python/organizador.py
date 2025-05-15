import os
import shutil

pasta_alvo = input("Digite o caminho da pasta que você quer organizar: ").strip()


if not os.path.isdir(pasta_alvo):
    print("❌ Caminho inválido.")
    exit()


tipos_arquivos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Compactados": [".zip", ".rar", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi", ".bat", ".sh"],
    "Outros": []
}

def descobrir_categoria(extensao):
    for categoria, extensoes in tipos_arquivos.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"

for item in os.listdir(pasta_alvo):
    item_path = os.path.join(pasta_alvo, item)

    if os.path.isfile(item_path):
        _, extensao = os.path.splitext(item)
        categoria = descobrir_categoria(extensao)

        pasta_destino = os.path.join(pasta_alvo, categoria)


        os.makedirs(pasta_destino, exist_ok=True)

        shutil.move(item_path, os.path.join(pasta_destino, item))
        print(f"🔃 {item} -> {categoria}/")

print("\n✅ Organização Concluída!")