## Copia a iso do ssh do darlon:
- (comando usado de dentro do maquina normal)
```
docker pull darlon/ssh 
```
## Cria um servidor ssh rodando na maquina:
- (comando usado de dentro do maquina normal)
```
docker run --rm -d --name ssh -p 2222:22 darlon/ssh 
```
## Verifica se o servidor ssh esta rodando:
- (comando usado de dentro da servidor ssh)
```
docker ps
```
## Entra dentro do servidor ssh:
- (comando usado de dentro do servidor ssh)
```
ssh -p 2222 samu@localhost
```
## Coloca o arquivo dentro do servidor ssh:
- (comando usado de dentro da maquina normal)
```
scp -P 2222 /home/aluno/redes/hehe.jpg samu@localhost:/tmp/
```
## Mostra os arquivos existentes dentro do tmp:
- (comando usado de dentro do servidor ssh)
```
ls /tmp 
```
## Copia o arquivo dentro de um ssh para outro ssh:
- (comando usado de dentro do servidor ssh)
```
scp -P 2222 /tmp/hehe.jpg samu@192.168.246.55:/tmp/hehe.jpg 
```
## Faz download de um arquivo dentro de um servidor ssh:
- (comando usado de dentro do maquina normal)
```
scp -P 2222 samu@192.168.246.60:/tmp/mosquito.jpg . 
```
