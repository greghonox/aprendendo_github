with open('tabuada.txt', 'w') as arq:
    for i in range(11):
        for ii in range(11):
            arq.write(f"{i} * {ii} = {ii*i}\n")
        arq.write("-"*20 + '\n')
        
