---
layout: container
name:  "quay.io/biocontainers/bioconductor-multtest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multtest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multtest/container.yaml"
updated_at: "2023-05-25 03:11:54.316640"
latest: "2.54.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multtest"

versions:
 - "2.50.0--r41hc0cfd56_2"
 - "2.54.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multtest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multtest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multtest", "latest": {"2.54.0--r42hc0cfd56_0": "sha256:8e7ab14a56d3765f6590bc2cc4eb61883bdc12578212549b33fa0fa26a8bc8c7"}, "tags": {"2.50.0--r41hc0cfd56_2": "sha256:487ca81662aa34fa3e7d7f1b95f7203cfbb9b31335e7383f2b9dc0025a86f454", "2.54.0--r42hc0cfd56_0": "sha256:8e7ab14a56d3765f6590bc2cc4eb61883bdc12578212549b33fa0fa26a8bc8c7"}, "docker": "quay.io/biocontainers/bioconductor-multtest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multtest.
shpc-registry automated BioContainers addition for bioconductor-multtest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multtest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multtest:2.54.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multtest/2.54.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-multtest/2.54.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multtest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multtest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multtest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multtest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multtest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multtest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-multtest

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