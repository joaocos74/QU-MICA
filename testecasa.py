import pandas as pd
tabela = pd.read_csv("banco de daos tcc.csv")
#colocar todas as letras em minuscula 
tabela= tabela.applymap(lambda x: x.lower() if isinstance(x, str) else x)