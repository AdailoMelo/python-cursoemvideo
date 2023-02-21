def notas(* n, situacao=False):
    """-> Função para analisar notas e situações de vários alunos.\n:param n: uma ou mais notas dos alunos (aceita várias)\n:param situacao: valor opcional, indicando se deve ou não adicionar a situação\n:return: dicionário com várias informações sobre a situação da turma."""
    soma = cont = 0
    dados = {'Qtd':len(n), 'Maior':max(n), 'Menor':min(n)}
    for pos, i in enumerate(n):
        if pos == 0:
            soma = i
        else:
            soma += i
        cont += 1
    dados['Media'] = soma / cont
    if situacao == True:
        if dados['Media'] >= 7:
            dados['Situação'] = 'BOA'
        elif dados['Media'] > 6 and dados['Media'] < 7:
            dados['Situação'] = 'RAZOAVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados
   
resp = notas(5.5, 9.5, 10, 6.5, situacao=True)        
help(notas)
print(resp)