---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirbase.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirbase.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirbase.db/container.yaml"
updated_at: "2023-11-12 02:51:56.854168"
latest: "1.2.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mirbase.db"

versions:
 - "1.2.0--r41hdfd78af_9"
 - "1.2.0--r42hdfd78af_10"
 - "1.2.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mirbase.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirbase.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirbase.db", "latest": {"1.2.0--r43hdfd78af_11": "sha256:66a888136c0180ca765c269c2d0a73ba3c2c59c12eb08e5e1e48a7fa68d13716"}, "tags": {"1.2.0--r41hdfd78af_9": "sha256:61cb11fc70be45577dd3b9d16892aa1118e56fe49259c2ce6831e750a36b4b3e", "1.2.0--r42hdfd78af_10": "sha256:d1f0f9893cacbb259208eb58c71ca3d666a5c7b4782469a959e90376cd1a981e", "1.2.0--r43hdfd78af_11": "sha256:66a888136c0180ca765c269c2d0a73ba3c2c59c12eb08e5e1e48a7fa68d13716"}, "docker": "quay.io/biocontainers/bioconductor-mirbase.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirbase.db.
shpc-registry automated BioContainers addition for bioconductor-mirbase.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbase.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirbase.db:1.2.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirbase.db/1.2.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mirbase.db/1.2.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirbase.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbase.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirbase.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirbase.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirbase.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirbase.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirbase.db

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