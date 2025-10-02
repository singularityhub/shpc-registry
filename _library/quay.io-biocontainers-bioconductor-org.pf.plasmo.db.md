---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.pf.plasmo.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.pf.plasmo.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.pf.plasmo.db/container.yaml"
updated_at: "2025-10-02 04:07:28.876097"
latest: "3.14.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-org.pf.plasmo.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.10.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.pf.plasmo.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.pf.plasmo.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.pf.plasmo.db", "latest": {"3.14.0--r41hdfd78af_1": "sha256:e73fecb3adbe00af78d794277613d0069fdcf9ede35ab1f7333ae5f537ce7220"}, "tags": {"3.8.2--r36_1": "sha256:96a3e5e65de8620263b527c69860de2c102a410e909f52e4564c7031e011c599", "3.14.0--r41hdfd78af_1": "sha256:e73fecb3adbe00af78d794277613d0069fdcf9ede35ab1f7333ae5f537ce7220", "3.13.0--r41hdfd78af_0": "sha256:af2c9118506ce5d92e234631538fc3dad4c1da6b5b0d5daff517aaf5cab35d47", "3.12.0--r40hdfd78af_1": "sha256:3bac465b709bfde97540b89cd72440359dd65308464a5dd41ef5041e8bda8168", "3.11.1--r40_0": "sha256:4f6b77ea067bec00ae6ec913f339710f1fd0c92e6b8387e1dcfba8c44337561b", "3.10.0--r36_0": "sha256:cfb5324b4a36eda916f8ae64753989d384f8daa536b4c919d7588794125ef6da"}, "docker": "quay.io/biocontainers/bioconductor-org.pf.plasmo.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.pf.plasmo.db.
shpc-registry automated BioContainers addition for bioconductor-org.pf.plasmo.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.pf.plasmo.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.pf.plasmo.db:3.14.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.pf.plasmo.db/3.14.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-org.pf.plasmo.db/3.14.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.pf.plasmo.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.pf.plasmo.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.pf.plasmo.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.pf.plasmo.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.pf.plasmo.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.pf.plasmo.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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