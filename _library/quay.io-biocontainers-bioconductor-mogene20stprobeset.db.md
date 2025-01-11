---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogene20stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogene20stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogene20stprobeset.db/container.yaml"
updated_at: "2025-01-11 03:12:00.920414"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mogene20stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mogene20stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogene20stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogene20stprobeset.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:9a7140e8531412cb4d664cd82c2ab9ea55e2c2ebd51dded2cad2f200574bb1ab"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:4fa24d699d6affeaf6f1b03c4770f2b257e9d25b1f58b9f15a6f2c160bafc825", "8.8.0--r42hdfd78af_2": "sha256:f8a4ef4f2bcc4e9328ce621c55243ece3e33c2f5b8827f27ab9b0cd627cd199a", "8.8.0--r43hdfd78af_3": "sha256:a94aca4726456155784cf83a54286eb99507205ca219d409b45998aa600a8b1d", "8.8.0--r43hdfd78af_4": "sha256:cd9f6a11473032e2dc2fba6b6d5e7bbd73c946e82790bc5bdb3e9ed6e401d803", "8.8.0--r44hdfd78af_5": "sha256:9a7140e8531412cb4d664cd82c2ab9ea55e2c2ebd51dded2cad2f200574bb1ab"}, "docker": "quay.io/biocontainers/bioconductor-mogene20stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogene20stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-mogene20stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene20stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene20stprobeset.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogene20stprobeset.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mogene20stprobeset.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogene20stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene20stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene20stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogene20stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogene20stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogene20stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogene20stprobeset.db

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