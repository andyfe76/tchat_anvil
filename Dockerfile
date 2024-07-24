FROM python:3.10.13-bullseye

EXPOSE 3030

RUN apt-get update
RUN apt install build-essential zlib1g zlib1g-dev libncurses5-dev libgdbm-dev \
libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev curl wget git -y 

RUN wget -O /tmp/corretto.key https://apt.corretto.aws/corretto.key && \
gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg < /tmp/corretto.key && \
echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | tee /etc/apt/sources.list.d/corretto.list

RUN  apt-get update && apt-get install -y java-1.8.0-amazon-corretto-jdk

RUN pip3 install --upgrade pip && pip3 install wheel && pip3 install anvil-app-server

COPY . /app

CMD anvil-app-server --app app/ --secret api_url=https://tchat_api.lansapp.net