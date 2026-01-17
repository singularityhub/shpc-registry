---
layout: container
name:  "quay.io/biocontainers/unicore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unicore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unicore/container.yaml"
updated_at: "2026-01-17 03:30:54.751778"
latest: "1.1.1--h7ef3eeb_0"
container_url: "https://biocontainers.pro/tools/unicore"
aliases:
 - "checksum-profile"
 - "datasets-cli"
 - "elastishadow"
 - "foldmason"
 - "foldseek"
 - "gawk-5.3.1"
 - "huggingface-cli"
 - "protoc-28.2.0"
 - "spm_decode"
 - "spm_encode"
 - "spm_export_vocab"
 - "spm_normalize"
 - "spm_train"
 - "torchfrtrace"
 - "transformers-cli"
 - "unicore"
 - "torch_shm_manager"
 - "get_gprof"
 - "iqtree2"
 - "aria2c"
 - "iqtree"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "gawkbug"
 - "xxhsum"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "isympy"
 - "torchrun"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
versions:
 - "1.0.1--h7ef3eeb_0"
 - "1.0.2--h7ef3eeb_0"
 - "1.1.0--h7ef3eeb_0"
 - "1.1.1--h7ef3eeb_0"
description: "singularity registry hpc automated addition for unicore"
config: {"url": "https://biocontainers.pro/tools/unicore", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unicore", "latest": {"1.1.1--h7ef3eeb_0": "sha256:b1a8b6a0864d09a5b2e33945aea0a816d06f2dbedc05878f3efe58760a18e75d"}, "tags": {"1.0.1--h7ef3eeb_0": "sha256:ebf035d6f930214a1fda9d8f3580ba192f0a0e0f69305f4421660e08b42b0ca3", "1.0.2--h7ef3eeb_0": "sha256:066a697bbd949df9766a10565f05b57955ec8d6754a05f12b11add7d4e6c7e04", "1.1.0--h7ef3eeb_0": "sha256:e960167c0f60983c316ccd5831febb67401ff7f35039a52c42ea88aa064db866", "1.1.1--h7ef3eeb_0": "sha256:b1a8b6a0864d09a5b2e33945aea0a816d06f2dbedc05878f3efe58760a18e75d"}, "docker": "quay.io/biocontainers/unicore", "aliases": {"checksum-profile": "/usr/local/bin/checksum-profile", "datasets-cli": "/usr/local/bin/datasets-cli", "elastishadow": "/usr/local/bin/elastishadow", "foldmason": "/usr/local/bin/foldmason", "foldseek": "/usr/local/bin/foldseek", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "huggingface-cli": "/usr/local/bin/huggingface-cli", "protoc-28.2.0": "/usr/local/bin/protoc-28.2.0", "spm_decode": "/usr/local/bin/spm_decode", "spm_encode": "/usr/local/bin/spm_encode", "spm_export_vocab": "/usr/local/bin/spm_export_vocab", "spm_normalize": "/usr/local/bin/spm_normalize", "spm_train": "/usr/local/bin/spm_train", "torchfrtrace": "/usr/local/bin/torchfrtrace", "transformers-cli": "/usr/local/bin/transformers-cli", "unicore": "/usr/local/bin/unicore", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "get_gprof": "/usr/local/bin/get_gprof", "iqtree2": "/usr/local/bin/iqtree2", "aria2c": "/usr/local/bin/aria2c", "iqtree": "/usr/local/bin/iqtree", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "gawkbug": "/usr/local/bin/gawkbug", "xxhsum": "/usr/local/bin/xxhsum", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unicore.
singularity registry hpc automated addition for unicore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unicore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unicore:1.1.1--h7ef3eeb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unicore/1.1.1--h7ef3eeb_0
$ module help quay.io/biocontainers/unicore/1.1.1--h7ef3eeb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unicore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unicore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unicore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unicore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unicore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unicore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldmason

```bash
$ singularity exec <container> /usr/local/bin/foldmason
$ podman run --it --rm --entrypoint /usr/local/bin/foldmason   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldmason   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### foldseek

```bash
$ singularity exec <container> /usr/local/bin/foldseek
$ podman run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/foldseek   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.2.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.2.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_decode

```bash
$ singularity exec <container> /usr/local/bin/spm_decode
$ podman run --it --rm --entrypoint /usr/local/bin/spm_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_encode

```bash
$ singularity exec <container> /usr/local/bin/spm_encode
$ podman run --it --rm --entrypoint /usr/local/bin/spm_encode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_encode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_export_vocab

```bash
$ singularity exec <container> /usr/local/bin/spm_export_vocab
$ podman run --it --rm --entrypoint /usr/local/bin/spm_export_vocab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_export_vocab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_normalize

```bash
$ singularity exec <container> /usr/local/bin/spm_normalize
$ podman run --it --rm --entrypoint /usr/local/bin/spm_normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spm_train

```bash
$ singularity exec <container> /usr/local/bin/spm_train
$ podman run --it --rm --entrypoint /usr/local/bin/spm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spm_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers-cli

```bash
$ singularity exec <container> /usr/local/bin/transformers-cli
$ podman run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicore

```bash
$ singularity exec <container> /usr/local/bin/unicore
$ podman run --it --rm --entrypoint /usr/local/bin/unicore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
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