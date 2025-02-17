---
layout: container
name:  "quay.io/biocontainers/nemo-age"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nemo-age/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nemo-age/container.yaml"
updated_at: "2025-02-17 03:42:35.875097"
latest: "0.30.0--h3053a90_5"
container_url: "https://biocontainers.pro/tools/nemo-age"
aliases:
 - "nemoage"
versions:
 - "0.30.0--h5e66344_2"
 - "0.30.0--h0432e7c_4"
 - "0.30.0--h3053a90_5"
description: "shpc-registry automated BioContainers addition for nemo-age"
config: {"url": "https://biocontainers.pro/tools/nemo-age", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nemo-age", "latest": {"0.30.0--h3053a90_5": "sha256:f85195f53b8c76da587f23f5d9abc509b822f81eb635d757990b68fd81fee35d"}, "tags": {"0.30.0--h5e66344_2": "sha256:7ecb7253220de4f755847332e05a2cd7719934614530b87a11ffd9744b14decb", "0.30.0--h0432e7c_4": "sha256:3749e78484bebfbacd8b6ca401baead04bdb7af890ccad427d85357e39dbd552", "0.30.0--h3053a90_5": "sha256:f85195f53b8c76da587f23f5d9abc509b822f81eb635d757990b68fd81fee35d"}, "docker": "quay.io/biocontainers/nemo-age", "aliases": {"nemoage": "/usr/local/bin/nemoage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nemo-age.
shpc-registry automated BioContainers addition for nemo-age
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nemo-age
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nemo-age:0.30.0--h3053a90_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nemo-age/0.30.0--h3053a90_5
$ module help quay.io/biocontainers/nemo-age/0.30.0--h3053a90_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nemo-age-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nemo-age-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nemo-age-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nemo-age-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nemo-age-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nemo-age-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nemoage

```bash
$ singularity exec <container> /usr/local/bin/nemoage
$ podman run --it --rm --entrypoint /usr/local/bin/nemoage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nemoage   -v ${PWD} -w ${PWD} <container> -c " $@"
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