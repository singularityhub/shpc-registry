---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgug4100a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgug4100a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgug4100a.db/container.yaml"
updated_at: "2023-09-23 02:57:39.240744"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgug4100a.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r41hdfd78af_10"
 - "3.2.3--r42hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgug4100a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgug4100a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgug4100a.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:29a6fc4c405f580e65b392afed34a04475b801fab53e7e2cb13103143312d331"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:9d5ad7626eed7e1432adf8c40ca6db3c46379dfdaaf992617fd4d233fbe7941f", "3.2.3--r41hdfd78af_10": "sha256:1332250c314c98f838a3376b367da036fb628bbad0104f0502256774f6a80536", "3.2.3--r42hdfd78af_11": "sha256:91ab33d095ff638ca41e618c7108f4b3605048df962ac7fe6458a79720e367fb", "3.2.3--r43hdfd78af_12": "sha256:29a6fc4c405f580e65b392afed34a04475b801fab53e7e2cb13103143312d331"}, "docker": "quay.io/biocontainers/bioconductor-hgug4100a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgug4100a.db.
shpc-registry automated BioContainers addition for bioconductor-hgug4100a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4100a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgug4100a.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgug4100a.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgug4100a.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgug4100a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4100a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgug4100a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgug4100a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgug4100a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgug4100a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgug4100a.db

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