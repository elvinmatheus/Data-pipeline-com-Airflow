# Data Pipeline with Airflow

## Visão Geral

Este documento descreve o projeto de pipeline de dados que utiliza a API do Reddit como fonte de dados. O projeto tem como objetivo coletar os dados do Reddit, em particular do subreddit 'dataengineering' relacionados a carreira, processá-los e armazená-los como arquivos CSV em um bucket do Amazon S3. Para isso, foram utilizadas ferramentas e tecnologias como Python, Amazon S3, Amazon EC2 e Apache Airflow.

## Arquitetura do Pipeline de Dados

O pipeline de dados obedece a seguinte arquitetura

![Imagem representando o pipeline de dados](https://github.com/elvinmatheus/Data-pipeline-with-Airflow/blob/main/Sem%20t%C3%ADtulo-2023-05-25-1435.png)

1. **Coleta de Dados**: Nesta etapa, os dados são coletados a partir da API pública do Reddit. A ferramenta utilizada para a coleta dos dados foi a biblioteca `requests` do Python.

2. **Transformação de Dados**: Após a coleta, os dados foram selecionados e transformados com o auxílio da biblioteca `pandas`

3. **Armazenamento de Dados**: Os dados selecionados e transformados são armazenados como arquivos CSV em um bucket do Amazon S3. Para interagir com o Amazon S3, é utilizada a biblioteca Python `s3fs`, que permite o envio dos arquivos CSV para o bucket.

4. **Agendamento e Orquestração**: O agendamento e a orquestração do pipeline são realizados usando o Apache Airflow. 

5. **Processamento em Nuvem**: Para a execução do pipeline, é utilizado o Amazon EC2. O EC2 é responsável por executar tarefas do pipeline, como a coleta de dados, processamento e envio para o Amazon S3.

## Ferramentas e Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes ferramentas e tecnologias:

- Python:
- Bibliotecas Python:
- Amazon Web Services:
- Apache Airflow:
- Reddit public API: