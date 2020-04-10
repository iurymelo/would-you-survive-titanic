FROM daskdev/dask

COPY . /home/code
WORKDIR /home/code

RUN conda install fastparquet && pip install sklearn

ENTRYPOINT ["python", "training/train.py", "--input", "data_preparation/data/", "-o", "training/data/model"]
