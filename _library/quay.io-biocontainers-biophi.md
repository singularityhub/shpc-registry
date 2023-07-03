---
layout: container
name:  "quay.io/biocontainers/biophi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biophi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biophi/container.yaml"
updated_at: "2023-07-03 03:02:05.861353"
latest: "1.0.9--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/biophi"
aliases:
 - "ANARCI"
 - "biophi"
 - "celery"
 - "fairseq-eval-lm"
 - "fairseq-generate"
 - "fairseq-interactive"
 - "fairseq-preprocess"
 - "fairseq-score"
 - "fairseq-train"
 - "fairseq-validate"
 - "sacrebleu"
 - "sapiens"
 - "torchrun"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "vba_extract.py"
 - "flask"
 - "tabulate"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "hmmpgmd_shard"
versions:
 - "1.0.5--pyhdfd78af_0"
 - "1.0.6--pyhdfd78af_0"
 - "1.0.7--pyhdfd78af_0"
 - "1.0.8--pyhdfd78af_1"
 - "1.0.9--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for biophi"
config: {"url": "https://biocontainers.pro/tools/biophi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biophi", "latest": {"1.0.9--pyhdfd78af_1": "sha256:00e0f28531ad0a50b89281fcfea418deeb8f18ee68d4a2c80908a15b3f6a9292"}, "tags": {"1.0.5--pyhdfd78af_0": "sha256:19d21733389ffcc3b7d8eefb06f1aae5703fd5d594f561079d0bdb30ca6d1531", "1.0.6--pyhdfd78af_0": "sha256:e5d36d76b583fb449ed30e93960294256b5c3bc7562054d6826c0e738aee7742", "1.0.7--pyhdfd78af_0": "sha256:b7e00a9bdcb1fc53988972bf30896fc79f377be05a8a2a6c84aeb771eea9b74b", "1.0.8--pyhdfd78af_1": "sha256:af2fd6993e725e0c208eb41a678c041834dee20f030abba79ced527d9345e480", "1.0.9--pyhdfd78af_1": "sha256:00e0f28531ad0a50b89281fcfea418deeb8f18ee68d4a2c80908a15b3f6a9292"}, "docker": "quay.io/biocontainers/biophi", "aliases": {"ANARCI": "/usr/local/bin/ANARCI", "biophi": "/usr/local/bin/biophi", "celery": "/usr/local/bin/celery", "fairseq-eval-lm": "/usr/local/bin/fairseq-eval-lm", "fairseq-generate": "/usr/local/bin/fairseq-generate", "fairseq-interactive": "/usr/local/bin/fairseq-interactive", "fairseq-preprocess": "/usr/local/bin/fairseq-preprocess", "fairseq-score": "/usr/local/bin/fairseq-score", "fairseq-train": "/usr/local/bin/fairseq-train", "fairseq-validate": "/usr/local/bin/fairseq-validate", "sacrebleu": "/usr/local/bin/sacrebleu", "sapiens": "/usr/local/bin/sapiens", "torchrun": "/usr/local/bin/torchrun", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "vba_extract.py": "/usr/local/bin/vba_extract.py", "flask": "/usr/local/bin/flask", "tabulate": "/usr/local/bin/tabulate", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biophi.
shpc-registry automated BioContainers addition for biophi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biophi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biophi:1.0.9--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biophi/1.0.9--pyhdfd78af_1
$ module help quay.io/biocontainers/biophi/1.0.9--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biophi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biophi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biophi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biophi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biophi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biophi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ANARCI

```bash
$ singularity exec <container> /usr/local/bin/ANARCI
$ podman run --it --rm --entrypoint /usr/local/bin/ANARCI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ANARCI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biophi

```bash
$ singularity exec <container> /usr/local/bin/biophi
$ podman run --it --rm --entrypoint /usr/local/bin/biophi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biophi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### celery

```bash
$ singularity exec <container> /usr/local/bin/celery
$ podman run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/celery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-eval-lm

```bash
$ singularity exec <container> /usr/local/bin/fairseq-eval-lm
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-eval-lm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-eval-lm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-generate

```bash
$ singularity exec <container> /usr/local/bin/fairseq-generate
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-interactive

```bash
$ singularity exec <container> /usr/local/bin/fairseq-interactive
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-interactive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-interactive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-preprocess

```bash
$ singularity exec <container> /usr/local/bin/fairseq-preprocess
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-score

```bash
$ singularity exec <container> /usr/local/bin/fairseq-score
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-train

```bash
$ singularity exec <container> /usr/local/bin/fairseq-train
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fairseq-validate

```bash
$ singularity exec <container> /usr/local/bin/fairseq-validate
$ podman run --it --rm --entrypoint /usr/local/bin/fairseq-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fairseq-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sacrebleu

```bash
$ singularity exec <container> /usr/local/bin/sacrebleu
$ podman run --it --rm --entrypoint /usr/local/bin/sacrebleu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sacrebleu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sapiens

```bash
$ singularity exec <container> /usr/local/bin/sapiens
$ podman run --it --rm --entrypoint /usr/local/bin/sapiens   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sapiens   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
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