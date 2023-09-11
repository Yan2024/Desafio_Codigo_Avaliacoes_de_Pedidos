def solution ():
    quantidade_pedidos = int(input())
    notas_por_comida = dict()
    maior_media, quantidade_notas = 0,0

    # Para iterar de acordo com a quantidade de pedidos
    for i in range(quantidade_pedidos):
        avaliacao = input().split()
        
        # Atribuindo uma variável para código e nota a partir de avaliacao
        codigo_comida = int(avaliacao[0])
        nota = int(avaliacao[1])
        
        # Verificar se o código da comida já está no dicionário, se não, adiciona-se como uma nova chave
        if codigo_comida in notas_por_comida:
            notas_por_comida[codigo_comida].append(nota)
        else:
            notas_por_comida[codigo_comida] = [nota]

    # Calcular a média para cada código de comida e imprimir
    for codigo, notas in notas_por_comida.items():
        media = sum(notas) / len(notas)
        print(media)
        if media >= maior_media and len(notas) >= quantidade_notas:
            maior_media = media
            melhor_comida = codigo
            quantidade_notas = len(notas)
    
    # Traz como resultado o código de comida com a maior média
    print(f'O código da comida com maior nota foi {melhor_comida} com a nota média de {maior_media}.')

# Para chamar a função solution()
if __name__ == '__main__':  
    solution()