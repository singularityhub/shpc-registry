---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgug4104a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgug4104a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgug4104a.db/container.yaml"
updated_at: "2023-09-15 02:40:18.459203"
latest: "3.2.3--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mgug4104a.db"

versions:
 - "3.2.3--r41hdfd78af_8"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mgug4104a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgug4104a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgug4104a.db", "latest": {"3.2.3--r43hdfd78af_11": "sha256:4a47603ceed1bbe0db86fcce249cfe136214e880877f79bcfd01c6a073ee183d"}, "tags": {"3.2.3--r41hdfd78af_8": "sha256:9b6866ced32dfdbfd5be8587b5ec66f9d11fb2a390f0fc0a76eda93d79a8d185", "3.2.3--r42hdfd78af_10": "sha256:edf452501f8a984ea061b21a740df0093898b69d2c260f24ac1fcba3ba78a91d", "3.2.3--r43hdfd78af_11": "sha256:4a47603ceed1bbe0db86fcce249cfe136214e880877f79bcfd01c6a073ee183d"}, "docker": "quay.io/biocontainers/bioconductor-mgug4104a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgug4104a.db.
shpc-registry automated BioContainers addition for bioconductor-mgug4104a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgug4104a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgug4104a.db:3.2.3--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgug4104a.db/3.2.3--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mgug4104a.db/3.2.3--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgug4104a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgug4104a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgug4104a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgug4104a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgug4104a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgug4104a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgug4104a.db

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