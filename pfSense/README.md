# Prática pfSense
## Bloqueio de Torrent
<br>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/pfsense.png)

## Equipe
[Antonio Carlos](https://github.com/AnttoniC/Seguranca-da-Informacao)<br>
[Samuel Brandão](https://github.com/SamuelBrandao08/Seguranca)

## Sobre pfSense:

PfSense é um sistema operacional de código aberto usado para transformar o computador em um
firewall, roteador. PfSense é uma distribuição FreeBSD feita com base no projeto m0n0wall, uma distribuição
de firewall poderoso e leve. PfSense se baseia basicamente em m0n0wall e toma decisões de todas as suas
funções, e foi adicionado mais uma variedade de serviços de rede mais usadas.

## Principais vantagens e os recursos do pfSense:
Primeiramente, uma das principais vantagens é a sua licença BSD — licença de código aberto, gratuita, utilizada em sistemas baseados em Unix. Esse tipo de licença permite que o pfSense seja customizado de acordo com as maiores necessidades da empresa.

Um fator que auxilia na customização é a imensa variedade de pacotes de software, muitos deles criados por especialistas da comunidade de desenvolvedores para acrescentar novas funcionalidades.

Na linguagem dos especialistas em Segurança da Informação, a disponibilização dos pacotes para as mais diversas funções credencia o pfSense como um UTM (Unified Threat Management, ou Central Unificada de Gerenciamento de Ameaças, em português), que, em breves palavras, pode ser entendido por um dispositivo com diversas funções, tais como:

firewall;<br>
servidor (internet, DHCP, NTP, Proxy…);<br>
antivírus;<br>
antispyware;<br>
antispam;<br>
filtragem de conteúdo;<br>
detecção de intrusão, entre outros.

# Instalando o pfSense

## Requisitos mínimos do sistema:

CPU:                             Pelo menos 100 MHz<br>
RAM:                             128 MB<br>
A instalação no disco rígido:	   1 GB<br>
Incorporado:                     Compact Flash de 512 MB

## Etapa 1 - Preparando o Ambiente:

<strong>O ambiente que iremos proporcionar nesse tutorial sera o seguinte:</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/Ambiente%20Pfsense.png)


<strong>Primeiramente devemos preparar a maquina Virtual com duas plcas de redes uma no modo NAT e outra como modo Interna.</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P13.png)
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P15.png)
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P14.png)

## Etapa 2 - Iniciando a instalação:
<br>

<strong>Tela inical de Boas Vindas do Sistema:</strong>
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P00.png)


<strong>Na tela de auto boot aperta a letra "i" para iniciar a instalação.</strong>
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P1.png)

<strong>Seleciona: Accept these Settings</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P2.png)

<strong>Seleciona: Quick/Easy Install</strong>
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P3.png)

<strong>Seleciona: OK</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P4.png)

<strong>Seleciona: Standard Kernel</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P5.png)

<strong>Seleciona: Reboot</strong><br>
Quando o sitema tiver reiniciando remova o disco ou se preferir desligue a maquina e remova o disco.

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P6.png)

<strong>Seleciona: F1</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/P7.png)


<strong>Tela inicial do sistema:</strong><br>
Na tela inicial vemos as duas interfaces WAN e LAN e vemos um menu com várias opções.<br>
Para podermos acessar a interface grafica devemos executar o comando `pfctl -d` para poder disabilitar o firewall e
`pfctl -e` para habilitar. Digitamos `8` para entramos no shell do pfsense e executamos.

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/A5.png)


## Etapa 3 - Acessar o gerenciadorWeb:

Acessaremos a interface pelo ip da `LAN` que no caso vai ser o ip `192.168.1.1` que é o que vem por padrão.
Nessa etapa só iremos mudar o que está sugerido a seguir no restante e só next.


<strong>Selecione a Timezone: América/São Paulo clicamos em next.</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/A1.jpg)

<strong>Selecione: DHCP e clicamos em next</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/A2.jpg)

<strong>Selecione: reload</strong> <br>
Obs:caso não carregue execute o comando `pfctl-d` no pfsense.

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/A2.jpg)

## Etapa 4 - Configurando as regras do firewall:
Veja como usar,criar,editar e excluir Alias. O Alias fornece um grau de separação entre as regras e valores que podem mudar no futuro (por exemplo, endereços de IP,portas, entre outros). O uso do Alias vai ser fundamental nessa prática.
Iremmos configurar as regras de acesso para `LAN` que é a nossa rede interna,vamos realizar as
configurações a seguir.

<strong>Regras do Firewall que vem como padrão:</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/pad.png)

<strong>Vamos acessar `Firewall\Aliases\Ports` onde vamos fazer as seguintes alterações:</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/cap1.png)

<strong> Agora iremos em `Firewall\Rules\LAN` onde vamos adicionar uma nova regra:</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/ace1.png)<br>
![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/ace2.png)


<strong>E por ultimo iremos desativar as duas regras que vem como padrão,vamos deixar ativo só a nova regra:</strong>

![img](https://github.com/AnttoniC/Seguranca-da-Informacao/blob/master/pfSense/img/ace3.png)


