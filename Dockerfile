FROM python:3.11.9-slim

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/program/requirements.txt
WORKDIR /opt/program/
    
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
    
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

#------------------------------------------------
# RUN mkdir -p /opt/ml/input/data/dataset
# RUN mkdir -p /opt/ml/input/data/model
# RUN mkdir -p /opt/ml/input/config
# RUN mkdir -p /opt/ml/output/data
# RUN mkdir -p /opt/ml/model

# COPY iris.csv /opt/ml/input/data/dataset/iris.csv
# COPY decision-tree-model.pkl /opt/ml/model/decision-tree-model.pkl
# COPY model.tar.gz /opt/ml/input/data/model/model.tar.gz
# COPY hyperparameters.json /opt/ml/input/config/hyperparameters.json
#------------------------------------------------

COPY program /opt/program

