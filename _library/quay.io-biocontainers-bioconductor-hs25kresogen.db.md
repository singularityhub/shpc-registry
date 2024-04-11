---
layout: container
name:  "quay.io/biocontainers/bioconductor-hs25kresogen.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hs25kresogen.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hs25kresogen.db/container.yaml"
updated_at: "2024-04-11 02:57:19.608709"
latest: "2.5.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hs25kresogen.db"

versions:
 - "2.5.0--r41hdfd78af_9"
 - "2.5.0--r42hdfd78af_10"
 - "2.5.0--r43hdfd78af_11"
 - "2.5.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hs25kresogen.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hs25kresogen.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hs25kresogen.db", "latest": {"2.5.0--r43hdfd78af_12": "sha256:dcee74a85e37945341041fde0d259233962ff9415304bda8d6dd31660493876b"}, "tags": {"2.5.0--r41hdfd78af_9": "sha256:d7a6340860e7902e283466bbdaa80d4bce284a2f014cb2c051c3ccfdc3b89e31", "2.5.0--r42hdfd78af_10": "sha256:0f51cd78b77a263aa6c04ce8297850f2733aca5e429c54e4ec2249e3a3f60ba5", "2.5.0--r43hdfd78af_11": "sha256:3ab84cb4e1de318080da1eb695b4e385dddbd3a854a1c65b22df64f64e4df8c7", "2.5.0--r43hdfd78af_12": "sha256:dcee74a85e37945341041fde0d259233962ff9415304bda8d6dd31660493876b"}, "docker": "quay.io/biocontainers/bioconductor-hs25kresogen.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hs25kresogen.db.
shpc-registry automated BioContainers addition for bioconductor-hs25kresogen.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hs25kresogen.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hs25kresogen.db:2.5.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hs25kresogen.db/2.5.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hs25kresogen.db/2.5.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hs25kresogen.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hs25kresogen.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hs25kresogen.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hs25kresogen.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hs25kresogen.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hs25kresogen.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hs25kresogen.db

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