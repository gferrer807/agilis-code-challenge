FROM lambci/lambda:build-python3.6

ENV AWS_DEFAULT_REGION us-east-1

COPY . .

RUN zip -9yr lambda.zip .

CMD aws lambda update-function-code --function-name agilis --zip-file fileb://lambda.zip