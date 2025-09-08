---
layout: container
name:  "quay.io/biocontainers/r-immunedeconv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-immunedeconv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-immunedeconv/container.yaml"
updated_at: "2025-09-08 05:16:59.301857"
latest: "2.1.2--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-immunedeconv"

versions:
 - "2.1.0--r41hdfd78af_0"
 - "2.1.0--r42hdfd78af_1"
 - "2.1.1--r42hdfd78af_0"
 - "2.1.1--r42hdfd78af_1"
 - "2.1.2--r42hdfd78af_0"
 - "2.1.2--r42hdfd78af_1"
 - "2.1.2--r43hdfd78af_2"
 - "2.1.2--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-immunedeconv"
config: {"url": "https://biocontainers.pro/tools/r-immunedeconv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-immunedeconv", "latest": {"2.1.2--r44hdfd78af_3": "sha256:655db0f878c4b5307fafdffdd84ecd4472ae8c014f2090d989a1291e6d0b8818"}, "tags": {"2.1.0--r41hdfd78af_0": "sha256:adb586fa12a7ed29ab239b2f1ae4e6328de5d5eeb4ed30a1b9907a26f62fa3a9", "2.1.0--r42hdfd78af_1": "sha256:5be53611a4b1a3bb8d0ecfb60365f47817d1fec5a24605cae2f2635ebe2d993e", "2.1.1--r42hdfd78af_0": "sha256:a50882cc289c5bb25b47dce65fdc42f77cc1bd6957c98cbdfbbb660209d3f3b4", "2.1.1--r42hdfd78af_1": "sha256:b72f2bbf7a7e643f529ec81341b27b64f5e59212dfe489771b956d74b82669c4", "2.1.2--r42hdfd78af_0": "sha256:613f9cea7b86d6202e70e16349f5431b318783e3b857d1bb6b974c7da90cf33f", "2.1.2--r42hdfd78af_1": "sha256:af43ff8d9ed432ca790bcd49e5fbd7589e2c57e0c76011a11c5a83b0ef434467", "2.1.2--r43hdfd78af_2": "sha256:952da4af3809bf80c5a60f7397df7191143009f3ef8eac20f884e950b49576be", "2.1.2--r44hdfd78af_3": "sha256:655db0f878c4b5307fafdffdd84ecd4472ae8c014f2090d989a1291e6d0b8818"}, "docker": "quay.io/biocontainers/r-immunedeconv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-immunedeconv.
shpc-registry automated BioContainers addition for r-immunedeconv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-immunedeconv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-immunedeconv:2.1.2--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-immunedeconv/2.1.2--r44hdfd78af_3
$ module help quay.io/biocontainers/r-immunedeconv/2.1.2--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-immunedeconv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-immunedeconv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-immunedeconv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-immunedeconv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-immunedeconv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-immunedeconv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-immunedeconv

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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