FROM python:3.8.2-alpine

ADD ./dist/qwazzock-0.1.0-py3-none-any.whl /app/
ADD *.pem /app/
WORKDIR /app
RUN apk add build-base libffi-dev openssl-dev python3-dev
RUN pip install qwazzock-0.1.0-py3-none-any.whl

CMD ["qwazzock"]
EXPOSE 5000/tcp
