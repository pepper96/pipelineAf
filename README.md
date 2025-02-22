# Pipeline Af
Projeto de Airflow executando em WSL no windows

### Inicializando o Airflow
**Para todos os comandos, serão realizados no terminal o WSL**
<br>
<br>
1. Instalação da virtualenv do Python

![image](https://github.com/user-attachments/assets/2870c613-62db-4ac9-a94f-c1e406e898fd)


2. criar o diretório do projeto


![image](https://github.com/user-attachments/assets/5aef13e0-0bd4-4e3f-b8a2-869bca48ea09)

E depois deverá acessar

![image](https://github.com/user-attachments/assets/fd307e79-4146-4de3-874d-ab9e109ee7fc)


3. criar a venv do projeto, uma versão do Python dedicada para ele

![image](https://github.com/user-attachments/assets/1762d3f4-ec7f-40c4-aac6-53a1ee8eaa91)


Para ativar esse ambiente deve-se executar o seguinte comando

![image](https://github.com/user-attachments/assets/4138324a-36f7-4595-9d50-097eb5744187)

4. Criar a variável AIRFLOW_HOME. Para isso, deve executar os seguintes comandos:

![image](https://github.com/user-attachments/assets/d1f19669-55a1-4812-8600-0423d82c429a)

Que abrirá o arquivo .bashrc e deverá inserir a informação abaixo

![image](https://github.com/user-attachments/assets/5eaabdca-b569-4b86-ba60-532262f80b0a)

Ou seja, o diretório do projeto.
<br>
Após inserir a informação aperte ctrl + s (para salvar) e ctrl + x (para fechar o arquivo)


Para verificar se funcionou execute o comando cd $AIRFLOW_HOME, será direcionado para o diretório do peojeto.
<br>
<br>
5. Instalar Apache Airflow

![image](https://github.com/user-attachments/assets/c7e6cb38-a517-4dd9-860b-ccb410254995)

6. Inicializar database

![image](https://github.com/user-attachments/assets/2ca173b0-f134-474d-98d6-01a28e1b20d6)

Neste comando são criados os arquivos de config necessários para o Airlfow
<br>
Além disso deve criar as pastas dags, logs e plugins

7. Criar um usuário do airflow
airflow users create --username admin -–password admin -–firstname admin -–lastname admin -–role Admin -–email youremail@email.com

8. Inicializar o Airflow

![image](https://github.com/user-attachments/assets/fbbf318f-251b-41e7-a38c-600c30330793)

9. Acessando Airflow
Com http://localhost:8080/ é possível acessar a UI do Airflow


Insira os dados de acesso criados
![image](https://github.com/user-attachments/assets/69d30a89-c961-4ddc-914a-cdbf019feeee)



Será direcionado para a tela abaixo
![image](https://github.com/user-attachments/assets/e8f6a168-9b56-446d-911f-836f4308c4a6)


10. Acessando uma DAG

A DAG abaixo extrai informações e preços de alguns fundos imobiliários e armazena em arquivos csv e parquet para consumo de dashboards.

![image](https://github.com/user-attachments/assets/5f43d22f-1653-4c39-b840-5081ca718598)





























