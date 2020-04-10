FROM daskdev/dask

COPY . /home/code
WORKDIR /home/code

RUN conda install fastparquet

ENTRYPOINT ["python", "data_preparation/data_wrangling.py", "--input", "data_preparation/data/titanic.csv", "--output", "data_preparation/data/"]
