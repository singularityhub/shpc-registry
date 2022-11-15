---
layout: container
name:  "quay.io/biocontainers/hifiasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hifiasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hifiasm/container.yaml"
updated_at: "2022-11-14 23:56:47.795764"
latest: "0.9--h8b12597_0"
container_url: "https://biocontainers.pro/tools/hifiasm"
aliases:
 - "hifiasm"
versions:
 - "0.9--h8b12597_0"
description: "shpc-registry automated BioContainers addition for hifiasm"
config: {"url": "https://biocontainers.pro/tools/hifiasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hifiasm", "latest": {"0.9--h8b12597_0": "sha256:d3e1ccc462ae75a00b8c4eab3ec8d5d8335fd7eda7576d1d5c0418e2555cd507"}, "tags": {"0.9--h8b12597_0": "sha256:d3e1ccc462ae75a00b8c4eab3ec8d5d8335fd7eda7576d1d5c0418e2555cd507"}, "docker": "quay.io/biocontainers/hifiasm", "aliases": {"hifiasm": "/usr/local/bin/hifiasm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hifiasm.
shpc-registry automated BioContainers addition for hifiasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hifiasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hifiasm:0.9--h8b12597_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hifiasm/0.9--h8b12597_0
$ module help quay.io/biocontainers/hifiasm/0.9--h8b12597_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hifiasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hifiasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hifiasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hifiasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hifiasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hifiasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hifiasm

```bash
$ singularity exec <container> /usr/local/bin/hifiasm
$ podman run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
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