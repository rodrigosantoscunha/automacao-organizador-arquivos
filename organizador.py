import os
import shutil

# --- CONFIGURAÇÃO ---
# Onde estão os arquivos bagunçados?
# IMPORTANTE: Você precisa criar essa pasta "Teste_Bagunca" em Downloads antes de rodar
diretorio_origem = r"C:\Users\rodri\Downloads\Teste_Bagunca"

# Para onde eles vão? (O script cria essa pasta sozinho)
diretorio_destino = r"C:\Users\rodri\Documents\Arquivos_Organizados"

# Dicionário: Define qual extensão vai para qual pasta
regras = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Apresentacoes": [".ppt", ".pptx"],
    "Compactados": [".zip", ".rar"]
}

# --- LÓGICA DO SCRIPT ---
def organizar_arquivos():
    # Verifica se a pasta de origem existe
    if not os.path.exists(diretorio_origem):
        print(f"ERRO: A pasta '{diretorio_origem}' não foi encontrada.")
        print("Crie a pasta 'Teste_Bagunca' dentro de Downloads e coloque arquivos lá!")
        return

    # 1. Listar todos os arquivos na pasta de origem
    lista_arquivos = os.listdir(diretorio_origem)

    for arquivo in lista_arquivos:
        caminho_completo = os.path.join(diretorio_origem, arquivo)

        # Se for uma pasta, ignora
        if os.path.isdir(caminho_completo):
            continue

        # Separa o nome da extensão
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        # Verifica para qual pasta o arquivo deve ir
        pasta_destino_nome = "Outros"
        for pasta, extensoes in regras.items():
            if extensao in extensoes:
                pasta_destino_nome = pasta
                break
        
        # Cria o caminho final
        caminho_pasta_final = os.path.join(diretorio_destino, pasta_destino_nome)

        # Se a pasta não existir, cria ela
        if not os.path.exists(caminho_pasta_final):
            os.makedirs(caminho_pasta_final)

        # Move o arquivo
        shutil.move(caminho_completo, os.path.join(caminho_pasta_final, arquivo))
        print(f"✅ Movido: {arquivo} -> {pasta_destino_nome}")

if __name__ == "__main__":
    organizar_arquivos()
    print("--- Fim da Organização ---")