#Titulo
#Botão iniciar Chat:
  #Clicou apareceu popup / modal
      #titulo: Bem vindo ao Hashzap
      #campo: escreva seu nome
      #botao: entrar no site
#chat
  #campo digite sua mensagem 
  #botao de enviar

# flet -> ajuda a criar um site ou aplicativo (FRAMEWORK DO PYTHON)
# py -m pip install flet

import flet as ft

# função principal do site
def main(pagina):
  texto = ft.Text('Hashzap')

  #chat é uma coluna que pode colocar texto dentro
  chat = ft.Column() 




#sempre que a função for rodada, vai rodar para o tunel de comunicação
  def enviar_mensagem_tunel(mensagem): 
    print(mensagem)

    # adicionar mensagem no chat para TODOS OS USUARIOS

    texto_mensagem = ft.Text(mensagem)#pegando o texto que o usuario digita no campo de mensagem
    chat.controls.append(texto_mensagem) #adicionando NO CHAT
    pagina.update() #usar sempre que fazer uma edição visual

  # criar tunel de comunicação
  pagina.pubsub.subscribe(enviar_mensagem_tunel) 
  #quando mandar mensagem para todos os usuarios, vai acionar essa função enviar_mensagem_tunel




  def enviar_mensagem(evento):
    pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}") #enviar mensagem para todos

    # limpar campo mensagem
    campo_mensagem.value = ""
    pagina.update() #usar sempre que fazer uma edição visual

    

  campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)

  botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

  linha_enviar = ft.Row([campo_mensagem, botao_enviar]) #criada a variavel para o campo de mensagem e o botão enviar ficar na mesma linha




  def entrar_chat(evento):
    #fechar popup
    popup.open =False
    #tirar botão iniciar chat
    pagina.remove(botao_iniciar)
    #tirar titulo
    pagina.remove(texto)
    #criar chat
    pagina.add(chat)
    pagina.pubsub.send_all(f'{nome_usuario.value} entrou no chat')#mostrando para todos que X usuario entrou no chat

    #colocar campo de digitar mensagem
    #criar botao de enviar
    pagina.add(linha_enviar)

    pagina.update()

  titulo_popup = ft.Text('Bem vindo ao Hashzap')
  nome_usuario = ft.TextField(label='Escreva seu nome no chat') #TextField -> campo que o usuario escreve
  botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)

#começa com modal fechado, modaltrue é para centralizar popup
  popup = ft.AlertDialog( open=False,
                          modal=True,
                          title=titulo_popup,
                          content=nome_usuario,
                          actions=[botao_entrar]
  ) #criando popup




  def abrir_popup(evento): #evento de clicar no botao
    pagina.dialog = popup
    popup.open = True #abrindo popup na tela
    pagina.update() # usar sempre que editar a pagina, serve para atualizar a pagina

  botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup) #texto que vai escrito no botão e a função 


  pagina.add(texto) #adicionando texto na pagina
  pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER) #criar o app chamando a função principal
# view=ft.WEB_BROWSER -> tornando codigo em um site