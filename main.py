import pandas as pd

def main():
    try:
        # Ler o CSV
        df = pd.read_csv("vendas.csv", sep=";")
    except FileNotFoundError:
        print("❌ Erro: Arquivo 'vendas.csv' não encontrado.")
        return

    # Verificar colunas obrigatórias
    colunas_esperadas = ["Produto", "Quantidade", "Preço"]
    for coluna in colunas_esperadas:
        if coluna not in df.columns:
            print(f"❌ Erro: Coluna '{coluna}' não encontrada no arquivo.")
            return

    # Criar coluna total
    df["Total"] = df["Quantidade"] * df["Preço"]

    # Calcular total vendido
    total_vendas = df["Total"].sum()

    # Produto mais vendido
    mais_vendido = df.loc[df["Quantidade"].idxmax()]

    # Exibir resultados
    print("\n📊 RELATÓRIO DE VENDAS")
    print("-" * 30)
    print(f"💰 Total vendido: R$ {total_vendas:.2f}")
    print(f"🏆 Produto mais vendido: {mais_vendido['Produto']}")
    print(f"📦 Quantidade vendida: {mais_vendido['Quantidade']}")

    # Salvar relatório
    df.to_csv("relatorio_final.csv", sep=";", index=False)
    print("\n✅ Relatório salvo como 'relatorio_final.csv'")

if __name__ == "__main__":
    main()