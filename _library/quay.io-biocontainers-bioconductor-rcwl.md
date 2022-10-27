---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcwl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcwl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcwl/container.yaml"
updated_at: "2022-10-27 00:47:03.028708"
latest: "1.8.0--py39r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcwl"

versions:
 - "1.8.0--py39r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcwl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcwl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcwl", "latest": {"1.8.0--py39r41hdfd78af_0": "sha256:b7d2bea3b22496203db712b155e407db8573a7aa923880773aff87163b852df6"}, "tags": {"1.8.0--py39r41hdfd78af_0": "sha256:b7d2bea3b22496203db712b155e407db8573a7aa923880773aff87163b852df6"}, "docker": "quay.io/biocontainers/bioconductor-rcwl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcwl.
shpc-registry automated BioContainers addition for bioconductor-rcwl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcwl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcwl:1.8.0--py39r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcwl/1.8.0--py39r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcwl/1.8.0--py39r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcwl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcwl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcwl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcwl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcwl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcwl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rcwl

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