---
layout: container
name:  "quay.io/biocontainers/staramr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staramr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/staramr/container.yaml"
updated_at: "2022-10-27 00:30:22.131208"
latest: "0.8.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/staramr"
aliases:
 - "file"
 - "green"
 - "green3"
 - "green3.10"
 - "mlst"
 - "staramr"
versions:
 - "0.8.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for staramr"
config: {"url": "https://biocontainers.pro/tools/staramr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for staramr", "latest": {"0.8.0--pyhdfd78af_1": "sha256:845264047df122c41e62d6236a2ddb0698f54ed893edbd56380544eb83ca5849"}, "tags": {"0.8.0--pyhdfd78af_1": "sha256:845264047df122c41e62d6236a2ddb0698f54ed893edbd56380544eb83ca5849"}, "docker": "quay.io/biocontainers/staramr", "aliases": {"file": "/usr/local/bin/file", "green": "/usr/local/bin/green", "green3": "/usr/local/bin/green3", "green3.10": "/usr/local/bin/green3.10", "mlst": "/usr/local/bin/mlst", "staramr": "/usr/local/bin/staramr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/staramr.
shpc-registry automated BioContainers addition for staramr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staramr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staramr:0.8.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staramr/0.8.0--pyhdfd78af_1
$ module help quay.io/biocontainers/staramr/0.8.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staramr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staramr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staramr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staramr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staramr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staramr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### file

```bash
$ singularity exec <container> /usr/local/bin/file
$ podman run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### green

```bash
$ singularity exec <container> /usr/local/bin/green
$ podman run --it --rm --entrypoint /usr/local/bin/green   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/green   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### green3

```bash
$ singularity exec <container> /usr/local/bin/green3
$ podman run --it --rm --entrypoint /usr/local/bin/green3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/green3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### green3.10

```bash
$ singularity exec <container> /usr/local/bin/green3.10
$ podman run --it --rm --entrypoint /usr/local/bin/green3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/green3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mlst

```bash
$ singularity exec <container> /usr/local/bin/mlst
$ podman run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mlst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### staramr

```bash
$ singularity exec <container> /usr/local/bin/staramr
$ podman run --it --rm --entrypoint /usr/local/bin/staramr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/staramr   -v ${PWD} -w ${PWD} <container> -c " $@"
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