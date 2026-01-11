# Associando as funçoes que foram definidas em outro arquivo para esse principal

from resumo_tarefas import resumo_tarefas
from curso_sql import curso_sql
from curso_front_end import curso_front_end
from separador import separador
# -------------------------------------------------------------------

# =====================
# INÍCIO DO RELATÓRIO
# =====================

separador("INÍCIO")

resumo_tarefas(total_tarefas = 10, tarefas_concluidas = 9, nome = "Thallisson")

separador()

curso_front_end(total_aulas = 797, aulas_concluidas = 0, nome = "Thallisson", dias_decorridos = 31)

separador()

curso_sql(total_aulas = 80, aulas_concluidas = 12, nome = "Thallisson", dias_decorridos = 10)

# =====================
# FIM DO RELATÓRIO
# =====================

separador("FIM")
