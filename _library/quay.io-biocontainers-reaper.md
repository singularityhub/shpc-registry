---
layout: container
name:  "quay.io/biocontainers/reaper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reaper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reaper/container.yaml"
updated_at: "2024-02-08 02:51:01.573772"
latest: "16.098--hed695b0_3"
container_url: "https://biocontainers.pro/tools/reaper"
aliases:
 - "minion"
 - "reaper"
 - "swan"
 - "tally"
versions:
 - "16.098--hed695b0_3"
description: "shpc-registry automated BioContainers addition for reaper"
config: {"url": "https://biocontainers.pro/tools/reaper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for reaper", "latest": {"16.098--hed695b0_3": "sha256:3e3d06f406ea8de6182f20f2b9e217872174657488fdbc079167fe669d068d80"}, "tags": {"16.098--hed695b0_3": "sha256:3e3d06f406ea8de6182f20f2b9e217872174657488fdbc079167fe669d068d80"}, "docker": "quay.io/biocontainers/reaper", "aliases": {"minion": "/usr/local/bin/minion", "reaper": "/usr/local/bin/reaper", "swan": "/usr/local/bin/swan", "tally": "/usr/local/bin/tally"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reaper.
shpc-registry automated BioContainers addition for reaper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reaper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reaper:16.098--hed695b0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reaper/16.098--hed695b0_3
$ module help quay.io/biocontainers/reaper/16.098--hed695b0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reaper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reaper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reaper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reaper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reaper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reaper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minion

```bash
$ singularity exec <container> /usr/local/bin/minion
$ podman run --it --rm --entrypoint /usr/local/bin/minion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reaper

```bash
$ singularity exec <container> /usr/local/bin/reaper
$ podman run --it --rm --entrypoint /usr/local/bin/reaper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reaper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swan

```bash
$ singularity exec <container> /usr/local/bin/swan
$ podman run --it --rm --entrypoint /usr/local/bin/swan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tally

```bash
$ singularity exec <container> /usr/local/bin/tally
$ podman run --it --rm --entrypoint /usr/local/bin/tally   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tally   -v ${PWD} -w ${PWD} <container> -c " $@"
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