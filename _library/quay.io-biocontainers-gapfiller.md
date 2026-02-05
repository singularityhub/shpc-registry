---
layout: container
name:  "quay.io/biocontainers/gapfiller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gapfiller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gapfiller/container.yaml"
updated_at: "2026-02-05 05:08:35.874991"
latest: "2.1.2--h7ff8a90_4"
container_url: "https://biocontainers.pro/tools/gapfiller"
aliases:
 - "GapFiller"
versions:
 - "2.1.2--h7ff8a90_3"
 - "2.1.2--h7ff8a90_4"
description: "shpc-registry automated BioContainers addition for gapfiller"
config: {"url": "https://biocontainers.pro/tools/gapfiller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gapfiller", "latest": {"2.1.2--h7ff8a90_4": "sha256:d4b99648da52e325ae894f03f57904dc8eff8d29843c499fbfdc70ef36038b9f"}, "tags": {"2.1.2--h7ff8a90_3": "sha256:a5e07022c9eeb8029b1ee571ba5214a1a3806f763ea02448586cdd336623fe60", "2.1.2--h7ff8a90_4": "sha256:d4b99648da52e325ae894f03f57904dc8eff8d29843c499fbfdc70ef36038b9f"}, "docker": "quay.io/biocontainers/gapfiller", "aliases": {"GapFiller": "/usr/local/bin/GapFiller"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gapfiller.
shpc-registry automated BioContainers addition for gapfiller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gapfiller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gapfiller:2.1.2--h7ff8a90_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gapfiller/2.1.2--h7ff8a90_4
$ module help quay.io/biocontainers/gapfiller/2.1.2--h7ff8a90_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gapfiller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gapfiller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gapfiller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gapfiller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gapfiller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gapfiller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GapFiller

```bash
$ singularity exec <container> /usr/local/bin/GapFiller
$ podman run --it --rm --entrypoint /usr/local/bin/GapFiller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GapFiller   -v ${PWD} -w ${PWD} <container> -c " $@"
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