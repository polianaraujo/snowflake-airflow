# snowflake-airflow

Usando o airflow para orquestrar DAGs para execução no **Amazon Managed Workflows for Apache Airflow (MWAA)**

3. Instale o Airflow usando o arquivo de restrições, que é determinado com base na URL que passamos:
```python
AIRFLOW_VERSION=3.0.3

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 3.0.0 with python 3.9: https://raw.githubusercontent.com/apache/airflow/constraints-3.0.3/constraints-3.9.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

4. Execute o Airflow autônomo:
O comando inicializa o banco de dados, cria um usuário e inicia todos os componentes. ``airflow standalone``

5. Acesse a interface do usuário do Airflow:
Acesse ``localhost:8080`` o seu navegador e faça login com os detalhes da conta de administrador exibidos no terminal. Habilite o ``example_bash_operatorDAG`` na página inicial.