---
layout: container
name:  "quay.io/biocontainers/bioconductor-pedbarrayv9.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pedbarrayv9.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pedbarrayv9.db/container.yaml"
updated_at: "2024-02-01 03:03:28.037612"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-pedbarrayv9.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-pedbarrayv9.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pedbarrayv9.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pedbarrayv9.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:9c14398e84d1a57cd9909d6bd9fd27a0a28bfed7f078624dc06063bccc48314e"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:14a1d0de09042a8d997c0122aff7e771588854c8c65ab108664f5865a88b59c0", "3.2.3--r42hdfd78af_10": "sha256:045dca014c437c01ff72a3e44e8b8c7ede51a8de6608cacd967705a4eb42cb18", "3.2.3--r43hdfd78af_11": "sha256:2472cbf86cbf68ac6d78bd99cfde9767d04517b8c4886bf2081a7597b884c78a", "3.2.3--r43hdfd78af_12": "sha256:9c14398e84d1a57cd9909d6bd9fd27a0a28bfed7f078624dc06063bccc48314e"}, "docker": "quay.io/biocontainers/bioconductor-pedbarrayv9.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pedbarrayv9.db.
shpc-registry automated BioContainers addition for bioconductor-pedbarrayv9.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pedbarrayv9.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pedbarrayv9.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pedbarrayv9.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-pedbarrayv9.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pedbarrayv9.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pedbarrayv9.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pedbarrayv9.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pedbarrayv9.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pedbarrayv9.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pedbarrayv9.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pedbarrayv9.db

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