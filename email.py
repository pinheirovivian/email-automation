from email.message import EmailMessage
import ssl
import smtplib

meu_email = "" # seu email aqui
senha_gerada = "" # sua senha aqui ou gere uma no gmail
destinatario_email = "" # email do destinatario
assunto = "Testando Python" # escreva o assunto
body = """
Teste
""" # a mensagem do email
em = EmailMessage()

em['From'] = meu_email
em['To'] = destinatario_email
em['subject'] = assunto
em.set_content(body)

context = ssl.create_default_context() # criando um contexto SSL segur

# SMTP é o protocolo que permite enviar emails pela internet
# fazendo conexão com o servidor SMTP do Gmail usando SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha_gerada) # fazendo seu login
    smtp.sendmail(meu_email, destinatario_email, em.as_string()) # enviando o email