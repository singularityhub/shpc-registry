---
layout: container
name:  "quay.io/biocontainers/samwell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samwell/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samwell/container.yaml"
updated_at: "2022-10-27 00:39:40.575766"
latest: "0.0.4--py39hbf8eff0_1"
container_url: "https://biocontainers.pro/tools/samwell"

versions:
 - "0.0.4--py39hbf8eff0_1"
description: "shpc-registry automated BioContainers addition for samwell"
config: {"url": "https://biocontainers.pro/tools/samwell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samwell", "latest": {"0.0.4--py39hbf8eff0_1": "sha256:4f02faf3cb58c793cd24e733143d8be372133c11f7fe06b7d60ae9837289237b"}, "tags": {"0.0.4--py39hbf8eff0_1": "sha256:4f02faf3cb58c793cd24e733143d8be372133c11f7fe06b7d60ae9837289237b"}, "docker": "quay.io/biocontainers/samwell"}
---

This module is a singularity container wrapper for quay.io/biocontainers/samwell.
shpc-registry automated BioContainers addition for samwell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samwell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samwell:0.0.4--py39hbf8eff0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samwell/0.0.4--py39hbf8eff0_1
$ module help quay.io/biocontainers/samwell/0.0.4--py39hbf8eff0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samwell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samwell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samwell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samwell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samwell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samwell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### samwell

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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