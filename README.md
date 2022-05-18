# python_Reconhecimento_Facial_Mysql
Reconhecimento Facial com inclusão dos usuários reconhecidos no banco de dados mysql

<img src="https://github.com/michaelsantsbird/python_Reconhecimento_Facial_Mysql/blob/main/img/ver.png" />

# Começando

Primeiro será necessário realizar a detecção da face e capturar as fotos.
Depois será feito a verificação de data e hora do reconhecimento.
Finalizando com a inclusão do rosto reconhecido no banco de dados Mysql.

# Pré-requisitos

Instale todas as dependências PIP
 - face_recognition
 - cv2
 - datetime
 - numpy

# Instalação

no terminal, escreva:
 -> pip install face_recognition
 -> pip install cv2
 -> pip install datetime
 -> pip install numpy
 
 # Criando Banco de dados
 
 no seu phpMyAdmin, crie seu banco de dados, exemplo:
  -  CREATE DATABASE SeuBancodeDados; (criar seu banco de dados)
  -  USE bancodeteste; (cria seu usuário para acessar o banco de dados)
  -  Vincule o usuário ao banco com todas as permissões
  -  importe o arquivo entradas.sql

 # Pronto, agora é só rodar o código.
