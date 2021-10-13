def batalhar(escolha1, escolha2):
    if escolha1 == escolha2:
        return 'nenhum'
    if escolha1 == 'c':
        if escolha2 == 'java':
            return escolha2
        return escolha1
    if escolha1 == 'py':
        if escolha2 == 'c':
            return escolha2
        return escolha1
    if escolha1 == 'java':
        if escolha2 == 'py':
            return 'py'
        return 'java'
    return "ERROR"
