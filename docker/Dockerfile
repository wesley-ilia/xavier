# Baixa e usa a Imagem Ubuntu no Dockerhub
FROM python:3.9
# Copia o arquivo start.sh para a pasta root do container
COPY start.sh /root/
# Copia a pasta 42api para dentro do container
RUN mkdir dojos
COPY dojos /dojos/


# Liga o bash para encontrar e executar files no container
ENTRYPOINT bash /root/start.sh

# Roda o container por tempo indeterminado
CMD tail -f /dev/null