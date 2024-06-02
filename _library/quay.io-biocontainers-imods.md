---
layout: container
name:  "quay.io/biocontainers/imods"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/imods/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/imods/container.yaml"
updated_at: "2024-06-02 02:38:56.509392"
latest: "1.0.4--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/imods"
aliases:
 - "imc"
 - "imode_gcc"
 - "imodview"
 - "imove"
versions:
 - "1.0.4--h9ee0642_2"
 - "1.0.4--h9ee0642_3"
description: "singularity registry hpc automated addition for imods"
config: {"url": "https://biocontainers.pro/tools/imods", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for imods", "latest": {"1.0.4--h9ee0642_3": "sha256:30a1caf3c275295807d3524e954733b1bc46dcc247fd698a8033f3be817c90fb"}, "tags": {"1.0.4--h9ee0642_2": "sha256:8d80e4d866d798c252838089bde35ec1d105e2bc03aca731802f0cc64cb15718", "1.0.4--h9ee0642_3": "sha256:30a1caf3c275295807d3524e954733b1bc46dcc247fd698a8033f3be817c90fb"}, "docker": "quay.io/biocontainers/imods", "aliases": {"imc": "/usr/local/bin/imc", "imode_gcc": "/usr/local/bin/imode_gcc", "imodview": "/usr/local/bin/imodview", "imove": "/usr/local/bin/imove"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/imods.
singularity registry hpc automated addition for imods
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/imods
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/imods:1.0.4--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/imods/1.0.4--h9ee0642_3
$ module help quay.io/biocontainers/imods/1.0.4--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### imods-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### imods-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### imods-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### imods-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### imods-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### imods-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### imc

```bash
$ singularity exec <container> /usr/local/bin/imc
$ podman run --it --rm --entrypoint /usr/local/bin/imc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imode_gcc

```bash
$ singularity exec <container> /usr/local/bin/imode_gcc
$ podman run --it --rm --entrypoint /usr/local/bin/imode_gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imode_gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imodview

```bash
$ singularity exec <container> /usr/local/bin/imodview
$ podman run --it --rm --entrypoint /usr/local/bin/imodview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imodview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imove

```bash
$ singularity exec <container> /usr/local/bin/imove
$ podman run --it --rm --entrypoint /usr/local/bin/imove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imove   -v ${PWD} -w ${PWD} <container> -c " $@"
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