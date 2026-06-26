---
layout: container
name:  "quay.io/biocontainers/mumu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mumu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mumu/container.yaml"
updated_at: "2026-06-26 07:01:01.870207"
latest: "1.1.4--hc52dbad_0"
container_url: "https://biocontainers.pro/tools/mumu"
aliases:
 - "mumu"
versions:
 - "1.1.4--hc52dbad_0"
description: "singularity registry hpc automated addition for mumu"
config: {"url": "https://biocontainers.pro/tools/mumu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mumu", "latest": {"1.1.4--hc52dbad_0": "sha256:560f683de7e0fb419ee8c94e44ff5440c36f7372eb669f99cda1cd1a10477d90"}, "tags": {"1.1.4--hc52dbad_0": "sha256:560f683de7e0fb419ee8c94e44ff5440c36f7372eb669f99cda1cd1a10477d90"}, "docker": "quay.io/biocontainers/mumu", "aliases": {"mumu": "/usr/local/bin/mumu"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mumu.
singularity registry hpc automated addition for mumu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mumu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mumu:1.1.4--hc52dbad_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mumu/1.1.4--hc52dbad_0
$ module help quay.io/biocontainers/mumu/1.1.4--hc52dbad_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mumu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mumu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mumu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mumu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mumu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mumu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mumu

```bash
$ singularity exec <container> /usr/local/bin/mumu
$ podman run --it --rm --entrypoint /usr/local/bin/mumu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mumu   -v ${PWD} -w ${PWD} <container> -c " $@"
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