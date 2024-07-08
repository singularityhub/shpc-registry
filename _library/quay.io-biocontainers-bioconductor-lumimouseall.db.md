---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumimouseall.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumimouseall.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumimouseall.db/container.yaml"
updated_at: "2024-07-08 03:34:16.710007"
latest: "1.22.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-lumimouseall.db"

versions:
 - "1.22.0--r41hdfd78af_9"
 - "1.22.0--r42hdfd78af_10"
 - "1.22.0--r43hdfd78af_11"
 - "1.22.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-lumimouseall.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumimouseall.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumimouseall.db", "latest": {"1.22.0--r43hdfd78af_12": "sha256:eba8cd9017d9afc3f1993e1ee70d05a71d0af619650fdf83ef48b4ab8499fde4"}, "tags": {"1.22.0--r41hdfd78af_9": "sha256:265552b04065ab345fec13af65bffd564819ad9f410395748df42374a6c1bd4d", "1.22.0--r42hdfd78af_10": "sha256:95ed76f20568ed883ea9c63b54dc0a22c36c0ef8ed376369b88d6b860c237279", "1.22.0--r43hdfd78af_11": "sha256:b2d407f1372d1a6b4ba40d9d1432a9172faf987baf4828b9cd81a8043fd94be8", "1.22.0--r43hdfd78af_12": "sha256:eba8cd9017d9afc3f1993e1ee70d05a71d0af619650fdf83ef48b4ab8499fde4"}, "docker": "quay.io/biocontainers/bioconductor-lumimouseall.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumimouseall.db.
shpc-registry automated BioContainers addition for bioconductor-lumimouseall.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumimouseall.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumimouseall.db:1.22.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumimouseall.db/1.22.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-lumimouseall.db/1.22.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumimouseall.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumimouseall.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumimouseall.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumimouseall.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumimouseall.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumimouseall.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lumimouseall.db

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