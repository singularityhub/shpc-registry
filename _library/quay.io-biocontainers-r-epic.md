---
layout: container
name:  "quay.io/biocontainers/r-epic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-epic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-epic/container.yaml"
updated_at: "2024-12-13 03:26:45.061343"
latest: "1.1.7--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-epic"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1--r41hdfd78af_4"
 - "1.1--r42hdfd78af_5"
 - "1.1.6--r42hdfd78af_0"
 - "1.1.7--r42hdfd78af_0"
 - "1.1.7--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-epic"
config: {"url": "https://biocontainers.pro/tools/r-epic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-epic", "latest": {"1.1.7--r43hdfd78af_1": "sha256:b6d618e05e4aec91fd42c5ba6c9a4eaf401aac9dac112fd38c9d3384488bbfdd"}, "tags": {"1.1--r41hdfd78af_4": "sha256:009053ec0f8cfb2d5a547677e497bf8e95f845962adffe23289554a774538c92", "1.1--r42hdfd78af_5": "sha256:1fe5e2dd6f1070c1ef1c445647aa5bb205442f2a36f05c0da97e6d4be0aac6d9", "1.1.6--r42hdfd78af_0": "sha256:fb01a7408383632f8c60c1667442003c847c599c8a00f2540284099a231b7920", "1.1.7--r42hdfd78af_0": "sha256:8857158fb2b37786b75d136b47c93a89502e2a00d575eee996ae1581420c6794", "1.1.7--r43hdfd78af_1": "sha256:b6d618e05e4aec91fd42c5ba6c9a4eaf401aac9dac112fd38c9d3384488bbfdd"}, "docker": "quay.io/biocontainers/r-epic", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-epic.
shpc-registry automated BioContainers addition for r-epic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-epic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-epic:1.1.7--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-epic/1.1.7--r43hdfd78af_1
$ module help quay.io/biocontainers/r-epic/1.1.7--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-epic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-epic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-epic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-epic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-epic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-epic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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