---
layout: container
name:  "quay.io/biocontainers/bioconductor-bambu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bambu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bambu/container.yaml"
updated_at: "2022-11-21 13:06:39.272584"
latest: "3.0.1--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bambu"
aliases:
 - "xgboost"
versions:
 - "2.0.6--r41hc247a5b_1"
 - "3.0.1--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bambu"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bambu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bambu", "latest": {"3.0.1--r42hc247a5b_0": "sha256:15e9236ba5abe34941a3106b28684765c37748b82e9722811a1b4e6749b21304"}, "tags": {"2.0.6--r41hc247a5b_1": "sha256:dc456fb2c0abfeb865104670cade38e62205daeb15347b24fe5c3f0d4d9b93d5", "3.0.1--r42hc247a5b_0": "sha256:15e9236ba5abe34941a3106b28684765c37748b82e9722811a1b4e6749b21304"}, "docker": "quay.io/biocontainers/bioconductor-bambu", "aliases": {"xgboost": "/usr/local/bin/xgboost"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bambu.
shpc-registry automated BioContainers addition for bioconductor-bambu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bambu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bambu:3.0.1--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bambu/3.0.1--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-bambu/3.0.1--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bambu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bambu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bambu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bambu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bambu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bambu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
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