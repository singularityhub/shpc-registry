---
layout: container
name:  "quay.io/biocontainers/viral-host-hunter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viral-host-hunter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viral-host-hunter/container.yaml"
updated_at: "2025-11-21 04:06:53.382798"
latest: "0.1.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/viral-host-hunter"
aliases:
 - "datasets-cli"
 - "hf"
 - "protoc-31.1.0"
 - "protoc-gen-upb-31.1.0"
 - "protoc-gen-upbdefs-31.1.0"
 - "spm_decode"
 - "spm_encode"
 - "spm_export_vocab"
 - "spm_normalize"
 - "spm_train"
 - "tiny-agents"
 - "transformers"
 - "transformers-cli"
 - "vhh-predict"
 - "vhh-predict-gut"
 - "vhh-predict-multi"
 - "vhh-train-gut"
 - "vhh-train-multi"
 - "xxh3sum"
 - "huggingface-cli"
 - "h2benchmark"
 - "torchfrtrace"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "checksum-profile"
 - "elastishadow"
 - "get_gprof"
 - "pybind11-config"
 - "torch_shm_manager"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "isympy"
 - "torchrun"
 - "get_objgraph"
 - "undill"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
versions:
 - "0.1.11--pyhdfd78af_0"
description: "singularity registry hpc automated addition for viral-host-hunter"
config: {"url": "https://biocontainers.pro/tools/viral-host-hunter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for viral-host-hunter", "latest": {"0.1.11--pyhdfd78af_0": "sha256:855e42de7b9424cab164026f1d84cd5611e99b920f526894cddfd104e949f946"}, "tags": {"0.1.11--pyhdfd78af_0": "sha256:855e42de7b9424cab164026f1d84cd5611e99b920f526894cddfd104e949f946"}, "docker": "quay.io/biocontainers/viral-host-hunter", "aliases": {"datasets-cli": "/usr/local/bin/datasets-cli", "hf": "/usr/local/bin/hf", "protoc-31.1.0": "/usr/local/bin/protoc-31.1.0", "protoc-gen-upb-31.1.0": "/usr/local/bin/protoc-gen-upb-31.1.0", "protoc-gen-upbdefs-31.1.0": "/usr/local/bin/protoc-gen-upbdefs-31.1.0", "spm_decode": "/usr/local/bin/spm_decode", "spm_encode": "/usr/local/bin/spm_encode", "spm_export_vocab": "/usr/local/bin/spm_export_vocab", "spm_normalize": "/usr/local/bin/spm_normalize", "spm_train": "/usr/local/bin/spm_train", "tiny-agents": "/usr/local/bin/tiny-agents", "transformers": "/usr/local/bin/transformers", "transformers-cli": "/usr/local/bin/transformers-cli", "vhh-predict": "/usr/local/bin/vhh-predict", "vhh-predict-gut": "/usr/local/bin/vhh-predict-gut", "vhh-predict-multi": "/usr/local/bin/vhh-predict-multi", "vhh-train-gut": "/usr/local/bin/vhh-train-gut", "vhh-train-multi": "/usr/local/bin/vhh-train-multi", "xxh3sum": "/usr/local/bin/xxh3sum", "huggingface-cli": "/usr/local/bin/huggingface-cli", "h2benchmark": "/usr/local/bin/h2benchmark", "torchfrtrace": "/usr/local/bin/torchfrtrace", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "get_gprof": "/usr/local/bin/get_gprof", "pybind11-config": "/usr/local/bin/pybind11-config", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "isympy": "/usr/local/bin/isympy", "torchrun": "/usr/local/bin/torchrun", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viral-host-hunter.
singularity registry hpc automated addition for viral-host-hunter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viral-host-hunter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viral-host-hunter:0.1.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viral-host-hunter/0.1.11--pyhdfd78af_0
$ module help quay.io/biocontainers/viral-host-hunter/0.1.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viral-host-hunter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viral-host-hunter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viral-host-hunter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viral-host-hunter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viral-host-hunter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viral-host-hunter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### datasets-cli

```bash
$ singularity exec <container> /usr/local/bin/datasets-cli
$ podman run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vhh-predict

```bash
$ singularity exec <container> /usr/local/bin/vhh-predict
$ podman run --it --rm --entrypoint /usr/local/bin/vhh-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhh-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhh-predict-gut

```bash
$ singularity exec <container> /usr/local/bin/vhh-predict-gut
$ podman run --it --rm --entrypoint /usr/local/bin/vhh-predict-gut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhh-predict-gut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhh-predict-multi

```bash
$ singularity exec <container> /usr/local/bin/vhh-predict-multi
$ podman run --it --rm --entrypoint /usr/local/bin/vhh-predict-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhh-predict-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhh-train-gut

```bash
$ singularity exec <container> /usr/local/bin/vhh-train-gut
$ podman run --it --rm --entrypoint /usr/local/bin/vhh-train-gut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhh-train-gut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhh-train-multi

```bash
$ singularity exec <container> /usr/local/bin/vhh-train-multi
$ podman run --it --rm --entrypoint /usr/local/bin/vhh-train-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhh-train-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh3sum

```bash
$ singularity exec <container> /usr/local/bin/xxh3sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh3sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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