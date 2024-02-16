---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanv2.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanv2.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanv2.db/container.yaml"
updated_at: "2024-02-16 02:56:21.714717"
latest: "1.26.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanv2.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanv2.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2.db", "latest": {"1.26.0--r43hdfd78af_12": "sha256:ac39eb615f59f672fbe043925cc059c119a276ce4e82e4d059fb322f23e9d928"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:0492a0be302d7e2cf9f8ef3cf10b3fc15661d184e5b0b5215873f67500a1b942", "1.26.0--r42hdfd78af_10": "sha256:cb3b6b25d76597dadad30f6b7ff77a89e5f05d8550d56c92241486ecce72443a", "1.26.0--r43hdfd78af_11": "sha256:3605a73dec84002003cd67af0b2ee1366d12c99ed5a32feb8c7ea5320738dc58", "1.26.0--r43hdfd78af_12": "sha256:ac39eb615f59f672fbe043925cc059c119a276ce4e82e4d059fb322f23e9d928"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanv2.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanv2.db.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanv2.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv2.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanv2.db:1.26.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanv2.db/1.26.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-illuminahumanv2.db/1.26.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanv2.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv2.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanv2.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanv2.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanv2.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanv2.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanv2.db

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