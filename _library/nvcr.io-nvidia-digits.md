---
layout: container
name:  "nvcr.io/nvidia/digits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/digits/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/digits/container.yaml"
updated_at: "2024-01-06 03:12:44.018619"
latest: "sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:digits/tags"
aliases:
 - "python"
versions:
 - "21.02-tensorflow-py3"
 - "21.03-tensorflow-py3"
 - "21.04-tensorflow-py3"
 - "21.05-tensorflow-py3"
 - "21.06-tensorflow-py3"
 - "21.08-tensorflow-py3"
 - "21.09-tensorflow-py3"
 - "21.07-tensorflow-py3"
 - "sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex"
 - "sha256-9821057c00a6413f1826cb1961c24704671c7f2e69993f1effce30fc3a696a8e.vex"
 - "sha256-7542143bc2292fc48a3874786877815a5ca6a74a69366324aaf66914155cb5a7.vex"
 - "sha256-364860a8f7c433e97c00031768af31bf8a3b70e361cc16c4e04d069ec42bf4bf.vex"
 - "sha256-d255314f71a1de749bce21b93554c49cca1796c495fa3373bb5e1fe0468d9e17.vex"
 - "sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.sbom"
description: "The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists."
config: {"docker": "nvcr.io/nvidia/digits", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:digits/tags", "maintainer": "@vsoch", "description": "The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists.", "latest": {"sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex": "sha256:2ddc3cd00d5eba6d9d3df4f49436f9c6bab4e23199923179a00132e4161212f8"}, "tags": {"21.02-tensorflow-py3": "sha256:f5973e9b4a4424b4d394d7c42cf0aee5259dbdcce58d8a9815fae081ce99020f", "21.03-tensorflow-py3": "sha256:ad2aa71d8650ea403437f86fc9a33760af8a20d980f64d660e8ef649e0d9296d", "21.04-tensorflow-py3": "sha256:b72344b124b07742f5a908566c5f1905edc3d58956e446db925cf153facdf9f9", "21.05-tensorflow-py3": "sha256:92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546", "21.06-tensorflow-py3": "sha256:fbe881eeb906edb58e67f7220617da648af74cac190fe4c14bb7646209eb5b89", "21.08-tensorflow-py3": "sha256:0e6009fb379ef17aef8f5cacb87f5a251c7762e0042acc6073533bad34625989", "21.09-tensorflow-py3": "sha256:2cd85ac9a8373804ae5242aeb36d2a438aabe2d349d07851b02ab0bb2309574d", "21.07-tensorflow-py3": "sha256:84a670644b33b6e1bfe19f67779517110ec6cb5a6082fb3ed974c79cc5a01389", "sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex": "sha256:2ddc3cd00d5eba6d9d3df4f49436f9c6bab4e23199923179a00132e4161212f8", "sha256-9821057c00a6413f1826cb1961c24704671c7f2e69993f1effce30fc3a696a8e.vex": "sha256:82cb6750e1ca1decaad3f3f628aeaf2393a8e7c4ea333277bd539c45c5641c70", "sha256-7542143bc2292fc48a3874786877815a5ca6a74a69366324aaf66914155cb5a7.vex": "sha256:66021ad6d5c945a3e0ff5a1b4a9d4a11d590c746d7a8d5b418816a484a52d1aa", "sha256-364860a8f7c433e97c00031768af31bf8a3b70e361cc16c4e04d069ec42bf4bf.vex": "sha256:9e3eec06f4256a31f18b586e7d1ba4c154d52f7072a36e85606d18f87eb23bbd", "sha256-d255314f71a1de749bce21b93554c49cca1796c495fa3373bb5e1fe0468d9e17.vex": "sha256:27f37c07d77e875948d172071928d625027a590acc8c44697799db2a6d184ff9", "sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.sbom": "sha256:8aba81e1516cfe20bb12768381a4e52aa6ef118e244086bb97c4e5af0a7c6f8c"}, "aliases": {"python": "/usr/bin/python"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/digits.
The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/digits
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/digits:sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/digits/sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex
$ module help nvcr.io/nvidia/digits/sha256-92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546.vex
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### digits-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### digits-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### digits-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### digits-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### digits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### digits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python

```bash
$ singularity exec <container> /usr/bin/python
$ podman run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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