def hello(nome, idade):
    print(f"Ola {nome}!")
    if int(idade) >= 16:
        print("Você pode votar!!!")
    else:
        print("Você não pode votar")   
    print("------------------------")

hello("Vitor", 16)

hello("Maria Eduarda", 15)

hello(idade=30, nome="Joca")