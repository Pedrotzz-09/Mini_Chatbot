nome = input('Qual é o seu nome?')
print("É um prazer te conhecer{}, seu nome é muito bonito!".format(nome))
idade = int(input('Bom, qual é a sua idade?'))
if idade == 20:
  print('Nossa, você tem a minha idade,{}!'.format(nome))
elif idade > 20:
  print('Caramba, sou mais novo que você!')
else:
  print('Sou mais velho que você!')
print('Bem, foi legal conversar com você{}, espero que possamos nos falar novamente, até logo!'.format(nome))