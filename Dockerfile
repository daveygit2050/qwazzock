FROM python:3.8.2-alpine

RUN apk add build-base libffi-dev openssl-dev python3-dev

ARG version
ADD ./dist/qwazzock-$version-py3-none-any.whl /app/
ADD *.pem /app/
WORKDIR /app
RUN pip install qwazzock-$version-py3-none-any.whl

CMD ["qwazzock"]
EXPOSE 5000/tcp
