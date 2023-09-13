---
layout: container
name:  "quay.io/biocontainers/heinz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/heinz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/heinz/container.yaml"
updated_at: "2023-09-13 02:48:49.607528"
latest: "2.0--he1b5a44_2"
container_url: "https://biocontainers.pro/tools/heinz"
aliases:
 - "dimacs-solver"
 - "dimacs-to-lgf"
 - "heinz"
 - "lemon-0.x-to-1.x.sh"
 - "lgf-gen"
 - "cbc"
 - "clp"
 - "glpsol"
versions:
 - "2.0--he1b5a44_2"
description: "shpc-registry automated BioContainers addition for heinz"
config: {"url": "https://biocontainers.pro/tools/heinz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for heinz", "latest": {"2.0--he1b5a44_2": "sha256:312eeb4f5fe35f30dbc0912245572e657db364e458e51ee888d788e80e9cc82a"}, "tags": {"2.0--he1b5a44_2": "sha256:312eeb4f5fe35f30dbc0912245572e657db364e458e51ee888d788e80e9cc82a"}, "docker": "quay.io/biocontainers/heinz", "aliases": {"dimacs-solver": "/usr/local/bin/dimacs-solver", "dimacs-to-lgf": "/usr/local/bin/dimacs-to-lgf", "heinz": "/usr/local/bin/heinz", "lemon-0.x-to-1.x.sh": "/usr/local/bin/lemon-0.x-to-1.x.sh", "lgf-gen": "/usr/local/bin/lgf-gen", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/heinz.
shpc-registry automated BioContainers addition for heinz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/heinz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/heinz:2.0--he1b5a44_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/heinz/2.0--he1b5a44_2
$ module help quay.io/biocontainers/heinz/2.0--he1b5a44_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### heinz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### heinz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### heinz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### heinz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### heinz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### heinz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dimacs-solver

```bash
$ singularity exec <container> /usr/local/bin/dimacs-solver
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-solver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dimacs-to-lgf

```bash
$ singularity exec <container> /usr/local/bin/dimacs-to-lgf
$ podman run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dimacs-to-lgf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heinz

```bash
$ singularity exec <container> /usr/local/bin/heinz
$ podman run --it --rm --entrypoint /usr/local/bin/heinz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heinz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lemon-0.x-to-1.x.sh

```bash
$ singularity exec <container> /usr/local/bin/lemon-0.x-to-1.x.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lemon-0.x-to-1.x.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lgf-gen

```bash
$ singularity exec <container> /usr/local/bin/lgf-gen
$ podman run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lgf-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
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