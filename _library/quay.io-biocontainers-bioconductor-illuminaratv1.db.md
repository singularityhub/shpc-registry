---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminaratv1.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminaratv1.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminaratv1.db/container.yaml"
updated_at: "2024-02-08 08:24:13.506599"
latest: "1.26.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminaratv1.db"

versions:
 - "1.26.0--r41hdfd78af_9"
 - "1.26.0--r42hdfd78af_10"
 - "1.26.0--r43hdfd78af_11"
 - "1.26.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminaratv1.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminaratv1.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminaratv1.db", "latest": {"1.26.0--r43hdfd78af_12": "sha256:7cb8a413808e55c62badabed044c92a5ab794fee8a2181b1577e5f6b43f88bc5"}, "tags": {"1.26.0--r41hdfd78af_9": "sha256:c388b903928c73297e546a4dbbd0b1be00424be620aba7fa89f3c45c544da77b", "1.26.0--r42hdfd78af_10": "sha256:aa5f5cc633fd039cf278f9eddf69b5d2515073d662fc86ab758e18c71e6da29e", "1.26.0--r43hdfd78af_11": "sha256:3f198b6ae0f4a598c491b2f3bcab7264bd845fa78030a5a5b89f6a603684a15a", "1.26.0--r43hdfd78af_12": "sha256:7cb8a413808e55c62badabed044c92a5ab794fee8a2181b1577e5f6b43f88bc5"}, "docker": "quay.io/biocontainers/bioconductor-illuminaratv1.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminaratv1.db.
shpc-registry automated BioContainers addition for bioconductor-illuminaratv1.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminaratv1.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminaratv1.db:1.26.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminaratv1.db/1.26.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-illuminaratv1.db/1.26.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminaratv1.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminaratv1.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminaratv1.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminaratv1.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminaratv1.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminaratv1.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminaratv1.db

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