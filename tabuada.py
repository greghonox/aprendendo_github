with open('tabuada.txt', 'w') as arq:
    for i in range(10):
        for ii in range(10):
            arq.write(f"{i} * {ii} = {ii*i}\n")
        arq.write("-"*20 + '\n')
        
