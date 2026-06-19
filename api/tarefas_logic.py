# api/views/tarefas_logic.py ou api/tarefas_logic.py
class TarefaService:
    def verificar_status_atraso(self, dias_restantes):
        # Regra Crítica: 0 dias restantes significa que está atrasado
        if dias_restantes <= 0:
            return True
        return False