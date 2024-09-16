---
layout: container
name:  "quay.io/biocontainers/bioconductor-ye6100subacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ye6100subacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ye6100subacdf/container.yaml"
updated_at: "2024-09-16 04:08:22.670682"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ye6100subacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ye6100subacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ye6100subacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ye6100subacdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:c9ed02389b6730d89facfeb1ecb203a97c04adf6ac8aec93be194daf692ecfd6"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:baa9d188101bad877a664fa32e152b7805464c9eebbf5ef1d7e4dace0ffaa1f6", "2.18.0--r42hdfd78af_10": "sha256:4bd56330a2f8c5633aec8a6402ead5d7ce9442f9e42651b44367c4bb4a69d54a", "2.18.0--r43hdfd78af_11": "sha256:494a3a069a1357f59fe99a130e417efbea9f27044f5f410d6f079078a7a3f04f", "2.18.0--r43hdfd78af_12": "sha256:c9ed02389b6730d89facfeb1ecb203a97c04adf6ac8aec93be194daf692ecfd6"}, "docker": "quay.io/biocontainers/bioconductor-ye6100subacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ye6100subacdf.
shpc-registry automated BioContainers addition for bioconductor-ye6100subacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subacdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ye6100subacdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ye6100subacdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ye6100subacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ye6100subacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ye6100subacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ye6100subacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ye6100subacdf

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