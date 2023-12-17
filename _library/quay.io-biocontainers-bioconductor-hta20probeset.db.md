---
layout: container
name:  "quay.io/biocontainers/bioconductor-hta20probeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hta20probeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hta20probeset.db/container.yaml"
updated_at: "2023-12-17 03:01:14.801394"
latest: "8.8.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-hta20probeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-hta20probeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hta20probeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hta20probeset.db", "latest": {"8.8.0--r43hdfd78af_4": "sha256:b8e2262f6282edaf53b0ee3ad51991126559af8b340383a11c33ac2b0865c4e2"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:89ec17f27083ca1f69270d05318c4344f19f1a5713c3923f67fcb0346c817e43", "8.8.0--r42hdfd78af_2": "sha256:576932d37ce9bd2afcaa65b2d0ba79779c1ef536de760a8458b2e30561fb33c0", "8.8.0--r43hdfd78af_3": "sha256:257ce773eee7c4593a059d331b212c76cd7fe98c760bab47de5862812d56e538", "8.8.0--r43hdfd78af_4": "sha256:b8e2262f6282edaf53b0ee3ad51991126559af8b340383a11c33ac2b0865c4e2"}, "docker": "quay.io/biocontainers/bioconductor-hta20probeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hta20probeset.db.
shpc-registry automated BioContainers addition for bioconductor-hta20probeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hta20probeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hta20probeset.db:8.8.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hta20probeset.db/8.8.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-hta20probeset.db/8.8.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hta20probeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hta20probeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hta20probeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hta20probeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hta20probeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hta20probeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hta20probeset.db

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