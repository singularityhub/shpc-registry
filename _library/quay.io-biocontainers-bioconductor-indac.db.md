---
layout: container
name:  "quay.io/biocontainers/bioconductor-indac.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-indac.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-indac.db/container.yaml"
updated_at: "2025-03-20 04:31:37.420273"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-indac.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-indac.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-indac.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-indac.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:318c90e72a2079996e798434ecde94b196d648a7dfeedac40ddde8119c96e19b"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:7b5422bed32c3aacb02169bead5c7efd1f657d0735a196a4ae48bf9208e834ee", "3.2.3--r42hdfd78af_10": "sha256:b24dc097c3597e2e4bfc3e57c3f25829cf7f32b686b9f7496bba3193e3954cc1", "3.2.3--r43hdfd78af_11": "sha256:1bcf2c7691269b7c4a9465eaab550c584d2d686fef8f16e068ee00f7ad892161", "3.2.3--r43hdfd78af_12": "sha256:318c90e72a2079996e798434ecde94b196d648a7dfeedac40ddde8119c96e19b"}, "docker": "quay.io/biocontainers/bioconductor-indac.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-indac.db.
shpc-registry automated BioContainers addition for bioconductor-indac.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-indac.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-indac.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-indac.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-indac.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-indac.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-indac.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-indac.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-indac.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-indac.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-indac.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-indac.db

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