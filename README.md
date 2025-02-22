# pipelineAf
## Projeto de um pipeline Airflow executando localmente no WSL do windows

<head><strong>Etapas:</strong></head>
<br>
<p> 1. Com o terminal WSL aberto, crie o diretório do projeto</p>
![image](https://github.com/user-attachments/assets/9d86c7c7-64b7-42bf-8c0f-f5fe19f4e703)
<br>
<p> e vá para o diretório criado<p>
  ![image](https://github.com/user-attachments/assets/2b91efff-4dfd-4b9f-84b9-ef4c2544ee69)

<br>
<br>
<p>2. Crie um ambiente virtual para o projeto </p>
![image](https://github.com/user-attachments/assets/1257892f-5bd7-4eb6-b486-63b16ea41bc4)
<br>
<p> E ative-o<p>
  ![image](https://github.com/user-attachments/assets/970a26c7-6937-46c4-993e-ab5affe0b07b)

<br>
<br>
<p>3. Acesse o arquivo com o comando nano ~/.bashrc e faça e insira nele AIRFLOW_HOME="diretorio do projeto" </p>
<p>Valide com o comando cd $AIRFLOW_HOME, se foi para o diretório do projeto, funcionou</p>
<br>
<br>
<p>4. Instale o apache airflow com o comando pip install apache-airflow e inicialize o database com airflow db init</p>
<p> Crie nele as pastas dags, logs e plugins<p>
  ![image](https://github.com/user-attachments/assets/3fc67de7-ab9a-4b59-a742-2c41ef2dcd60)
<br>
<br>
<p>5. Crie o Airflow User:</p>
<p>airflow users create --username admin -–password admin -–firstname admin -–lastname admin -–role Admin -–email youremail@email.com</p>
<br>
<br>
<p>6. Execute o airflow scheduler e webserver</p>
<p>airflow webserver & airflow scheduler</p>
<P>No Navegador com localhost:8008 aparecerá a UI do Airflow </P>
![image](https://github.com/user-attachments/assets/839e1aac-5d3b-4d17-951d-bae5871cbebd)
<br>
Após login aparecerá a tela principal
<br>
![image](https://github.com/user-attachments/assets/b96b2e02-58ff-4aea-aa9a-a5b2e2474e29)





