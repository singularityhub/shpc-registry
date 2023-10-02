---
layout: container
name:  "quay.io/biocontainers/selene-sdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selene-sdk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/selene-sdk/container.yaml"
updated_at: "2023-10-02 03:01:35.717764"
latest: "0.5.0--py37h77a2a36_1"
container_url: "https://biocontainers.pro/tools/selene-sdk"
aliases:
 - "selene_sdk"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "faidx"
 - "f2py3.7"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.7"
 - "idle3.7"
versions:
 - "0.5.0--py37h77a2a36_1"
description: "shpc-registry automated BioContainers addition for selene-sdk"
config: {"url": "https://biocontainers.pro/tools/selene-sdk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for selene-sdk", "latest": {"0.5.0--py37h77a2a36_1": "sha256:58d61ec06edb3441f7d9b2b5dcc0f819a096b134468c6b5b4eda1cae22392d0e"}, "tags": {"0.5.0--py37h77a2a36_1": "sha256:58d61ec06edb3441f7d9b2b5dcc0f819a096b134468c6b5b4eda1cae22392d0e"}, "docker": "quay.io/biocontainers/selene-sdk", "aliases": {"selene_sdk": "/usr/local/bin/selene_sdk", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "faidx": "/usr/local/bin/faidx", "f2py3.7": "/usr/local/bin/f2py3.7", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selene-sdk.
shpc-registry automated BioContainers addition for selene-sdk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selene-sdk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selene-sdk:0.5.0--py37h77a2a36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selene-sdk/0.5.0--py37h77a2a36_1
$ module help quay.io/biocontainers/selene-sdk/0.5.0--py37h77a2a36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selene-sdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selene-sdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selene-sdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selene-sdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selene-sdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selene-sdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### selene_sdk

```bash
$ singularity exec <container> /usr/local/bin/selene_sdk
$ podman run --it --rm --entrypoint /usr/local/bin/selene_sdk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selene_sdk   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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