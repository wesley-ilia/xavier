# Baixa e usa a Imagem python no Dockerhub
FROM python:3.9
# Copia o arquivo start.sh para a pasta root do container
COPY start.sh /root/
# Copia a pasta dojos para dentro do container
RUN mkdir dojos
COPY dojos /dojos/


# Liga o bash para encontrar e executar files no container
ENTRYPOINT bash /root/start.sh
