---
layout: container
name:  "quay.io/biocontainers/svim-asm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svim-asm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/svim-asm/container.yaml"
updated_at: "2022-10-27 00:44:28.702860"
latest: "1.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/svim-asm"
aliases:
 - "svim-asm"
versions:
 - "1.0.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for svim-asm"
config: {"url": "https://biocontainers.pro/tools/svim-asm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svim-asm", "latest": {"1.0.3--pyhdfd78af_0": "sha256:36494601b4cd59e2394f3ab52307a3db002b9faa137106ff6c81601d5287b022"}, "tags": {"1.0.3--pyhdfd78af_0": "sha256:36494601b4cd59e2394f3ab52307a3db002b9faa137106ff6c81601d5287b022"}, "docker": "quay.io/biocontainers/svim-asm", "aliases": {"svim-asm": "/usr/local/bin/svim-asm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svim-asm.
shpc-registry automated BioContainers addition for svim-asm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svim-asm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svim-asm:1.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svim-asm/1.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/svim-asm/1.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svim-asm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svim-asm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svim-asm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svim-asm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svim-asm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svim-asm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### svim-asm

```bash
$ singularity exec <container> /usr/local/bin/svim-asm
$ podman run --it --rm --entrypoint /usr/local/bin/svim-asm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svim-asm   -v ${PWD} -w ${PWD} <container> -c " $@"
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