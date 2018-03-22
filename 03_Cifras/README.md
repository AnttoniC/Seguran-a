
## O que foi feito da atividade e o que não foi feito.
Respondemos todas as questões.
## Com quem você fez.
[Antonio Carlos](https://github.com/AnttoniC/Seguranca-da-Informacao)<br>
[Cicero de Oliveira](https://github.com/cicerooli)<br>

## Como vocês dividiram/fizeram a atividade.
Dividimos 4 questões pra cada um, no meu caso eu pesquisei as primeiras quatro questões.
## O que você aprendeu e o que ainda tem dificuldade.
Aprendi muito coisa pois já tinha ouvido falar em algumas coisa e não sabia o que eram,da questão 5 emdiante eu nunca tinha ouvido falar sobre essas siglas.

## Quanto tempo você gastou no total na atividade.
Basicamente a aula quase toda. 
<br>
<br>
# RESPOSTAS
<br>

## 1 - O que são chaves simetrica e assimetrica?<br>
**Simétrica**
A criptografia simétrica é também conhecida por criptografia de chave secreta.
Algoritmos que usam criptografia simétrica tendem a ser mais rápidos, 
no entanto não são tão seguros como os que usam criptografia assimétrica,
uma vez que a chave usada para cifrar a informação é partilhada entre as várias máquinas.<br>
**Assimétrica**
A criptografia assimétrica é também conhecida por criptografia de chave pública.
Em comparação com a criptografia simétrica, a criptografia assimétrica tende a ser 
mais lenta e necessita de um maior poder computacional por parte das máquinas.
No entanto, este é um excelente método para garantir segurança num canal público e inseguro (ex. Internet). <br>

## 2 - Quais são as diferenças? 
**Chave Simétrica**
É usada uma única chave que é partilhada entre o emissor e o receptor. Desta forma, a chave que é usada para cifrar é a mesma que é usada para decifrar.<br>
**Chave Assimétrica**
Usam um par de chaves distintas (chave privada e chave pública)
A chave pública é usada para cifrar (encriptar)
A chave privada é usada para decifrar (desencriptar)<br>

## 3 - Dê exemplos reais de algoritmo. 
DES , 3DES , AES e RC4 são alguns dos algoritmos que usam criptografia simétrica.<br>
Assimétrica RSA<br> 

## 4 - Dê exemplo de onde elas são usadas em conjunto. 

Os algoritmos de criptografia podem ser utilizados em conjunto para tornar vários processos de análise de dados e troca de informações mais seguros. Assim, o ciframento de mensagens, a verificação de identidades e a otimização de assinaturas digitais torna-se mais ágil e poderosa.

## 5 - O que é KDC? 
 O KDC ( Centro Distribuidor de Chaves ) trata-se de um servidor centralizado também responsável pela autenticação dos usuários. O KDC autentica o usuário,  destinado a reduzir os riscos inerentes à troca de chaves. Os KDCs geralmente operam em sistemas nos quais alguns usuários podem ter permissão para usar certos serviços em algumas ocasiões e não em outros.<br>

Exemplo: ao receber de uma máquina cliente uma requisição por um ticket, o KDC cria o chamado Ticket Granting Ticket (TGT), o criptografa utilizando a senha secreta do usuário, criando a chamada chave secreta, e o envia para o cliente que fez a solicitação. O processo de autenticação inicia-se com um pedido do cliente a este servidor central, o KDC, onde estão registradas as chaves secretas dos usuários.<br>

## 6 - Como funciona o GPG? 
GPG ou Gnu Private Guard é uma ferramenta pra comunicação segura.<br>
Além de encriptar mensagens inteiras, o GPG permite que você “assine” digitalmente as assinaturas. Usadas desta forma, as mensagens podem ser lidas por recipientes que carecem do software GPG ou chaves apropriadas; mas, aqueles que tiverem estas ferramentas podem verificar que os conteúdos não foram cuidados. <br>

1- Criação do seu par de chaves (uma pública e uma secreta)<br>
2-Publicação da sua chave pública — lembre-se: sua chave secreta deve permanecer absolutamente secreta<br>
3-Divulgação da sua chave pública<br>
4- Importação da chave de um(a) amigo(a) para prosseguir à...<br>
5-Criptografia de um arquivo com a chave pública do destinatário<br>
6-Decifragem de um arquivo criptografado com a sua chave pública<br>

## 7 - O que é um ICP?
A sigla ICP vem de ICP-Brasil, que significa Infraestrutura de Chaves Públicas
é necessário o uso de um Certificado Digital, totalmente criptografado, impossibilitando a alteração do documento por terceiros. Ou seja, o Conectividade Social ICP agora é muito mais seguro utilizando seu Certificado Digital.

## 8 - Porque dá erro de cerficifado em alguns site inclusive no site da caixa?
O certificado não é considerado confiável porque o certificado do expedidor não é considerado confiável.
