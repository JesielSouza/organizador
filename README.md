# Organizador de Arquivos com Python

Script simples para organizar arquivos dentro de uma pasta, separando-os em subpastas por tipo (imagens, documentos, áudios, vídeos, compactados, etc).

---

## Funcionalidades

- Move arquivos para pastas conforme extensão
- Cria as pastas automaticamente, se não existirem
- Suporta vários tipos comuns de arquivo
- Simples e rápido para organizar diretórios bagunçados

---

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/JesielSouza/organizador-arquivos-python.git
   cd organizador-arquivos-python
   ```

2. Execute o script:
   ```bash
   python organizador.py
   ```

3. Informe o caminho da pasta que deseja organizar quando solicitado.

---

## Exemplo de pasta de testes

Incluí um script para criar uma pasta de testes com arquivos de exemplo:

```bash
python criar_pasta_teste.py
```

Isso gera a pasta `pasta_teste_organizador` com arquivos diversos para você testar.

---

## Requisitos

- Python 3.13
- Apenas módulos padrão (`os`, `shutil`)

---

## Melhorias futuras

- Evitar sobrescrita de arquivos com nomes iguais
- Aceitar argumento de caminho via linha de comando
- Gerar logs detalhados
- Interface gráfica para usuários leigos

---

## Autor

Jesiel Souza — [JesielSouza](https://github.com/JesielSouza)

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
