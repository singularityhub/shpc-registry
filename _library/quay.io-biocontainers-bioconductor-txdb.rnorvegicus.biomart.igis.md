---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis/container.yaml"
updated_at: "2025-01-25 03:02:43.379462"
latest: "2.3.2--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.biomart.igis"

versions:
 - "2.3.2--r41hdfd78af_9"
 - "2.3.2--r42hdfd78af_10"
 - "2.3.2--r43hdfd78af_11"
 - "2.3.2--r43hdfd78af_12"
 - "2.3.2--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.biomart.igis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.rnorvegicus.biomart.igis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.biomart.igis", "latest": {"2.3.2--r44hdfd78af_13": "sha256:ad66f5337047ec1b59ef1b70365205130fe1ad6c3d0a0e2b1ae6d8ca765c5a6d"}, "tags": {"2.3.2--r41hdfd78af_9": "sha256:55b36ae995826bb703942561368a0731aba6b9aedcfedbbac75a73ec3fa1f85c", "2.3.2--r42hdfd78af_10": "sha256:e56dfb25e122582c1003c9de54adf91fe8e0b80421119679887aac4fe31f6a7d", "2.3.2--r43hdfd78af_11": "sha256:7bef18b5808556eab51438e7e9bcda8407d86fbb1b46a8b5546901beb3ffd4e3", "2.3.2--r43hdfd78af_12": "sha256:53a166f28eaf74cd2400de9ba93be4d8db3ac39f74ce8b5929be2906b2bc9e64", "2.3.2--r44hdfd78af_13": "sha256:ad66f5337047ec1b59ef1b70365205130fe1ad6c3d0a0e2b1ae6d8ca765c5a6d"}, "docker": "quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis.
shpc-registry automated BioContainers addition for bioconductor-txdb.rnorvegicus.biomart.igis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis:2.3.2--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis/2.3.2--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-txdb.rnorvegicus.biomart.igis/2.3.2--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.rnorvegicus.biomart.igis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.biomart.igis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.rnorvegicus.biomart.igis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.rnorvegicus.biomart.igis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.rnorvegicus.biomart.igis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.rnorvegicus.biomart.igis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txdb.rnorvegicus.biomart.igis

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