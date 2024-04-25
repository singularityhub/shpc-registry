---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathrender"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathrender/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathrender/container.yaml"
updated_at: "2024-04-25 02:45:44.161832"
latest: "1.70.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathrender"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
 - "1.68.0--r43hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathrender"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathrender", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathrender", "latest": {"1.70.0--r43hdfd78af_0": "sha256:d353097567118c16099235ded56a8dcc503279a64c410520066a6dc2a51415f3"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:612ac39d6d5c49e6d99fbcdaf1afc62ac3dd72a01fe53f504160d4d2adf45ccb", "1.66.0--r42hdfd78af_0": "sha256:a9d9990d2db1ea80cfc3fd7cbfd300cf15f391b61ff229c7a83376682a0c5152", "1.68.0--r43hdfd78af_0": "sha256:03a12751f8c430524178627e681605c190e1771fbb83c3e82a27f24e1e46a406", "1.70.0--r43hdfd78af_0": "sha256:d353097567118c16099235ded56a8dcc503279a64c410520066a6dc2a51415f3"}, "docker": "quay.io/biocontainers/bioconductor-pathrender"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathrender.
shpc-registry automated BioContainers addition for bioconductor-pathrender
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathrender
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathrender:1.70.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathrender/1.70.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathrender/1.70.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathrender-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathrender-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathrender-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathrender-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathrender-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathrender-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pathrender

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