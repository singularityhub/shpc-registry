---
layout: container
name:  "quay.io/biocontainers/corgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/corgi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/corgi/container.yaml"
updated_at: "2024-08-23 02:56:26.779576"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/corgi"
aliases:
 - "alembic"
 - "celery"
 - "configure_accelerate"
 - "cookiecutter"
 - "corgi"
 - "corgi-train"
 - "databricks"
 - "dbfs"
 - "gunicorn"
 - "mlflow"
 - "optuna"
 - "pathy"
 - "pyaml"
 - "pybtex"
 - "pybtex-convert"
 - "pybtex-format"
 - "shortuuid"
 - "slugify"
 - "spacy"
 - "sqlformat"
 - "termgraph"
 - "torchapp"
 - "torchapp-imageclassifier"
 - "wandb"
 - "wb"
 - "weasel"
 - "wsdump"
 - "httpx"
 - "pbr"
 - "produce_x_platform_fuzz_corpus"
 - "run_x_platform_fuzz_corpus"
 - "isympy"
 - "torchrun"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "plasma-store-server"
 - "plasma_store"
 - "mako-render"
 - "csv-import"
 - "markdown-it"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "sha256_profile"
 - "h5delete"
 - "gflags_completions.sh"
versions:
 - "0.4.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for corgi"
config: {"url": "https://biocontainers.pro/tools/corgi", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for corgi", "latest": {"0.4.0--pyhdfd78af_0": "sha256:b3ae3f99aea81fa72782d07dac31a8b05ce4315179e3d75e6fe1057c5dc38309"}, "tags": {"0.4.0--pyhdfd78af_0": "sha256:b3ae3f99aea81fa72782d07dac31a8b05ce4315179e3d75e6fe1057c5dc38309"}, "docker": "quay.io/biocontainers/corgi", "aliases": {"alembic": "/usr/local/bin/alembic", "celery": "/usr/local/bin/celery", "configure_accelerate": "/usr/local/bin/configure_accelerate", "cookiecutter": "/usr/local/bin/cookiecutter", "corgi": "/usr/local/bin/corgi", "corgi-train": "/usr/local/bin/corgi-train", "databricks": "/usr/local/bin/databricks", "dbfs": "/usr/local/bin/dbfs", "gunicorn": "/usr/local/bin/gunicorn", "mlflow": "/usr/local/bin/mlflow", "optuna": "/usr/local/bin/optuna", "pathy": "/usr/local/bin/pathy", "pyaml": "/usr/local/bin/pyaml", "pybtex": "/usr/local/bin/pybtex", "pybtex-convert": "/usr/local/bin/pybtex-convert", "pybtex-format": "/usr/local/bin/pybtex-format", "shortuuid": "/usr/local/bin/shortuuid", "slugify": "/usr/local/bin/slugify", "spacy": "/usr/local/bin/spacy", "sqlformat": "/usr/local/bin/sqlformat", "termgraph": "/usr/local/bin/termgraph", "torchapp": "/usr/local/bin/torchapp", "torchapp-imageclassifier": "/usr/local/bin/torchapp-imageclassifier", "wandb": "/usr/local/bin/wandb", "wb": "/usr/local/bin/wb", "weasel": "/usr/local/bin/weasel", "wsdump": "/usr/local/bin/wsdump", "httpx": "/usr/local/bin/httpx", "pbr": "/usr/local/bin/pbr", "produce_x_platform_fuzz_corpus": "/usr/local/bin/produce_x_platform_fuzz_corpus", "run_x_platform_fuzz_corpus": "/usr/local/bin/run_x_platform_fuzz_corpus", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "mako-render": "/usr/local/bin/mako-render", "csv-import": "/usr/local/bin/csv-import", "markdown-it": "/usr/local/bin/markdown-it", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "sha256_profile": "/usr/local/bin/sha256_profile", "h5delete": "/usr/local/bin/h5delete", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/corgi.
singularity registry hpc automated addition for corgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/corgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/corgi:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/corgi/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/corgi/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### corgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### corgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### corgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### corgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### corgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### corgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### celery

```bash
$ singularity exec <container> /usr/local/bin/celery
$ podman run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### configure_accelerate

```bash
$ singularity exec <container> /usr/local/bin/configure_accelerate
$ podman run --it --rm --entrypoint /usr/local/bin/configure_accelerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configure_accelerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corgi

```bash
$ singularity exec <container> /usr/local/bin/corgi
$ podman run --it --rm --entrypoint /usr/local/bin/corgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corgi-train

```bash
$ singularity exec <container> /usr/local/bin/corgi-train
$ podman run --it --rm --entrypoint /usr/local/bin/corgi-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corgi-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### databricks

```bash
$ singularity exec <container> /usr/local/bin/databricks
$ podman run --it --rm --entrypoint /usr/local/bin/databricks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/databricks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbfs

```bash
$ singularity exec <container> /usr/local/bin/dbfs
$ podman run --it --rm --entrypoint /usr/local/bin/dbfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunicorn

```bash
$ singularity exec <container> /usr/local/bin/gunicorn
$ podman run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlflow

```bash
$ singularity exec <container> /usr/local/bin/mlflow
$ podman run --it --rm --entrypoint /usr/local/bin/mlflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### optuna

```bash
$ singularity exec <container> /usr/local/bin/optuna
$ podman run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/optuna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathy

```bash
$ singularity exec <container> /usr/local/bin/pathy
$ podman run --it --rm --entrypoint /usr/local/bin/pathy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyaml

```bash
$ singularity exec <container> /usr/local/bin/pyaml
$ podman run --it --rm --entrypoint /usr/local/bin/pyaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybtex

```bash
$ singularity exec <container> /usr/local/bin/pybtex
$ podman run --it --rm --entrypoint /usr/local/bin/pybtex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybtex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybtex-convert

```bash
$ singularity exec <container> /usr/local/bin/pybtex-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pybtex-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybtex-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybtex-format

```bash
$ singularity exec <container> /usr/local/bin/pybtex-format
$ podman run --it --rm --entrypoint /usr/local/bin/pybtex-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybtex-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shortuuid

```bash
$ singularity exec <container> /usr/local/bin/shortuuid
$ podman run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spacy

```bash
$ singularity exec <container> /usr/local/bin/spacy
$ podman run --it --rm --entrypoint /usr/local/bin/spacy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spacy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqlformat

```bash
$ singularity exec <container> /usr/local/bin/sqlformat
$ podman run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### termgraph

```bash
$ singularity exec <container> /usr/local/bin/termgraph
$ podman run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/termgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchapp

```bash
$ singularity exec <container> /usr/local/bin/torchapp
$ podman run --it --rm --entrypoint /usr/local/bin/torchapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchapp-imageclassifier

```bash
$ singularity exec <container> /usr/local/bin/torchapp-imageclassifier
$ podman run --it --rm --entrypoint /usr/local/bin/torchapp-imageclassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchapp-imageclassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wandb

```bash
$ singularity exec <container> /usr/local/bin/wandb
$ podman run --it --rm --entrypoint /usr/local/bin/wandb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wandb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wb

```bash
$ singularity exec <container> /usr/local/bin/wb
$ podman run --it --rm --entrypoint /usr/local/bin/wb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weasel

```bash
$ singularity exec <container> /usr/local/bin/weasel
$ podman run --it --rm --entrypoint /usr/local/bin/weasel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weasel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbr

```bash
$ singularity exec <container> /usr/local/bin/pbr
$ podman run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### produce_x_platform_fuzz_corpus

```bash
$ singularity exec <container> /usr/local/bin/produce_x_platform_fuzz_corpus
$ podman run --it --rm --entrypoint /usr/local/bin/produce_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/produce_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_x_platform_fuzz_corpus

```bash
$ singularity exec <container> /usr/local/bin/run_x_platform_fuzz_corpus
$ podman run --it --rm --entrypoint /usr/local/bin/run_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_x_platform_fuzz_corpus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)