---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgug4845a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgug4845a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgug4845a.db/container.yaml"
updated_at: "2025-02-20 03:42:31.146297"
latest: "0.0.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgug4845a.db"

versions:
 - "0.0.3--r41hdfd78af_9"
 - "0.0.3--r42hdfd78af_10"
 - "0.0.3--r43hdfd78af_11"
 - "0.0.3--r43hdfd78af_12"
 - "0.0.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgug4845a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgug4845a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgug4845a.db", "latest": {"0.0.3--r44hdfd78af_13": "sha256:2b12b0bc5ef3981a5b9dfdfd42607347d6dc20b742b3368d9e0664c147754056"}, "tags": {"0.0.3--r41hdfd78af_9": "sha256:b2d887881ca27778710be2b8629178b9c3be0efa22cf966b3de2fbfbf3ee6e50", "0.0.3--r42hdfd78af_10": "sha256:24cc4ac541785275c6c214853b7661000dcb449f59d0322f1ed440378acffab1", "0.0.3--r43hdfd78af_11": "sha256:12e15c8836455d6193b9d07fab8ea7a3d73fd7d2f82aac2115f7d4c1877e60ac", "0.0.3--r43hdfd78af_12": "sha256:c8c6ce6fd10fb19bca9236d2918a07e44124fbcecb9fd727a9f81a293e3c1095", "0.0.3--r44hdfd78af_13": "sha256:2b12b0bc5ef3981a5b9dfdfd42607347d6dc20b742b3368d9e0664c147754056"}, "docker": "quay.io/biocontainers/bioconductor-hgug4845a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgug4845a.db.
shpc-registry automated BioContainers addition for bioconductor-hgug4845a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4845a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4845a.db:0.0.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgug4845a.db/0.0.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgug4845a.db/0.0.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgug4845a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4845a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4845a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgug4845a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgug4845a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgug4845a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgug4845a.db

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