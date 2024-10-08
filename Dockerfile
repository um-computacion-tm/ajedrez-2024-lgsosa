FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-lgsosa ajedrez

WORKDIR /ajedrez

RUN pip install -r requirements.txt

# CMD corregido
CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && echo 'Press any key to continue...' && read -n 1 && python3 -m ajedrez.cli"]

# docker buildx build -t ajedrez-2024-lgsosa . 
# docker run -i ajedrez-2024-lgsosa