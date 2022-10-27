---
layout: container
name:  "quay.io/biocontainers/python-chado"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-chado/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/python-chado/container.yaml"
updated_at: "2022-10-27 00:56:53.111847"
latest: "2.3.9--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/python-chado"
aliases:
 - "chakin"
versions:
 - "2.3.9--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for python-chado"
config: {"url": "https://biocontainers.pro/tools/python-chado", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-chado", "latest": {"2.3.9--pyh5e36f6f_0": "sha256:49ea8a2863267a08b11520a4f0c3d7eb7b92a90b212035588e63dc06325e3a00"}, "tags": {"2.3.9--pyh5e36f6f_0": "sha256:49ea8a2863267a08b11520a4f0c3d7eb7b92a90b212035588e63dc06325e3a00"}, "docker": "quay.io/biocontainers/python-chado", "aliases": {"chakin": "/usr/local/bin/chakin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-chado.
shpc-registry automated BioContainers addition for python-chado
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-chado
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-chado:2.3.9--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-chado/2.3.9--pyh5e36f6f_0
$ module help quay.io/biocontainers/python-chado/2.3.9--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-chado-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-chado-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-chado-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-chado-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-chado-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-chado-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chakin

```bash
$ singularity exec <container> /usr/local/bin/chakin
$ podman run --it --rm --entrypoint /usr/local/bin/chakin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chakin   -v ${PWD} -w ${PWD} <container> -c " $@"
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