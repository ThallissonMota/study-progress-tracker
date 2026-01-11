def separador(texto = "", tamanho = 60):
    """
    Exibe um separador visual opcional com texto centralizado.
    """
    if texto:
        print(f"\n{"=" * 25} ({texto}) {"=" * 25}\n")
    else:
        print(f"\n{"=" * tamanho}\n")