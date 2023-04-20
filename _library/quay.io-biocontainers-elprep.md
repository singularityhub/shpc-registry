---
layout: container
name:  "quay.io/biocontainers/elprep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/elprep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/elprep/container.yaml"
updated_at: "2023-04-20 03:04:58.049690"
latest: "5.1.3--he881be0_0"
container_url: "https://biocontainers.pro/tools/elprep"
aliases:
 - "elprep"
versions:
 - "5.1.3--he881be0_0"
description: "shpc-registry automated BioContainers addition for elprep"
config: {"url": "https://biocontainers.pro/tools/elprep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for elprep", "latest": {"5.1.3--he881be0_0": "sha256:fbd786098aedf03a86128f7e91789b20edff85f5724eac5db982482de0b4813d"}, "tags": {"5.1.3--he881be0_0": "sha256:fbd786098aedf03a86128f7e91789b20edff85f5724eac5db982482de0b4813d"}, "docker": "quay.io/biocontainers/elprep", "aliases": {"elprep": "/usr/local/bin/elprep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/elprep.
shpc-registry automated BioContainers addition for elprep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/elprep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/elprep:5.1.3--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/elprep/5.1.3--he881be0_0
$ module help quay.io/biocontainers/elprep/5.1.3--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### elprep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### elprep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### elprep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### elprep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### elprep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elprep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### elprep

```bash
$ singularity exec <container> /usr/local/bin/elprep
$ podman run --it --rm --entrypoint /usr/local/bin/elprep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elprep   -v ${PWD} -w ${PWD} <container> -c " $@"
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