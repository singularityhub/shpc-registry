---
layout: container
name:  "quay.io/biocontainers/bioconductor-m20kcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-m20kcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-m20kcod.db/container.yaml"
updated_at: "2023-11-16 03:12:40.966115"
latest: "3.4.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-m20kcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-m20kcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-m20kcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-m20kcod.db", "latest": {"3.4.0--r43hdfd78af_11": "sha256:ceb33063090c27e8dfe43763bcd9a25b25a99daae65956cfcda63ecba6e86bb6"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:e5d18802667ae30abecd736fc08f1efacd2a30b42741307d24b90ef93e4e11eb", "3.4.0--r42hdfd78af_10": "sha256:0c3028bcef308bfd7a6d1dfb44357aa0b18d4acc8fa2b44f2aa9b8f7851472c4", "3.4.0--r43hdfd78af_11": "sha256:ceb33063090c27e8dfe43763bcd9a25b25a99daae65956cfcda63ecba6e86bb6"}, "docker": "quay.io/biocontainers/bioconductor-m20kcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-m20kcod.db.
shpc-registry automated BioContainers addition for bioconductor-m20kcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-m20kcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-m20kcod.db:3.4.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-m20kcod.db/3.4.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-m20kcod.db/3.4.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-m20kcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m20kcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m20kcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-m20kcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-m20kcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-m20kcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-m20kcod.db

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