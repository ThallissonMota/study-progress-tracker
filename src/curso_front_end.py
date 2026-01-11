def curso_front_end(total_aulas, aulas_concluidas, nome, dias_decorridos):
    """
    Exibe o progresso do curso de Front-end e estima o tempo necessário
    para conclusão com base em aulas diárias.
    """

    print(f"\nOlá, {nome}!")
    print("Acompanhe abaixo o seu progresso no curso de Front-end.")
    print("OBS: A meta é finalizar o curso até o fim de Dezembro.\n")

    # -------------------------
    # Dados gerais do curso
    # -------------------------
    
    aulas_restantes = total_aulas - aulas_concluidas

    print(f"Total de aulas: {total_aulas}")
    print(f"Aulas concluídas: {aulas_concluidas}")
    print(f"Aulas restantes: {aulas_restantes}\n")

    # -------------------------
    # Cálculo do progresso
    # -------------------------

    percentual_concluido = (aulas_concluidas / total_aulas) * 100
    percentual_restante = 100 - percentual_concluido

    print(f"Progresso atual: {percentual_concluido:.2f}%")
    print(f"Falta concluir: {percentual_restante:.2f}%\n")

    # -------------------------
    # Estimativas de tempo
    # -------------------------

    aulas_por_dia = 3
    periodo_total_dias = 365
    dias_restantes_periodo = periodo_total_dias - dias_decorridos

    dias_necessarios_para_concluir = aulas_restantes / aulas_por_dia
    saldo_dias = dias_restantes_periodo - dias_necessarios_para_concluir

    dias_ja_planejados = 31  # dias já considerados no planejamento
    saldo_final = saldo_dias - dias_ja_planejados

    print(
        f"Estudando {aulas_por_dia} aulas por dia, "
        f"você concluirá o curso em aproximadamente "
        f"{dias_necessarios_para_concluir:.2f} dias."
    )

    print(
        f"\nDias corridos restantes até o fim do período de estudos: "
        f"{dias_restantes_periodo}\n"
    )

    # -------------------------
    # Avaliação final
    # -------------------------

    if saldo_final < 0:
        aulas_extras = abs(saldo_final) * aulas_por_dia
        print(
            f"Você precisará adiantar {abs(saldo_final):.2f} dias de estudo "
            f"({aulas_extras:.0f} aulas) para manter folgas nos fins de semana."
        )
    else:
        print(
            f"Parabéns! Você possui {saldo_final:.2f} dias de folga "
            f"durante a semana."
        )
