---
layout: container
name:  "quay.io/biocontainers/hmmratac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmratac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmmratac/container.yaml"
updated_at: "2022-10-27 00:41:38.105741"
latest: "1.2.9--0"
container_url: "https://biocontainers.pro/tools/hmmratac"
aliases:
 - "HMMRATAC"
versions:
 - "1.2.9--0"
description: "shpc-registry automated BioContainers addition for hmmratac"
config: {"url": "https://biocontainers.pro/tools/hmmratac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmratac", "latest": {"1.2.9--0": "sha256:be28c28d52f565b5fbc683a21324aea81c8d342b9eb6993aeb672ac1a0f8ff13"}, "tags": {"1.2.9--0": "sha256:be28c28d52f565b5fbc683a21324aea81c8d342b9eb6993aeb672ac1a0f8ff13"}, "docker": "quay.io/biocontainers/hmmratac", "aliases": {"HMMRATAC": "/usr/local/bin/HMMRATAC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmratac.
shpc-registry automated BioContainers addition for hmmratac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmratac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmratac:1.2.9--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmratac/1.2.9--0
$ module help quay.io/biocontainers/hmmratac/1.2.9--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmratac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmratac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmratac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmratac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmratac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmratac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HMMRATAC

```bash
$ singularity exec <container> /usr/local/bin/HMMRATAC
$ podman run --it --rm --entrypoint /usr/local/bin/HMMRATAC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HMMRATAC   -v ${PWD} -w ${PWD} <container> -c " $@"
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