FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-lgsosa.git

WORKDIR /ajedrez-2024-lgsosa

RUN pip install -r requirements.txt

# CMD corregido
CMD ["sh", "-c", "coverage run -m unittest discover -s tests && coverage report -m && python main.py" , "cli.py"]



# docker buildx build -t ajedrez-2024-lgsosa . 
# docker run -i ajedrez-2024-lgsosa