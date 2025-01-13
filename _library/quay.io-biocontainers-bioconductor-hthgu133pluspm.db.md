---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133pluspm.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133pluspm.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133pluspm.db/container.yaml"
updated_at: "2025-01-13 03:24:26.174525"
latest: "3.13.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133pluspm.db"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspm.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133pluspm.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspm.db", "latest": {"3.13.0--r43hdfd78af_4": "sha256:a0d3943764957f09c378399b21cbebb97b8776450866a70c1bc909b37d77ea64"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:019692fd759218e685a96bf08d3856dc6cf46e3a9071422eeecb3951ca4e042e", "3.13.0--r42hdfd78af_2": "sha256:f83b63880d9c71abba8a03683794a1e4b8de5f221cc70adc9ba0672f54ec35ad", "3.13.0--r43hdfd78af_3": "sha256:afdcb543adc7ebb54e9aa00bda8e8dbabf3a5071c87f51a5c1204024c8d60537", "3.13.0--r43hdfd78af_4": "sha256:a0d3943764957f09c378399b21cbebb97b8776450866a70c1bc909b37d77ea64"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133pluspm.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133pluspm.db.
shpc-registry automated BioContainers addition for bioconductor-hthgu133pluspm.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133pluspm.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133pluspm.db:3.13.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133pluspm.db/3.13.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hthgu133pluspm.db/3.13.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133pluspm.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133pluspm.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133pluspm.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133pluspm.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133pluspm.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133pluspm.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hthgu133pluspm.db

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