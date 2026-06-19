from api.tarefas_logic import TarefaService

def test_tarefa_com_prazo_folgado():
    service = TarefaService()
    assert service.verificar_status_atraso(5) == False

def test_tarefa_muito_atrasada():
    service = TarefaService()
    assert service.verificar_status_atraso(-5) == True

def test_tarefa_no_dia_do_vencimento_limite():
    service = TarefaService()
    # Este assert força o teste a validar exatamente o limite da condição (0)
    assert service.verificar_status_atraso(0) == True