---
layout: container
name:  "quay.io/biocontainers/immuneml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/immuneml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/immuneml/container.yaml"
updated_at: "2024-12-31 02:50:18.884032"
latest: "3.0.3--h1fe012e_0"
container_url: "https://biocontainers.pro/tools/immuneml"
aliases:
 - "airr-tools"
 - "immune-ml"
 - "immune-ml-quickstart"
 - "pystache"
 - "pystache-test"
 - "torchrun"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "google-oauthlib-tool"
 - "get_objgraph"
 - "undill"
 - "tensorboard"
 - "xkbcli"
 - "cygdb"
 - "cython"
versions:
 - "2.2.0--py39hbf8eff0_0"
 - "2.2.2--py39hbf8eff0_0"
 - "2.2.3--py37h8902056_0"
 - "2.2.4--py39hbf8eff0_0"
 - "2.2.4--py38he5da3d1_1"
 - "2.2.5--py39hf95cd2a_1"
 - "2.2.6--py38he5da3d1_0"
 - "2.2.6--py39hf95cd2a_0"
 - "2.2.6--py38h0020b31_1"
 - "3.0.3--h1fe012e_0"
description: "shpc-registry automated BioContainers addition for immuneml"
config: {"url": "https://biocontainers.pro/tools/immuneml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for immuneml", "latest": {"3.0.3--h1fe012e_0": "sha256:e2a92f08526edd65236b7e1999fd59da9cded2fa46f06feab1ddd49ddc3730f3"}, "tags": {"2.2.0--py39hbf8eff0_0": "sha256:60a6ea6a986487ea863598dc0585e75e337dbe36fb6cef5494d54ae135a3a347", "2.2.2--py39hbf8eff0_0": "sha256:187e443a396f53f14e95992e87c574ec22cfb0ef8925de47219cb1416ce70310", "2.2.3--py37h8902056_0": "sha256:fcd7b7e9750e4f76f4d5de45932b5d515b2f6aeebc39bc1c1c4dd597e727ca8f", "2.2.4--py39hbf8eff0_0": "sha256:39c028048421889e1312756ac516be6d8f2a9e637d64c29755a3b89441f3b7b5", "2.2.4--py38he5da3d1_1": "sha256:be75abc673b23f2ea4018863d80056eff57a390a4ebc80992b6e7cd9d4020593", "2.2.5--py39hf95cd2a_1": "sha256:38b71ffbdfabcc443e20e06ad9fa62e64d3a18be23ffaf82a926b28429fbe058", "2.2.6--py38he5da3d1_0": "sha256:2e01a8e85a254a88003e8b30f7ffcca20ef124b8a6c270a1ef076c52f77aaad6", "2.2.6--py39hf95cd2a_0": "sha256:44351c8d27e92462fc038d42231d8e394b8402a81004b723a0a1784133425321", "2.2.6--py38h0020b31_1": "sha256:4c434ce623eb93cd134cf07b4e0f9003f46c37e1b2a0f5db8461f66921e6f94b", "3.0.3--h1fe012e_0": "sha256:e2a92f08526edd65236b7e1999fd59da9cded2fa46f06feab1ddd49ddc3730f3"}, "docker": "quay.io/biocontainers/immuneml", "aliases": {"airr-tools": "/usr/local/bin/airr-tools", "immune-ml": "/usr/local/bin/immune-ml", "immune-ml-quickstart": "/usr/local/bin/immune-ml-quickstart", "pystache": "/usr/local/bin/pystache", "pystache-test": "/usr/local/bin/pystache-test", "torchrun": "/usr/local/bin/torchrun", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "tensorboard": "/usr/local/bin/tensorboard", "xkbcli": "/usr/local/bin/xkbcli", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/immuneml.
shpc-registry automated BioContainers addition for immuneml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/immuneml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/immuneml:3.0.3--h1fe012e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/immuneml/3.0.3--h1fe012e_0
$ module help quay.io/biocontainers/immuneml/3.0.3--h1fe012e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### immuneml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### immuneml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### immuneml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### immuneml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### immuneml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### immuneml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### airr-tools

```bash
$ singularity exec <container> /usr/local/bin/airr-tools
$ podman run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immune-ml

```bash
$ singularity exec <container> /usr/local/bin/immune-ml
$ podman run --it --rm --entrypoint /usr/local/bin/immune-ml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immune-ml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immune-ml-quickstart

```bash
$ singularity exec <container> /usr/local/bin/immune-ml-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/immune-ml-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immune-ml-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pystache

```bash
$ singularity exec <container> /usr/local/bin/pystache
$ podman run --it --rm --entrypoint /usr/local/bin/pystache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pystache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pystache-test

```bash
$ singularity exec <container> /usr/local/bin/pystache-test
$ podman run --it --rm --entrypoint /usr/local/bin/pystache-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pystache-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
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