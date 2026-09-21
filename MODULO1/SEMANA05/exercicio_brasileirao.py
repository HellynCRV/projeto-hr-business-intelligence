import pandas as pd

caminho_arquivo = "MODULO1/SEMANA05/campeonato-brasileiro-full.csv"

try:
    df = pd.read_csv(caminho_arquivo, encoding="ISO-8859-1")
   
    
    # 1. Coluna Nova: Total de Gols da Partida
    df['total_gols'] = df['mandante_Placar'] + df['visitante_Placar']
    
    # 2. Coluna Nova: Resultado do Jogo
    def calcular_vencedor(linha):
        if linha['mandante_Placar'] > linha['visitante_Placar']:
            return 'Vitoria Mandante'
        elif linha['visitante_Placar'] > linha['mandante_Placar']:
            return 'Vitoria Visitante'
        return 'Empate'
        
    df['resultado_final'] = df.apply(calcular_vencedor, axis=1)
    
 
    
    # Exibe apenas as colunas importantes e as novas que criei
    colunas_exibir = ['mandante', 'visitante', 'mandante_Placar', 'visitante_Placar', 'total_gols', 'resultado_final']
    print(df[colunas_exibir].head(5))
 
except Exception as e:
    print(f"Ocorreu um erro ao processar o Brasileirão: {e}")