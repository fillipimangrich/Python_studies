def voto(nascimento):
    from datetime import date
    n= date.today().year
    idade = n - nascimento
    if idade < 16:
        return f'Com {idade} anos: Não pode votar!'
        
    elif (idade >= 16 and idade < 18) or idade > 65:
        return f'Com {idade} anos: Seu voto é opcional!'
         
    else:
        return f'Com {idade} anos: Seu voto é obrigatório!'
nascimento = (int(input('Digite o ano de nascimento:')))
print(voto(nascimento))
