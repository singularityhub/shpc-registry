---
layout: container
name:  "quay.io/biocontainers/ir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ir/container.yaml"
updated_at: "2024-12-20 03:24:28.813413"
latest: "2.8.0--h031d066_6"
container_url: "https://biocontainers.pro/tools/ir"
aliases:
 - "ir"
versions:
 - "2.8.0--hec16e2b_4"
 - "2.8.0--hec16e2b_5"
 - "2.8.0--h031d066_6"
description: "shpc-registry automated BioContainers addition for ir"
config: {"url": "https://biocontainers.pro/tools/ir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ir", "latest": {"2.8.0--h031d066_6": "sha256:94ebabf6c337139a96099b44996800777c13bb115b1c5549e16dc1782b6034ab"}, "tags": {"2.8.0--hec16e2b_4": "sha256:a705547b48500cdfa7f6926c11e4139e405a3b7f458ddae8768a43254a92e3b8", "2.8.0--hec16e2b_5": "sha256:d37e8e71d6764c068bdd86f13010d49c63401ac53efaee267f5a25e663d975ed", "2.8.0--h031d066_6": "sha256:94ebabf6c337139a96099b44996800777c13bb115b1c5549e16dc1782b6034ab"}, "docker": "quay.io/biocontainers/ir", "aliases": {"ir": "/usr/local/bin/ir"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ir.
shpc-registry automated BioContainers addition for ir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ir:2.8.0--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ir/2.8.0--h031d066_6
$ module help quay.io/biocontainers/ir/2.8.0--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ir

```bash
$ singularity exec <container> /usr/local/bin/ir
$ podman run --it --rm --entrypoint /usr/local/bin/ir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ir   -v ${PWD} -w ${PWD} <container> -c " $@"
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