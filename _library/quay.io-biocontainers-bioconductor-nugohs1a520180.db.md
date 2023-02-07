---
layout: container
name:  "quay.io/biocontainers/bioconductor-nugohs1a520180.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nugohs1a520180.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nugohs1a520180.db/container.yaml"
updated_at: "2023-02-07 02:49:21.289193"
latest: "3.4.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-nugohs1a520180.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nugohs1a520180.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180.db", "latest": {"3.4.0--r42hdfd78af_10": "sha256:f7ef0423872a374aa3291b2e14e1e151814ae347f322597831dc32dc7a8ec6d5"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:07104eb05b0baede9194ac2344f30cd9044dcc4c5d25bb5faafbbe9c13503976", "3.4.0--r42hdfd78af_10": "sha256:f7ef0423872a374aa3291b2e14e1e151814ae347f322597831dc32dc7a8ec6d5"}, "docker": "quay.io/biocontainers/bioconductor-nugohs1a520180.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nugohs1a520180.db.
shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nugohs1a520180.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nugohs1a520180.db:3.4.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nugohs1a520180.db/3.4.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-nugohs1a520180.db/3.4.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nugohs1a520180.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugohs1a520180.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugohs1a520180.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nugohs1a520180.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nugohs1a520180.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nugohs1a520180.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nugohs1a520180.db

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