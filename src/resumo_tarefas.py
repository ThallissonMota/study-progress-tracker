def resumo_tarefas(total_tarefas, tarefas_concluidas, nome):
    """
    Exibe um resumo do desempenho semanal de tarefas
    e avalia se a meta mínima foi atingida.
    """

    print(f"Olá, {nome}!")
    print("Este é o seu resumo semanal de tarefas:\n")

    # -------------------------
    # Dados gerais
    # -------------------------

    tarefas_restantes = total_tarefas - tarefas_concluidas

    print(f"Total de tarefas: {total_tarefas}")
    print(f"Tarefas concluídas: {tarefas_concluidas}")
    print(f"Tarefas pendentes: {tarefas_restantes}\n")

    # -------------------------
    # Cálculo do percentual
    # -------------------------

    percentual_concluido = (tarefas_concluidas / total_tarefas) * 100
    meta_minima = 80

    # -------------------------
    # Avaliação da meta
    # -------------------------
    
    if percentual_concluido < meta_minima:
        percentual_faltante = meta_minima - percentual_concluido
        tarefas_faltantes = (total_tarefas * percentual_faltante) / 100

        print(
            f"Seu desempenho atual é de {percentual_concluido:.2f}%, "
            f"abaixo da meta mínima de {meta_minima}%."
        )
        print(
            f"Faltam {percentual_faltante:.2f}% "
            f"({tarefas_faltantes:.2f} tarefas) para atingir a meta.\n"
        )

    elif percentual_concluido == meta_minima:
        print(
            f"Parabéns! Você atingiu exatamente a meta mínima "
            f"de {meta_minima}% das tarefas.\n"
        )

    else:
        percentual_restante = 100 - percentual_concluido

        print(
            f"Excelente trabalho! Você está acima da meta mínima "
            f"de {meta_minima}%."
        )
        print(
            f"Faltam apenas {percentual_restante:.2f}% "
            f"para concluir todas as tarefas.\n"
        )
