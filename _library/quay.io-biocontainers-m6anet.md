---
layout: container
name:  "quay.io/biocontainers/m6anet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/m6anet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/m6anet/container.yaml"
updated_at: "2024-10-26 03:25:36.575738"
latest: "2.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/m6anet"
aliases:
 - "m6anet"
 - "m6anet-compute_norm_factors"
 - "m6anet-dataprep"
 - "m6anet-run_inference"
 - "m6anet-train"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "futurize"
 - "pasteurize"
 - "f2py3.8"
 - "tqdm"
 - "normalizer"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "2.0.2--pyhdfd78af_0"
 - "2.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for m6anet"
config: {"url": "https://biocontainers.pro/tools/m6anet", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for m6anet", "latest": {"2.1.0--pyhdfd78af_0": "sha256:d2c7247c253a6570964cb431cccb3a3b8a9345022d547322c5f6081a1f221c58"}, "tags": {"2.0.2--pyhdfd78af_0": "sha256:774c962203226a214e435df070ecff216c9770ffde30bc33c0d09db6d42f12e3", "2.1.0--pyhdfd78af_0": "sha256:d2c7247c253a6570964cb431cccb3a3b8a9345022d547322c5f6081a1f221c58"}, "docker": "quay.io/biocontainers/m6anet", "aliases": {"m6anet": "/usr/local/bin/m6anet", "m6anet-compute_norm_factors": "/usr/local/bin/m6anet-compute_norm_factors", "m6anet-dataprep": "/usr/local/bin/m6anet-dataprep", "m6anet-run_inference": "/usr/local/bin/m6anet-run_inference", "m6anet-train": "/usr/local/bin/m6anet-train", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "f2py3.8": "/usr/local/bin/f2py3.8", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/m6anet.
singularity registry hpc automated addition for m6anet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/m6anet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/m6anet:2.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/m6anet/2.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/m6anet/2.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### m6anet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### m6anet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### m6anet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### m6anet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### m6anet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### m6anet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### m6anet

```bash
$ singularity exec <container> /usr/local/bin/m6anet
$ podman run --it --rm --entrypoint /usr/local/bin/m6anet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m6anet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m6anet-compute_norm_factors

```bash
$ singularity exec <container> /usr/local/bin/m6anet-compute_norm_factors
$ podman run --it --rm --entrypoint /usr/local/bin/m6anet-compute_norm_factors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m6anet-compute_norm_factors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m6anet-dataprep

```bash
$ singularity exec <container> /usr/local/bin/m6anet-dataprep
$ podman run --it --rm --entrypoint /usr/local/bin/m6anet-dataprep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m6anet-dataprep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m6anet-run_inference

```bash
$ singularity exec <container> /usr/local/bin/m6anet-run_inference
$ podman run --it --rm --entrypoint /usr/local/bin/m6anet-run_inference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m6anet-run_inference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m6anet-train

```bash
$ singularity exec <container> /usr/local/bin/m6anet-train
$ podman run --it --rm --entrypoint /usr/local/bin/m6anet-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m6anet-train   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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