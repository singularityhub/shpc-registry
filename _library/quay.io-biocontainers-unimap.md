---
layout: container
name:  "quay.io/biocontainers/unimap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unimap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unimap/container.yaml"
updated_at: "2025-09-03 03:43:44.153461"
latest: "0.1--h577a1d6_5"
container_url: "https://biocontainers.pro/tools/unimap"
aliases:
 - "unimap"
versions:
 - "0.1--h7132678_2"
 - "0.1--h7132678_3"
 - "0.1--he4a0461_4"
 - "0.1--h577a1d6_5"
description: "shpc-registry automated BioContainers addition for unimap"
config: {"url": "https://biocontainers.pro/tools/unimap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unimap", "latest": {"0.1--h577a1d6_5": "sha256:95f846f5f473390f0432743037acc98d73092a3445e881d9ccdc9c2ae2294674"}, "tags": {"0.1--h7132678_2": "sha256:d38a8e17efd24ce27b17113fc1dd206039ae3d25d74290ce37c95c09d7848bbf", "0.1--h7132678_3": "sha256:cbb45aed837fed6860b22e3a2bf39f3e26644ba7c5f6c3391085cabc54116f0c", "0.1--he4a0461_4": "sha256:0185a8feeb73398a24f845f85639eb78f87156be3a4a424ca9668ec9df3f3bd8", "0.1--h577a1d6_5": "sha256:95f846f5f473390f0432743037acc98d73092a3445e881d9ccdc9c2ae2294674"}, "docker": "quay.io/biocontainers/unimap", "aliases": {"unimap": "/usr/local/bin/unimap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unimap.
shpc-registry automated BioContainers addition for unimap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unimap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unimap:0.1--h577a1d6_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unimap/0.1--h577a1d6_5
$ module help quay.io/biocontainers/unimap/0.1--h577a1d6_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unimap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unimap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unimap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unimap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unimap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unimap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unimap

```bash
$ singularity exec <container> /usr/local/bin/unimap
$ podman run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unimap   -v ${PWD} -w ${PWD} <container> -c " $@"
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