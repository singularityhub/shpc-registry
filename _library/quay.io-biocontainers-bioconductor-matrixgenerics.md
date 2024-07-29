---
layout: container
name:  "quay.io/biocontainers/bioconductor-matrixgenerics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-matrixgenerics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-matrixgenerics/container.yaml"
updated_at: "2024-07-29 17:24:02.904272"
latest: "1.14.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-matrixgenerics"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.2--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_1"
 - "1.14.0--r43hdfd78af_2"
 - "1.14.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-matrixgenerics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-matrixgenerics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-matrixgenerics", "latest": {"1.14.0--r43hdfd78af_3": "sha256:223586c30ec4914398696139503695a88113af780001a10478be56e8c3ed9e8d"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:56e4e617b0774f182ac143d91569d33a43d671c606c1fc44c199ed7bca8d7e1a", "1.10.0--r42hdfd78af_0": "sha256:29320fd25e9f47419019977e3e4b0da190a09a02003d8f41fd688bb75636461b", "1.12.2--r43hdfd78af_0": "sha256:b2d14dab80d65a493c40759f57e8af27f4e7407fe7488b892a235eacb2cdf3a9", "1.14.0--r43hdfd78af_1": "sha256:96fd9a8f2689bfd1a723f3c28970ff7716fba36b5161b9f01443f13c7e77d707", "1.14.0--r43hdfd78af_2": "sha256:ec0141f37e84b9f91372d20cfca04acbcc889b535fd133b067c6950df5043b4d", "1.14.0--r43hdfd78af_3": "sha256:223586c30ec4914398696139503695a88113af780001a10478be56e8c3ed9e8d"}, "docker": "quay.io/biocontainers/bioconductor-matrixgenerics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-matrixgenerics.
shpc-registry automated BioContainers addition for bioconductor-matrixgenerics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-matrixgenerics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-matrixgenerics:1.14.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-matrixgenerics/1.14.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-matrixgenerics/1.14.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-matrixgenerics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matrixgenerics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matrixgenerics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-matrixgenerics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-matrixgenerics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-matrixgenerics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-matrixgenerics

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