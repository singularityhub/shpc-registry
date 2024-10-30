---
layout: container
name:  "quay.io/biocontainers/bioconductor-mm24kresogen.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mm24kresogen.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mm24kresogen.db/container.yaml"
updated_at: "2024-10-30 15:44:04.113885"
latest: "2.5.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mm24kresogen.db"

versions:
 - "2.5.0--r41hdfd78af_9"
 - "2.5.0--r42hdfd78af_10"
 - "2.5.0--r43hdfd78af_11"
 - "2.5.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mm24kresogen.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mm24kresogen.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mm24kresogen.db", "latest": {"2.5.0--r43hdfd78af_12": "sha256:2fa734e017ee351412c8077b01df256cc2be44d5ca276a4f84cea17851f7bdce"}, "tags": {"2.5.0--r41hdfd78af_9": "sha256:b8adf6d2b488e157862d26d014c56860c6b1185b77e4ab91ad823f9a2c80577c", "2.5.0--r42hdfd78af_10": "sha256:2dcee8c579a225b1812ff6d017da1d3cebf7b735970f0d2872b4d12ecdc5d494", "2.5.0--r43hdfd78af_11": "sha256:ae131d9ba1cdc15e53eb8fe4ea325e319a4d7a2ad743422fddd69dc3e89a1ba6", "2.5.0--r43hdfd78af_12": "sha256:2fa734e017ee351412c8077b01df256cc2be44d5ca276a4f84cea17851f7bdce"}, "docker": "quay.io/biocontainers/bioconductor-mm24kresogen.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mm24kresogen.db.
shpc-registry automated BioContainers addition for bioconductor-mm24kresogen.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mm24kresogen.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mm24kresogen.db:2.5.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mm24kresogen.db/2.5.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mm24kresogen.db/2.5.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mm24kresogen.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mm24kresogen.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mm24kresogen.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mm24kresogen.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mm24kresogen.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mm24kresogen.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mm24kresogen.db

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