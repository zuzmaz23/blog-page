FROM --platform=linux/amd64 python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# Kopiuj requirements najpierw
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Kopiuj CAŁY projekt Django
COPY django_blog/ .

# Utwórz katalogi na pliki statyczne
RUN mkdir -p staticfiles

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]