# Estrutura: LISTA
playlist = ["Música A", "Música B", "Música C", "Música D", "Música E"]

while True:
    print("\n=== Menu ===")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Exibir")
    print("0 - Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        musica = input("Música: ")
        playlist.append(musica)
    elif opcao == "2":
        musica = input("Música a remover: ")
        if musica in playlist:
            playlist.remove(musica)
        else:
            print("Música não encontrada.")
    elif opcao == "3":
        for i, musica in enumerate(playlist, start=1):
            print(f"{i} - {musica}")
    elif opcao == "0":
        break