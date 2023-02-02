import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá, meu nome é Taiza e estou participando do processo seletivo para o <b>Programa de estágio Talent Lab Itacoatiara - Nível Superior</b> </p>
    
    """

    mensagem = email.message.Message()
    mensagem['Subject'] = "DESAFIO TALENT LAB ITACOATIARA - NÍVEL SUPERIOR"
    mensagem['From'] = 'taizapauladeoliveiralima@gmail.com'
    mensagem['To'] = 'izaridely@gmail.com, alfredobarros@bemol.com.br, juanoliveira@bemol.com.br, emariellealmeida@bemol.com.br'
    senha = 'sylfbzgzghpmrmcw' 
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Credenciais de login para enviar o e-mail
    s.login(mensagem['From'], senha)
    s.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    print('Email enviado')



enviar_email()

