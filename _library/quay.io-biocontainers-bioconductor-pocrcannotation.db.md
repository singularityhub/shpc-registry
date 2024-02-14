---
layout: container
name:  "quay.io/biocontainers/bioconductor-pocrcannotation.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pocrcannotation.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pocrcannotation.db/container.yaml"
updated_at: "2024-02-14 02:24:23.307298"
latest: "3.2.3--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-pocrcannotation.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-pocrcannotation.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pocrcannotation.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pocrcannotation.db", "latest": {"3.2.3--r43hdfd78af_11": "sha256:26d244927c74206cd50bfbeabb1754d7552101b583e12c1fa7a76604bfd09eed"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:b73b7b056be002568d450d57b779c11345ce7aa48a46a080d6b42d9b950e9668", "3.2.3--r42hdfd78af_10": "sha256:e259699a8629da1ceb5f535426a54e89eac1ebd3bbb4e9a71df2c4ae98f5061b", "3.2.3--r43hdfd78af_11": "sha256:26d244927c74206cd50bfbeabb1754d7552101b583e12c1fa7a76604bfd09eed"}, "docker": "quay.io/biocontainers/bioconductor-pocrcannotation.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pocrcannotation.db.
shpc-registry automated BioContainers addition for bioconductor-pocrcannotation.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pocrcannotation.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pocrcannotation.db:3.2.3--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pocrcannotation.db/3.2.3--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-pocrcannotation.db/3.2.3--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pocrcannotation.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pocrcannotation.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pocrcannotation.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pocrcannotation.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pocrcannotation.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pocrcannotation.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pocrcannotation.db

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