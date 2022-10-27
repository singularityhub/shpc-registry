---
layout: container
name:  "quay.io/biocontainers/semeta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/semeta/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/semeta/container.yaml"
updated_at: "2022-10-27 01:05:25.487327"
latest: "1.0--0"
container_url: "https://biocontainers.pro/tools/semeta"
aliases:
 - ".semeta-post-link.sh"
 - "SeMeta_Assign"
 - "SeMeta_Cluster"
 - "config.conf"
versions:
 - "1.0--0"
description: "shpc-registry automated BioContainers addition for semeta"
config: {"url": "https://biocontainers.pro/tools/semeta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for semeta", "latest": {"1.0--0": "sha256:1a6859d197e0898c4364ddb2463e97426d8c631376ac23010dd3032409d8c240"}, "tags": {"1.0--0": "sha256:1a6859d197e0898c4364ddb2463e97426d8c631376ac23010dd3032409d8c240"}, "docker": "quay.io/biocontainers/semeta", "aliases": {".semeta-post-link.sh": "/usr/local/bin/.semeta-post-link.sh", "SeMeta_Assign": "/usr/local/bin/SeMeta_Assign", "SeMeta_Cluster": "/usr/local/bin/SeMeta_Cluster", "config.conf": "/usr/local/bin/config.conf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/semeta.
shpc-registry automated BioContainers addition for semeta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/semeta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/semeta:1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/semeta/1.0--0
$ module help quay.io/biocontainers/semeta/1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### semeta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### semeta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### semeta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### semeta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### semeta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### semeta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .semeta-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.semeta-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.semeta-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.semeta-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SeMeta_Assign

```bash
$ singularity exec <container> /usr/local/bin/SeMeta_Assign
$ podman run --it --rm --entrypoint /usr/local/bin/SeMeta_Assign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeMeta_Assign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SeMeta_Cluster

```bash
$ singularity exec <container> /usr/local/bin/SeMeta_Cluster
$ podman run --it --rm --entrypoint /usr/local/bin/SeMeta_Cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeMeta_Cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config.conf

```bash
$ singularity exec <container> /usr/local/bin/config.conf
$ podman run --it --rm --entrypoint /usr/local/bin/config.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
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