def verificar_idade(idade, nome):
    if idade >= 18:
        return f"{nome} é maior de idade"
    else:
        return f"{idade}é menor de idade"
    
print(verificar_idade("Vitor", 16))