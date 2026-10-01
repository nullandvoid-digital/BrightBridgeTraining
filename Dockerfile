ARG PYTHON_VERSION=3.14-slim

FROM python:${PYTHON_VERSION}

ENV PYTHON_VERSION=3.14 VIRTUAL_ENV=/.venv PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0 UV_PROJECT_ENVIRONMENT=${VIRTUAL_ENV} \
    UV_CACHE_DIR=/opt/uv-cache/ PATH="${VIRTUAL_ENV}/bin:$PATH"
RUN apt update && apt-get install --autoremove -y gcc graphviz graphviz-dev

RUN mkdir -p /code

WORKDIR /code
COPY . /code
RUN pip install uv
COPY pyproject.toml uv.lock /code/
RUN uv sync --locked --no-install-project;

RUN --mount=type=secret,id=SECRET_KEY \
    --mount=type=secret,id=ALLOWED_HOSTS \
    --mount=type=secret,id=INTERNAL_IPS \
    --mount=type=secret,id=DEBUG

ENV ALLOWED_HOSTS="$(cat /run/secrets/ALLOWED_HOSTS)" DEBUG="$(cat /run/secrets/DEBUG)" \
    SECRET_KEY="$(cat /run/secrets/SECRET_KEY)" INTERNAL_IPS="$(cat /run/secrets/ALLOWED_HOSTS)"

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn","--bind","0.0.0.0:8000","--workers","2","brightbridge.wsgi"]
