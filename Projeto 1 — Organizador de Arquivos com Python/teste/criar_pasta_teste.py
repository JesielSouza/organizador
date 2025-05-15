import os

# Nome da pasta de teste
pasta_teste = "pasta_teste_organizador"

# Estrutura de arquivos de exemplo
arquivos_exemplo = [
    "foto1.jpg",
    "foto2.png",
    "documento1.pdf",
    "documento2.docx",
    "musica1.mp3",
    "video1.mp4",
    "arquivo.zip",
    "script.sh",
    "notas.txt",
    "apresentacao.pptx",
    "instalador.exe",
    "sem_extensao",
    "arquivo.DESCONHECIDO"
]

# Criando a pasta
os.makedirs(pasta_teste, exist_ok=True)

# Criando os arquivos vazios
for nome_arquivo in arquivos_exemplo:
    caminho = os.path.join(pasta_teste, nome_arquivo)
    with open(caminho, 'w') as f:
        f.write("")  # Conteúdo vazio

print(f"✅ Pasta de teste '{pasta_teste}' criada com {len(arquivos_exemplo)} arquivos.")
