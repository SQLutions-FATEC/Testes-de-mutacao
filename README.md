# Testes-de-mutacao

Este repositório é um exemplo prático de como utilizar testes de mutação em Python para avaliar a qualidade e a cobertura da sua suíte de testes.

## O que são Testes de Mutação?

Testes de mutação são uma técnica de teste de software usada para avaliar e melhorar a qualidade da sua suíte de testes (como os testes de unidade). O processo funciona da seguinte forma:

1. **Geração de Mutantes:** A ferramenta de teste introduz pequenas modificações (falhas intencionais) no código original, criando versões alternativas do programa chamadas de "mutantes". Exemplos de mutações incluem alterar um `<=` para `<`, trocar um `True` por `False`, ou mudar um `+` por `-`.
2. **Execução da Suíte:** A sua suíte de testes é executada contra cada um desses mutantes.
3. **Sobrevivência ou Morte:** 
   - Se os seus testes **falharem** ao rodar um mutante, significa que os testes identificaram o defeito. O mutante foi "morto" (Killed). Isso é um bom sinal!
   - Se os seus testes **passarem** mesmo com o código modificado com defeito, o mutante "sobreviveu" (Survived). Isso indica um ponto cego na sua suíte de testes.

O objetivo do teste de mutação não é testar a aplicação em si, mas **testar os seus testes**, garantindo que eles sejam rigorosos o suficiente para pegar quebras acidentais de lógica no futuro.

## Como os Testes de Mutação são usados neste projeto?

Este projeto utiliza a biblioteca [`mutmut`](https://mutmut.readthedocs.io/en/latest/) para testar a lógica de uma simples classe de serviço (`TarefaService` em `api/tarefas_logic.py`). A função principal do serviço verifica se uma tarefa está atrasada com base nos dias restantes.

Durante o desenvolvimento deste exemplo, a suíte de testes em `tests/test_tarefas.py` tinha uma cobertura que aparentemente parecia completa. Porém, quando executamos o `mutmut`, ele identificou que um mutante conseguia alterar a regra de negócio (`if dias_restantes <= 0:` para `if dias_restantes <= 1:`) sem que nenhum teste falhasse. 

Isso destacou que faltava um caso de teste para o "limiar" exato de não-atraso (quando `dias_restantes == 1`). Após incluir um teste cobrindo esse caso de limite (boundary testing), a suíte passou a matar todos os mutantes com sucesso, tornando-se mais robusta.

## Como Executar

### Pré-requisitos
Certifique-se de que o Python 3.13 ou superior está instalado. O projeto fornece duas formas de configurar o ambiente e instalar as dependências: usando `uv` (recomendado) ou o `pip` padrão.

### 1. Configurando o Ambiente

**Opção A: Usando o `uv` (Recomendado)**
O `uv` é um gerenciador de pacotes ultra-rápido. Se você o possui instalado, basta rodar:
```bash
uv sync
```
*Isso criará automaticamente a pasta `.venv` e instalará as versões exatas das dependências definidas no `uv.lock`. Após o sync, o ambiente virtual pode ser ativado normalmente se necessário.*

**Opção B: Usando o `pip` padrão**
Se você prefere usar o ecossistema padrão do Python, utilize o arquivo `requirements.txt`:
1. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```
2. Ative o ambiente virtual:
   - No Linux/macOS: `source .venv/bin/activate`
   - No Windows: `.venv\Scripts\activate`
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Rodando os Testes

*(Nota: Certifique-se de estar com o `.venv` ativado se estiver usando pip, ou use `uv run <comando>` caso não tenha ativado)*

1. **Execute a suíte de testes normal (Pytest):**
   ```bash
   pytest
   ```
   Isso executará a suíte de testes padrão, mostrando se a regra original do código funciona.

2. **Execute os testes de mutação (Mutmut):**
   ```bash
   mutmut run
   ```
   O `mutmut` rodará os testes em cima das mutações geradas. O processo pode demorar um pouco dependendo da quantidade de código e testes.

3. **Verifique os resultados das mutações:**
   ```bash
   mutmut results --all true
   ```
   Este comando mostrará uma visão geral de quantos mutantes foram gerados e o status final deles (Mortos, Sobreviventes, etc).

4. **Exibir um mutante sobrevivente específico (caso exista):**
   Para ver o código específico que foi modificado e sobreviveu, copie o nome do mutante listado no comando anterior e execute:
   ```bash
   mutmut show <NOME_DO_MUTANTE>
   ```
   *(Exemplo: `mutmut show api.tarefas_logic.xǁTarefaServiceǁverificar_status_atraso__mutmut_2`)*