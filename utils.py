# Funções de Suporte


def filtrar_nulos(df, coluna):
    """
    Retorna apenas as linhas onde
    a coluna especificada possui valores nulos.
    """
    return df[df[coluna].isna()]


def preencher_nulos(df, colunas, valor_preenchimento):
    df_copia = df.copy()
    df_copia[colunas] = df_copia[colunas].fillna(valor_preenchimento)

    return df_copia


def identificar_atraso(valor):
    if valor > 0:
        return 1
    return 0


def limpar_dados_faltantes(df, colunas_criticas):
    """
    Remove linhas que possuem valores vazios (NaN) nas colunas especificadas.
    """
    df_limpo = df.dropna(subset=colunas_criticas)

    return df_limpo
