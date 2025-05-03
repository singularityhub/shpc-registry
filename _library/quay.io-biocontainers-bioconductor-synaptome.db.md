---
layout: container
name:  "quay.io/biocontainers/bioconductor-synaptome.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synaptome.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synaptome.db/container.yaml"
updated_at: "2025-05-03 03:37:56.260346"
latest: "0.99.16--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-synaptome.db"
aliases:
 - "glpsol"
versions:
 - "0.99.8--r41hdfd78af_1"
 - "0.99.12--r42hdfd78af_0"
 - "0.99.12--r43hdfd78af_1"
 - "0.99.15--r43hdfd78af_0"
 - "0.99.16--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-synaptome.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synaptome.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synaptome.db", "latest": {"0.99.16--r44hdfd78af_0": "sha256:b9f8ea92b9070bf623e29a0804df420350cafece0f6afea74be381cf50885bce"}, "tags": {"0.99.8--r41hdfd78af_1": "sha256:2d453fdef720b1037f3e36272cd38f34a4e2fc5fb2ca92011f44c271f37c063f", "0.99.12--r42hdfd78af_0": "sha256:8f1b7fe30bb9916aacf08bc7165fde57d299081804363b4245006054bc2c7d9d", "0.99.12--r43hdfd78af_1": "sha256:0944222026352a79cd014c28db4914b162f3eeabbf1a8a2b6e66e62807bc4f14", "0.99.15--r43hdfd78af_0": "sha256:b226f17f37bcb70068ca79e60e97c908dbd5e188778a7335c449bb177ed99d35", "0.99.16--r44hdfd78af_0": "sha256:b9f8ea92b9070bf623e29a0804df420350cafece0f6afea74be381cf50885bce"}, "docker": "quay.io/biocontainers/bioconductor-synaptome.db", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synaptome.db.
shpc-registry automated BioContainers addition for bioconductor-synaptome.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synaptome.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synaptome.db:0.99.16--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synaptome.db/0.99.16--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-synaptome.db/0.99.16--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synaptome.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synaptome.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synaptome.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synaptome.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synaptome.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synaptome.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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