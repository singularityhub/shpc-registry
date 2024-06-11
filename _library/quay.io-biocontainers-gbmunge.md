---
layout: container
name:  "quay.io/biocontainers/gbmunge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gbmunge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gbmunge/container.yaml"
updated_at: "2024-06-11 04:59:35.497708"
latest: "2018.07.06--h031d066_6"
container_url: "https://biocontainers.pro/tools/gbmunge"
aliases:
 - "gbmunge"
versions:
 - "2018.07.06--hec16e2b_4"
 - "2018.07.06--hec16e2b_5"
 - "2018.07.06--h031d066_6"
description: "shpc-registry automated BioContainers addition for gbmunge"
config: {"url": "https://biocontainers.pro/tools/gbmunge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gbmunge", "latest": {"2018.07.06--h031d066_6": "sha256:d67c95024218bc55ed40265204689cf9450aa7710fae2a698528231ae7522394"}, "tags": {"2018.07.06--hec16e2b_4": "sha256:818cc218ed20d40030152ff0e960f73e1dc026ad44342597e0d15d61c4de1bc5", "2018.07.06--hec16e2b_5": "sha256:40f3d6c1a7d7b7ab201c9da15f726109c5e04978387bbbca8ec2c082272bc227", "2018.07.06--h031d066_6": "sha256:d67c95024218bc55ed40265204689cf9450aa7710fae2a698528231ae7522394"}, "docker": "quay.io/biocontainers/gbmunge", "aliases": {"gbmunge": "/usr/local/bin/gbmunge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gbmunge.
shpc-registry automated BioContainers addition for gbmunge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gbmunge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gbmunge:2018.07.06--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gbmunge/2018.07.06--h031d066_6
$ module help quay.io/biocontainers/gbmunge/2018.07.06--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gbmunge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gbmunge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gbmunge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gbmunge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gbmunge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gbmunge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gbmunge

```bash
$ singularity exec <container> /usr/local/bin/gbmunge
$ podman run --it --rm --entrypoint /usr/local/bin/gbmunge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbmunge   -v ${PWD} -w ${PWD} <container> -c " $@"
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