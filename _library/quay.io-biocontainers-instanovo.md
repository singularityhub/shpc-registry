---
layout: container
name:  "quay.io/biocontainers/instanovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/instanovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/instanovo/container.yaml"
updated_at: "2025-09-11 03:23:51.594271"
latest: "1.1.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/instanovo"
aliases:
 - "datasets-cli"
 - "dotenv"
 - "huggingface-cli"
 - "jiwer"
 - "neptune"
 - "pygrun"
 - "x86_64-conda-linux-gnu.cfg"
 - "jsonpointer"
 - "torch_shm_manager"
 - "wsdump"
 - "get_gprof"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "protoc-25.3.0"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "xxhsum"
 - "dumpsexp"
 - "gpg-error"
 - "gpgrt-config"
 - "hmac256"
 - "mpicalc"
 - "yat2m"
versions:
 - "1.0.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for instanovo"
config: {"url": "https://biocontainers.pro/tools/instanovo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for instanovo", "latest": {"1.1.4--pyhdfd78af_0": "sha256:eb2f00aef90f8e17cfb2923938781a83b147e545160051dd1cb477bf5d10c7fc"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:e28eabae0be906b7bdf48335d561023d6ced5c332be9913e3ed0b0b3659f69e4", "1.1.1--pyhdfd78af_0": "sha256:9f16d2bddaf23f5d50ffcc27e36286af5d569bea8742e4f095748c7ac630a556", "1.1.2--pyhdfd78af_0": "sha256:f5f93712066ca1b9716dc0867881b3af60e90698a293d6a6614a2565a6b830c5", "1.1.4--pyhdfd78af_0": "sha256:eb2f00aef90f8e17cfb2923938781a83b147e545160051dd1cb477bf5d10c7fc"}, "docker": "quay.io/biocontainers/instanovo", "aliases": {"datasets-cli": "/usr/local/bin/datasets-cli", "dotenv": "/usr/local/bin/dotenv", "huggingface-cli": "/usr/local/bin/huggingface-cli", "jiwer": "/usr/local/bin/jiwer", "neptune": "/usr/local/bin/neptune", "pygrun": "/usr/local/bin/pygrun", "x86_64-conda-linux-gnu.cfg": "/usr/local/bin/x86_64-conda-linux-gnu.cfg", "jsonpointer": "/usr/local/bin/jsonpointer", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "wsdump": "/usr/local/bin/wsdump", "get_gprof": "/usr/local/bin/get_gprof", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "xxhsum": "/usr/local/bin/xxhsum", "dumpsexp": "/usr/local/bin/dumpsexp", "gpg-error": "/usr/local/bin/gpg-error", "gpgrt-config": "/usr/local/bin/gpgrt-config", "hmac256": "/usr/local/bin/hmac256", "mpicalc": "/usr/local/bin/mpicalc", "yat2m": "/usr/local/bin/yat2m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/instanovo.
singularity registry hpc automated addition for instanovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/instanovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/instanovo:1.1.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/instanovo/1.1.4--pyhdfd78af_0
$ module help quay.io/biocontainers/instanovo/1.1.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### instanovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### instanovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### instanovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### instanovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### instanovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### instanovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jiwer

```bash
$ singularity exec <container> /usr/local/bin/jiwer
$ podman run --it --rm --entrypoint /usr/local/bin/jiwer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jiwer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neptune

```bash
$ singularity exec <container> /usr/local/bin/neptune
$ podman run --it --rm --entrypoint /usr/local/bin/neptune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neptune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygrun

```bash
$ singularity exec <container> /usr/local/bin/pygrun
$ podman run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123

```bash
$ singularity exec <container> /usr/local/bin/mpg123
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-id3dump

```bash
$ singularity exec <container> /usr/local/bin/mpg123-id3dump
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-strip

```bash
$ singularity exec <container> /usr/local/bin/mpg123-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### out123

```bash
$ singularity exec <container> /usr/local/bin/out123
$ podman run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsexp

```bash
$ singularity exec <container> /usr/local/bin/dumpsexp
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-error

```bash
$ singularity exec <container> /usr/local/bin/gpg-error
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgrt-config

```bash
$ singularity exec <container> /usr/local/bin/gpgrt-config
$ podman run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmac256

```bash
$ singularity exec <container> /usr/local/bin/hmac256
$ podman run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicalc

```bash
$ singularity exec <container> /usr/local/bin/mpicalc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yat2m

```bash
$ singularity exec <container> /usr/local/bin/yat2m
$ podman run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
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