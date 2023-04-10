## Puxa os arquivos do ssh do darlon:
```
docker pull darlon/ssh 
```
## Cria um servidor ssh rodando na maquina:
```
docker run --rm -d --name ssh -p 2222:22 darlon/ssh 
```
## Verifica se o servidor ssh esta rodando:
```
docker ps
```
## Entra dentro do servidor ssh:
```
ssh -p 2222 samu@localhost
```
## Coloca o arquivo dentro do servidor ssh:
```
scp -P 2222 /home/aluno/redes/hehe.jpg samu@localhost:/tmp/
```
## Mostra os arquivos existentes dentro do tmp:
```
ls /tmp 
```
## Copia o arquivo dentro de um ssh para outro ssh:
```
scp -P 2222 /tmp/hehe.jpg samu@192.168.246.55:/tmp/hehe.jpg 
```
## (dentro da maquina pc) Faz download de um arquivo dentro de um servidor ssh:
```
scp -P 2222 samu@192.168.246.60:/tmp/mosquito.jpg . 
```
