---
layout: container
name:  "quay.io/biocontainers/bioconductor-mpedbarray.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mpedbarray.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mpedbarray.db/container.yaml"
updated_at: "2026-01-20 04:38:14.706210"
latest: "3.2.3--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-mpedbarray.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r43hdfd78af_13"
 - "3.2.3--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-mpedbarray.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mpedbarray.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mpedbarray.db", "latest": {"3.2.3--r44hdfd78af_14": "sha256:31b0fa08dc54ed14cdebe6034dd321d4aaf9d18a2c0ac9b654b8e5b3eeba39fb"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:5d802f7ada010a58f587fa11e07074e7cdf75d56de0e2637f8ac3f6d04bd06fa", "3.2.3--r42hdfd78af_11": "sha256:096a8c798db80b88ad0cc6a418d29b3b882657036fac1135f09885ba3dea8da4", "3.2.3--r43hdfd78af_12": "sha256:841428ee33a0227ed66a63fca33e3c432d7d61ae48571733d3710e7f678a657d", "3.2.3--r43hdfd78af_13": "sha256:4e0edbf07b85f24fa7da7794dd826e421adbf47dd69abfc87917538f58febd14", "3.2.3--r44hdfd78af_14": "sha256:31b0fa08dc54ed14cdebe6034dd321d4aaf9d18a2c0ac9b654b8e5b3eeba39fb"}, "docker": "quay.io/biocontainers/bioconductor-mpedbarray.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mpedbarray.db.
shpc-registry automated BioContainers addition for bioconductor-mpedbarray.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mpedbarray.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mpedbarray.db:3.2.3--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mpedbarray.db/3.2.3--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-mpedbarray.db/3.2.3--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mpedbarray.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpedbarray.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mpedbarray.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mpedbarray.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mpedbarray.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mpedbarray.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mpedbarray.db

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