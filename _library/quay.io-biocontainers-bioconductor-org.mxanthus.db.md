---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.mxanthus.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.mxanthus.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.mxanthus.db/container.yaml"
updated_at: "2024-03-08 02:48:49.895280"
latest: "1.0.27--r43hdfd78af_9"
container_url: "https://biocontainers.pro/tools/bioconductor-org.mxanthus.db"
aliases:
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.0.27--r41hdfd78af_6"
 - "1.0.27--r42hdfd78af_7"
 - "1.0.27--r43hdfd78af_8"
 - "1.0.27--r43hdfd78af_9"
description: "shpc-registry automated BioContainers addition for bioconductor-org.mxanthus.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.mxanthus.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.mxanthus.db", "latest": {"1.0.27--r43hdfd78af_9": "sha256:d5e0be370accb401798c9dc9b3a7aed7c075a29bdbe6d67430a9eb01bbed6c47"}, "tags": {"1.0.27--r41hdfd78af_6": "sha256:1853fc2aa6be57ac505c13a55278ff4c8bf936702229c5362778c2f0d340f086", "1.0.27--r42hdfd78af_7": "sha256:0d97864d6739db2183a958e37c4bcf7be4d4ce293e772ec53ad37d1ec71023aa", "1.0.27--r43hdfd78af_8": "sha256:8b07a330aff2cc230386d5d74473647337f1809f6c060a73e4acbae2bb8a71a7", "1.0.27--r43hdfd78af_9": "sha256:d5e0be370accb401798c9dc9b3a7aed7c075a29bdbe6d67430a9eb01bbed6c47"}, "docker": "quay.io/biocontainers/bioconductor-org.mxanthus.db", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.mxanthus.db.
shpc-registry automated BioContainers addition for bioconductor-org.mxanthus.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.mxanthus.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.mxanthus.db:1.0.27--r43hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.mxanthus.db/1.0.27--r43hdfd78af_9
$ module help quay.io/biocontainers/bioconductor-org.mxanthus.db/1.0.27--r43hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.mxanthus.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.mxanthus.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.mxanthus.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.mxanthus.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.mxanthus.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.mxanthus.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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