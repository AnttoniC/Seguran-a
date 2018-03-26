

chave = input("digite a chave: ").upper()
msg = input("Digite a Menssagem: ").upper()

def cript(chave,msg):
    letra = []
    for i in chave:
        letra.append(i)

    cifra = []
    cifra.append(letra[0])
    i = 0
    while i < len(letra):
        y = 0
        while y < len(letra):
            if letra[i] != letra[y]:
                soma = 0
                x = 0
                while x < len(cifra):
                    if letra[y] == cifra[x]:
                        soma += 1
                    x = x + 1
                if soma < 1:
                    cifra.append(letra[y])
            y = 1 + y

        i = 1 + i

    alfa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X",
            "Y", "Z"]

    for i in range(0, len(alfa)):

        for y in range(0, len(cifra)):

            if alfa[i] != cifra[y]:

                soma = 0

                for x in range(0, len(cifra)):

                    if cifra[x] == alfa[i]:
                        soma += 1

                if soma < 1:
                    cifra.append(alfa[i])

    v1=[]
    v2=[]
    v3=[]
    v4=[]
    v5=[]

    for i in range(5):
        v1.append(cifra[i])
        v2.append(cifra[i+5])
        v3.append(cifra[i+10])
        v4.append(cifra[i+15])
        v5.append(cifra[i+20])

    matrix = [v1,v2,v3,v4,v5]
    print("\n",v1,"\n",v2,"\n",v3,"\n",v4,"\n",v5)




    msg1=[]

    for i in msg:
        if (i != " "):
            msg1.append(i)
    #print(msg1)

    dupla = []

    #print(msg1)

    for i in range(len(msg1)-1):
        if (msg1[i] == msg1[i+1]):
            if (msg1[i] != "X"):
                msg1.insert(i+1, "X")
            else:
                msg1.insert(i+1, "Z")
    #print(msg1)


    if ((len(msg1) % 2) != 0):
        if (msg1[len(msg1)-1]) == "Z":
            msg1.append("X")

        elif(msg1[len(msg1)-1]) == "X":
            msg1.append("Z")

    x = 1
    m=""
    for i in msg1:
        m=m+i
        if ((x%2)==0):
            dupla.append(m)
            m=""
        x=x+1


  #print ("-------------")
  #  print (dupla)
  # print ("-------------")


    for i in msg:
        if ((len(msg) % 2) != 0):
            msg=msg+"x"
        if (i != " "):
            dupla.append(i)

    msg2= []

    for i in msg1:
        for l in range(5):
            for c in range(5):
                if (i == matrix[l][c]):
                    msg2.append([l,c])

    aux=0
    for i in range(len(msg2)//2):

        #andar pra direita
        if (msg2[aux][0] == msg2[aux+1][0]):
            if (msg2[aux][1] == 4):
                msg2[aux][1] = 0
                msg2[aux + 1][1] += 1

            elif (msg2[aux+1][1] == 4):
                msg2[aux+1][1] = 0
                msg2[aux][1] += 1

            else:
                msg2[aux][1] += 1
                msg2[aux+1][1] += 1
        #descer
        elif (msg2[aux][1] == msg2[aux+1][1]):
            if (msg2[aux][1] == 4):
                msg2[aux][1] = 0
                msg2[aux + 1][1] += 1

            elif (msg2[aux+1][0] == 4):
                msg2[aux+1][0] = 0
                msg2[aux][0] += 1

            else:
                msg2[aux][0] += 1
                msg2[aux+1][0] += 1
        #inverter as posições
        else:
            ax = msg2[aux][1]
            msg2[aux][1] = msg2[aux+1][1]
            msg2[aux + 1][1] = ax

        aux+=2

    msgC=""
    for i in msg2:
        msgC += matrix[i[0]][i[1]]

    return msgC


    #print(msgC)

    #print("\n",v1,"\n",v2,"\n",v3,"\n",v4,"\n",v5)
    #print(msg2)



#print (cript(chave,msg))


def descri(chave,msg2):
    '''msg2=""
    for i in msg1_c.upper():
        if i != "X" or i != "Z":
            msg2+=i '''
    cifra = []
    for i in chave:
        cifra.append(i)

    alfa = "ABCDEFGHIJLMNOPQRSTUVWXYZ"

    for i in alfa:
        if (i not in cifra):
            cifra.append(i)


    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []

    for i in range(5):
        v1.append(cifra[i])
        v2.append(cifra[i + 5])
        v3.append(cifra[i + 10])
        v4.append(cifra[i + 15])
        v5.append(cifra[i + 20])

    matrix = [v1, v2, v3, v4, v5]

    #print("\n", v1, "\n", v2, "\n", v3, "\n", v4, "\n", v5)

    x = 1
    m = ""
    msg3 = []
    for i in msg2:
        m = m + i
        if ((x % 2) == 0):
            msg3.append(m)
            m = ""
        x = x + 1
   # print(msg3)
    dp = []
    for i in msg3:
        for l in range(5):
            for c in range(5):
                for j in i:
                    if (j == matrix[l][c]):
                        dp.append([l,c])
    #print(dp)
    aux = 0
    for i in range(len(dp) // 2):
        #print(dp[aux][0], dp[aux + 1][0])

        #andar pra esquerda
        if (dp[aux][0] == dp[aux + 1][0]):

            if (dp[aux][1] > 0 and dp[aux][1] > 0 ):
                dp[aux][1] -= 1
                dp[aux + 1][1] -= 1

            elif (dp[aux + 1][1] == 0 and dp[aux][1] > 0):
                dp[aux + 1][1] = 4
                dp[aux][1] -= 1
            elif (dp[aux + 1][1] > 0 and dp[aux][1] == 0):
                dp[aux][1] = 4
                dp[aux + 1][1] -= 1
        #subir
        elif (dp[aux][1] == dp[aux + 1][1]):
            if (dp[aux][0] == 0 and dp[aux + 1][0] > 0):
                dp[aux][0] = 4
                dp[aux + 1][0] -= 1

            elif (dp[aux + 1][0] == 0 and dp[aux][0] > 0):
                dp[aux + 1][0] = 4
                dp[aux][0] -= 1
            elif (dp[aux][0] > 0 and dp[aux + 1][0] > 0):
                dp[aux][0] -= 1
                dp[aux+1][0] -= 1
        #troca as posições
        else:
            ax = dp[aux + 1][0]
            dp[aux + 1][0] = dp[aux][0]
            dp[aux][0] = ax

        aux += 2
    msgD = ""
    for i in dp:
        msgD += matrix[i[0]][i[1]]

    return msgD



#print (cript(chave,msg))
print(descri(chave,msg))