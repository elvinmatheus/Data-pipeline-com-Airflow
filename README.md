# Reddit Data Pipeline com Airflow

## Visão Geral

Este documento descreve o projeto de pipeline de dados que utiliza a API do Reddit como fonte de dados. O projeto tem como objetivo coletar os dados do Reddit, em particular do subreddit 'dataengineering' relacionados a carreira, processá-los e armazená-los como arquivos CSV em um bucket do Amazon S3. Para isso, foram utilizadas ferramentas e tecnologias como Python, Amazon S3, Amazon EC2 e Apache Airflow.

## Arquitetura do Pipeline de Dados

O pipeline de dados obedece a seguinte arquitetura

![Imagem representando o pipeline de dados](https://github.com/elvinmatheus/Data-pipeline-com-Airflow/blob/main/images/arquitetura_data_pipeline.png)

1. **Coleta de Dados**: Nesta etapa, os dados são coletados a partir da API pública do Reddit. A ferramenta utilizada para a coleta dos dados foi a biblioteca `requests` do Python.

2. **Transformação de Dados:** Após a coleta, os dados foram selecionados e transformados com o auxílio da biblioteca `pandas`

3. **Armazenamento de Dados:** Os dados selecionados e transformados são armazenados como arquivos CSV em um bucket do `Amazon S3`. Para interagir com o `Amazon S3`, é utilizada a biblioteca Python `s3fs`, que permite o envio dos arquivos CSV para o bucket.

4. **Agendamento e Orquestração:** O agendamento e a orquestração do pipeline são realizados usando o `Apache Airflow`. 

5. **Processamento em Nuvem**: Para a execução do pipeline, é utilizado o `Amazon EC2`. O EC2 é responsável por executar tarefas do pipeline, como a coleta de dados, processamento e envio para o `Amazon S3`.

## Configuração e execução do Pipeline

1. **Criação da instância EC2 e do bucket no S3:** É preciso ter o AWS CLI instalado e configurado corretamente para criar instâncias EC2 e buckets S3. Execute o arquivo `create_instance_and_bucket.sh`.

2. **Configuração do Ambiente:** Na instância criada é preciso configurar o ambiente de desenvolvimento com as bibliotecas e dependências necessárias, como o sistema de gerenciamento de pacotes pip, pandas, requests, s3fs e Apache Airflow.

```
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
```

3. **Definição das Tarefas e Configurações dos Parâmetros do Pipeline:** São definidas as tarefas, o DAG (Directed Acyclic Graphs) e os parâmetros necessários para a execução do pipeline, como a frequência da coleta dos dados.

4. **Configurações das Credenciais:** É necessário configurar as credenciais de acesso ao Amazon S3, criando uma nova role com regras de acesso ao S3 e atribuindo as permissões à instância EC2 criada.

5. **Execução do Pipeline:** O pipeline é executado diariamente ao fim do dia. A tarefa realiza a coleta, processamento e envio para o Amazon S3.