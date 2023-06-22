# Reddit Data Pipeline com Airflow

## Visão Geral

Este documento descreve o projeto de um pipeline de dados que utiliza a API do Reddit como fonte de dados. O projeto tem como objetivo coletar dados do Reddit, em particular dos top posts do subreddit 'dataengineering' relacionados a carreira, processá-los e armazená-los como arquivos `CSV` em um bucket do `Amazon S3`. Para isso, foram utilizadas ferramentas e tecnologias como `Python`, `Amazon S3`, `Amazon EC2` e `Apache Airflow`.

## Arquitetura do Pipeline de Dados

O pipeline de dados obedece a seguinte arquitetura:

![Imagem representando o pipeline de dados](https://github.com/elvinmatheus/Data-pipeline-com-Airflow/blob/main/images/Arquitetura.png)

1. **Coleta de Dados**: Nesta etapa, os dados são coletados a partir da API pública do Reddit. A ferramenta utilizada para a coleta dos dados foi a biblioteca `requests` do `Python`.

2. **Transformação de Dados:** Após a coleta, os dados foram selecionados e transformados com o auxílio da biblioteca `pandas`.

3. **Armazenamento de Dados:** Os dados selecionados e transformados são armazenados como arquivos CSV em um bucket do `Amazon S3`. Para interagir com o `Amazon S3`, é utilizada a biblioteca `s3fs` do `Python`, que permite o envio dos arquivos CSV para o bucket.

4. **Agendamento e Orquestração:** O agendamento e a orquestração do pipeline são realizados com o `Apache Airflow`.

5. **Processamento em Nuvem**: Uma instância do `Amazon EC2` é responsável por executar as tarefas do pipeline, como a coleta de dados, processamento e envio para o `Amazon S3`.

## Configuração e execução do Pipeline

1. **Criação da instância EC2 e do bucket no S3:** É preciso ter o [`AWS CLI` instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) localmente e configurado corretamente para criar a instância no `EC2` e o bucket no `S3`. Configure os parâmetros do arquivo `create_instance_and_bucket.sh` para o seu uso. Execute o arquivo com os seguintes comandos:

```
sudo chmod +x create_instance_and_bucket.sh
sudo ./create_instance_and_bucket.sh
```

2. **Configuração do Ambiente:** Na instância criada, é preciso configurar o ambiente de desenvolvimento com as bibliotecas e dependências necessárias, como o sistema de gerenciamento de pacotes `pip`, `pandas`, `requests`, `s3fs` e `Apache Airflow`.

```
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
```

3. **Definição das Tarefas e Configurações dos Parâmetros do Pipeline:** Envie os arquivos `reddit_dag.py` e `reddit_etl.py` para a instância `EC2` criada. Nestes arquivos estão definidas o DAG, as Tasks e os parâmetros necessários para a execução do pipeline, como a frequência da coleta dos dados. Após o envio dos arquivos, configure o arquivo `airflow.cfg` para que o parâmetro `dags_folder` aponte para a pasta onde estão os códigos do pipeline de dados.

4. **Configurações das Credenciais:** É necessário configurar as credenciais de acesso ao `Amazon S3`, criando uma nova role com regras de acesso ao `S3` e atribuindo as permissões à instância `EC2` criada.