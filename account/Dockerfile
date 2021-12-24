FROM python:3.10

ENV WORKDIR=/opt/account

ADD requirements.txt $WORKDIR/requirements.txt
RUN pip install -r $WORKDIR/requirements.txt

ADD . $WORKDIR
WORKDIR $WORKDIR
RUN mkdir -p db
EXPOSE 8000

CMD ["bash", "entrypoint.sh"]
