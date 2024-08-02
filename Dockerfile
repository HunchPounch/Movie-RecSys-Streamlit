# Отдельный образ сборки
FROM python:3.10.10 as compile-image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Финальный образ
FROM python:3.10.10
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY recsys_app /app/recsys_app
CMD ["streamlit", "run", "recsys_app/app.py"]