---
layout: container
name:  "quay.io/biocontainers/bioconductor-rguatlas4k.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rguatlas4k.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rguatlas4k.db/container.yaml"
updated_at: "2024-08-06 03:04:28.441934"
latest: "3.2.3--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rguatlas4k.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rguatlas4k.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rguatlas4k.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rguatlas4k.db", "latest": {"3.2.3--r43hdfd78af_13": "sha256:640d12dd2037f8b3aad67425cfdc1f8d70f38a74df8182931913a6ccd2314db9"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:e0431d918120c3a827095b5b42403f3809da76dd780345e95329199bd8ed1e7e", "3.2.3--r42hdfd78af_11": "sha256:cbd66317c4ef8a4b99300ea9722a9688dd43e6ce1c426ba11ce95a9656f2a3aa", "3.2.3--r43hdfd78af_12": "sha256:899f1222b6ff8a49cf91b9c34e4a71f6892f2db3e0db77304b4378f37e5d27f8", "3.2.3--r43hdfd78af_13": "sha256:640d12dd2037f8b3aad67425cfdc1f8d70f38a74df8182931913a6ccd2314db9"}, "docker": "quay.io/biocontainers/bioconductor-rguatlas4k.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rguatlas4k.db.
shpc-registry automated BioContainers addition for bioconductor-rguatlas4k.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rguatlas4k.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rguatlas4k.db:3.2.3--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rguatlas4k.db/3.2.3--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rguatlas4k.db/3.2.3--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rguatlas4k.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rguatlas4k.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rguatlas4k.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rguatlas4k.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rguatlas4k.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rguatlas4k.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rguatlas4k.db

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