---
layout: container
name:  "quay.io/biocontainers/wtdbg2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wtdbg2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wtdbg2/container.yaml"
updated_at: "2025-01-23 03:33:19.501976"
latest: "2.0--h470a237_0"
container_url: "https://biocontainers.pro/tools/wtdbg2"
aliases:
 - "wtdbg-cns"
 - "wtdbg2"
 - "wtpoa-cns"
versions:
 - "2.0--h470a237_0"
description: "shpc-registry automated BioContainers addition for wtdbg2"
config: {"url": "https://biocontainers.pro/tools/wtdbg2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wtdbg2", "latest": {"2.0--h470a237_0": "sha256:acf11e19c6c431ca2ccb0270554e5a76087b5b650c150bf67dcd5f25f782bdfa"}, "tags": {"2.0--h470a237_0": "sha256:acf11e19c6c431ca2ccb0270554e5a76087b5b650c150bf67dcd5f25f782bdfa"}, "docker": "quay.io/biocontainers/wtdbg2", "aliases": {"wtdbg-cns": "/usr/local/bin/wtdbg-cns", "wtdbg2": "/usr/local/bin/wtdbg2", "wtpoa-cns": "/usr/local/bin/wtpoa-cns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wtdbg2.
shpc-registry automated BioContainers addition for wtdbg2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wtdbg2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wtdbg2:2.0--h470a237_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wtdbg2/2.0--h470a237_0
$ module help quay.io/biocontainers/wtdbg2/2.0--h470a237_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wtdbg2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wtdbg2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wtdbg2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wtdbg2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wtdbg2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wtdbg2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wtdbg-cns

```bash
$ singularity exec <container> /usr/local/bin/wtdbg-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtdbg2

```bash
$ singularity exec <container> /usr/local/bin/wtdbg2
$ podman run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtdbg2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtpoa-cns

```bash
$ singularity exec <container> /usr/local/bin/wtpoa-cns
$ podman run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wtpoa-cns   -v ${PWD} -w ${PWD} <container> -c " $@"
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