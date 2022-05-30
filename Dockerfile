FROM ubuntu:latest
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip \
    && \
    apt-get install psmisc && \
    apt-get install sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y openvpn
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
EXPOSE 8999
COPY . /code/
CMD ["python3", "VPNsite/manage.py", "runserver", "0.0.0.0:8999"]
