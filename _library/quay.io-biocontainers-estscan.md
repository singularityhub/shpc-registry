---
layout: container
name:  "quay.io/biocontainers/estscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/estscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/estscan/container.yaml"
updated_at: "2023-02-22 03:29:44.960306"
latest: "3.0--hec16e2b_5"
container_url: "https://biocontainers.pro/tools/estscan"
aliases:
 - "estscan"
versions:
 - "3.0--hec16e2b_5"
description: "shpc-registry automated BioContainers addition for estscan"
config: {"url": "https://biocontainers.pro/tools/estscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for estscan", "latest": {"3.0--hec16e2b_5": "sha256:e1cae8e2e2a630e0874baf23b795a4474cc63a04f2839534d36c5c4b8f839892"}, "tags": {"3.0--hec16e2b_5": "sha256:e1cae8e2e2a630e0874baf23b795a4474cc63a04f2839534d36c5c4b8f839892"}, "docker": "quay.io/biocontainers/estscan", "aliases": {"estscan": "/usr/local/bin/estscan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/estscan.
shpc-registry automated BioContainers addition for estscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/estscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/estscan:3.0--hec16e2b_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/estscan/3.0--hec16e2b_5
$ module help quay.io/biocontainers/estscan/3.0--hec16e2b_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### estscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### estscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### estscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### estscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### estscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### estscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### estscan

```bash
$ singularity exec <container> /usr/local/bin/estscan
$ podman run --it --rm --entrypoint /usr/local/bin/estscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estscan   -v ${PWD} -w ${PWD} <container> -c " $@"
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