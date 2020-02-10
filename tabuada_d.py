with open('tabuada_d.txt', 'w') as arq:
    for i in range(1, 10):
        for ii in range(1, 10):
            arq.write(f'{i} / {ii} = {i / ii} \n')
        arq.write('---' * 10 + '\n')


