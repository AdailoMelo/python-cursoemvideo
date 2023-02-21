def leiaDinheiro(msg):
    while True:
        din = input(msg).strip()
        verifica = din.replace('.', '')
        verifica = din.replace(',', '')
        if verifica.isnumeric() == True:
            din = din.replace(',','.')
            return float(din)            
        else:
            print('Erro! só serão aceitos valores monetários!')
        

            