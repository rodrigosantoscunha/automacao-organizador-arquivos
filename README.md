# 📂 Organizador Automático de Arquivos (Python)

## 🎯 Sobre o Projeto
Script desenvolvido para automatizar a organização de arquivos em ambientes administrativos.
Ele monitora uma pasta de entrada e distribui os arquivos (PDFs, Planilhas, Imagens) para pastas definitivas automaticamente.

## 🛠️ Tecnologias
- Python 3
- Bibliotecas: `os`, `shutil`

## ⚙️ Como funciona
O script lê a extensão do arquivo e move para o destino correto:
- `.xlsx` -> Pasta Planilhas
- `.pdf` -> Pasta Documentos
- `.jpg` -> Pasta Imagens