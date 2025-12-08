---
layout: container
name:  "quay.io/biocontainers/phynteny_transformer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phynteny_transformer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phynteny_transformer/container.yaml"
updated_at: "2025-12-08 03:25:50.265789"
latest: "0.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/phynteny_transformer"
aliases:
 - "compute_confidence"
 - "datasets-cli"
 - "generate_training_data"
 - "huggingface-cli"
 - "install_models"
 - "phynteny_transformer"
 - "tiny-agents"
 - "train_model"
 - "transformers"
 - "transformers-cli"
 - "xxh3sum"
 - "protoc-28.3.0"
 - "torchfrtrace"
 - "checksum-profile"
 - "elastishadow"
 - "pybind11-config"
 - "get_gprof"
 - "torch_shm_manager"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "isympy"
 - "torchrun"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "get_objgraph"
 - "undill"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
versions:
 - "0.1.2--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for phynteny_transformer"
config: {"url": "https://biocontainers.pro/tools/phynteny_transformer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phynteny_transformer", "latest": {"0.1.3--pyhdfd78af_0": "sha256:b254483a374ba7c0c84a5789396c3d8cc5cb20cbcf7c9f45f6ecbbed5f6a128d"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:6bcebe9f43553ebc8036c6100933facd7d4193a1249d633364509f7d4056cf67", "0.1.3--pyhdfd78af_0": "sha256:b254483a374ba7c0c84a5789396c3d8cc5cb20cbcf7c9f45f6ecbbed5f6a128d"}, "docker": "quay.io/biocontainers/phynteny_transformer", "aliases": {"compute_confidence": "/usr/local/bin/compute_confidence", "datasets-cli": "/usr/local/bin/datasets-cli", "generate_training_data": "/usr/local/bin/generate_training_data", "huggingface-cli": "/usr/local/bin/huggingface-cli", "install_models": "/usr/local/bin/install_models", "phynteny_transformer": "/usr/local/bin/phynteny_transformer", "tiny-agents": "/usr/local/bin/tiny-agents", "train_model": "/usr/local/bin/train_model", "transformers": "/usr/local/bin/transformers", "transformers-cli": "/usr/local/bin/transformers-cli", "xxh3sum": "/usr/local/bin/xxh3sum", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "torchfrtrace": "/usr/local/bin/torchfrtrace", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "pybind11-config": "/usr/local/bin/pybind11-config", "get_gprof": "/usr/local/bin/get_gprof", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phynteny_transformer.
singularity registry hpc automated addition for phynteny_transformer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phynteny_transformer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phynteny_transformer:0.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phynteny_transformer/0.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/phynteny_transformer/0.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phynteny_transformer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phynteny_transformer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phynteny_transformer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phynteny_transformer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phynteny_transformer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phynteny_transformer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compute_confidence

```bash
$ singularity exec <container> /usr/local/bin/compute_confidence
$ podman run --it --rm --entrypoint /usr/local/bin/compute_confidence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute_confidence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_training_data

```bash
$ singularity exec <container> /usr/local/bin/generate_training_data
$ podman run --it --rm --entrypoint /usr/local/bin/generate_training_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_training_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_models

```bash
$ singularity exec <container> /usr/local/bin/install_models
$ podman run --it --rm --entrypoint /usr/local/bin/install_models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phynteny_transformer

```bash
$ singularity exec <container> /usr/local/bin/phynteny_transformer
$ podman run --it --rm --entrypoint /usr/local/bin/phynteny_transformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phynteny_transformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_model

```bash
$ singularity exec <container> /usr/local/bin/train_model
$ podman run --it --rm --entrypoint /usr/local/bin/train_model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers

```bash
$ singularity exec <container> /usr/local/bin/transformers
$ podman run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers-cli

```bash
$ singularity exec <container> /usr/local/bin/transformers-cli
$ podman run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mqtt5canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
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