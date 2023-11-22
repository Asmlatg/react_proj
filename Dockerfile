FROM ubuntu:18.04

WORKDIR /myproject/

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev 
COPY ./req.txt ./

RUN pip3 install -r req.txt

COPY . ./

ENTRYPOINT [ "python3" ]

CMD [ "traducteur.py" ]