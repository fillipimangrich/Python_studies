
def notas(*n, sit=False):
    """
    Função para analisar notas e situações de alunos
    parameto n: notas dos alunos(tuple)
    parameto sit: habilita/desbilita a situação (boa: nota maior ou igual a 7, ruim: nota menor que 7)
    return: dicionário contendo as seguintes informações: quantidade de notas, maior e menor nota, media da turma e se habilitado, a situação.

    """
    total = 0
    for i in n:
        total += i 
    dict = {
        'quantidade_notas': len(n),
        'maior_nota': max(n),
        'menor_nota': min(n),
        'media_turma': total/(len(n))
    }
    if sit:
        if dict['media_turma'] < 7:
            dict['situação'] = 'Ruim'
        else:
            dict['situação'] = 'Boa'
    return dict

resp = notas(5,8,8,9,7,sit=True)
help(notas)

print(resp)

        