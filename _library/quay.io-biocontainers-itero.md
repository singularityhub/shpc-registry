---
layout: container
name:  "quay.io/biocontainers/itero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/itero/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/itero/container.yaml"
updated_at: "2022-10-27 01:04:13.457388"
latest: "1.1.2--py_1"
container_url: "https://biocontainers.pro/tools/itero"
aliases:
 - "dipspades.py"
 - "gawk-5.0.1"
 - "itero"
 - "spades-dipspades-core"
versions:
 - "1.1.2--py_1"
description: "shpc-registry automated BioContainers addition for itero"
config: {"url": "https://biocontainers.pro/tools/itero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for itero", "latest": {"1.1.2--py_1": "sha256:a1f00e2670ec270fe4dea51820396de3a90da5ef836fc5e29ce18f499cb74fc5"}, "tags": {"1.1.2--py_1": "sha256:a1f00e2670ec270fe4dea51820396de3a90da5ef836fc5e29ce18f499cb74fc5"}, "docker": "quay.io/biocontainers/itero", "aliases": {"dipspades.py": "/usr/local/bin/dipspades.py", "gawk-5.0.1": "/usr/local/bin/gawk-5.0.1", "itero": "/usr/local/bin/itero", "spades-dipspades-core": "/usr/local/bin/spades-dipspades-core"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/itero.
shpc-registry automated BioContainers addition for itero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/itero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/itero:1.1.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/itero/1.1.2--py_1
$ module help quay.io/biocontainers/itero/1.1.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### itero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### itero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### itero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### itero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### itero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### itero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dipspades.py

```bash
$ singularity exec <container> /usr/local/bin/dipspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dipspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.0.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.0.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### itero

```bash
$ singularity exec <container> /usr/local/bin/itero
$ podman run --it --rm --entrypoint /usr/local/bin/itero   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/itero   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-dipspades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-dipspades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-dipspades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-dipspades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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