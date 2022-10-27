---
layout: container
name:  "quay.io/biocontainers/pyhalcyon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyhalcyon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pyhalcyon/container.yaml"
updated_at: "2022-10-27 00:54:25.572079"
latest: "0.1.1--py_0"
container_url: "https://biocontainers.pro/tools/pyhalcyon"
aliases:
 - "halcyon"
versions:
 - "0.1.1--py_0"
description: "shpc-registry automated BioContainers addition for pyhalcyon"
config: {"url": "https://biocontainers.pro/tools/pyhalcyon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyhalcyon", "latest": {"0.1.1--py_0": "sha256:dd8058f9a5d2e79b34d2ee8c6c97ff7a343a180bca9413110bdb0d6ed1231690"}, "tags": {"0.1.1--py_0": "sha256:dd8058f9a5d2e79b34d2ee8c6c97ff7a343a180bca9413110bdb0d6ed1231690"}, "docker": "quay.io/biocontainers/pyhalcyon", "aliases": {"halcyon": "/usr/local/bin/halcyon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyhalcyon.
shpc-registry automated BioContainers addition for pyhalcyon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyhalcyon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyhalcyon:0.1.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyhalcyon/0.1.1--py_0
$ module help quay.io/biocontainers/pyhalcyon/0.1.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyhalcyon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyhalcyon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyhalcyon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyhalcyon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyhalcyon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyhalcyon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### halcyon

```bash
$ singularity exec <container> /usr/local/bin/halcyon
$ podman run --it --rm --entrypoint /usr/local/bin/halcyon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halcyon   -v ${PWD} -w ${PWD} <container> -c " $@"
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