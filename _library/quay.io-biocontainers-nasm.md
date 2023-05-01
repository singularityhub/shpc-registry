---
layout: container
name:  "quay.io/biocontainers/nasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nasm/container.yaml"
updated_at: "2023-05-01 03:47:37.940280"
latest: "2.11.08--0"
container_url: "https://biocontainers.pro/tools/nasm"
aliases:
 - "nasm"
 - "ndisasm"
versions:
 - "2.11.08--0"
description: "shpc-registry automated BioContainers addition for nasm"
config: {"url": "https://biocontainers.pro/tools/nasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nasm", "latest": {"2.11.08--0": "sha256:3ab599f56c500d09698c2f6bd54b460a62c8acd870edb0fa07acf38b3627aa18"}, "tags": {"2.11.08--0": "sha256:3ab599f56c500d09698c2f6bd54b460a62c8acd870edb0fa07acf38b3627aa18"}, "docker": "quay.io/biocontainers/nasm", "aliases": {"nasm": "/usr/local/bin/nasm", "ndisasm": "/usr/local/bin/ndisasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nasm.
shpc-registry automated BioContainers addition for nasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nasm:2.11.08--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nasm/2.11.08--0
$ module help quay.io/biocontainers/nasm/2.11.08--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nasm

```bash
$ singularity exec <container> /usr/local/bin/nasm
$ podman run --it --rm --entrypoint /usr/local/bin/nasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndisasm

```bash
$ singularity exec <container> /usr/local/bin/ndisasm
$ podman run --it --rm --entrypoint /usr/local/bin/ndisasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndisasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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