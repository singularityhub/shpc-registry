---
layout: container
name:  "quay.io/biocontainers/sibelia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sibelia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sibelia/container.yaml"
updated_at: "2025-09-27 03:28:21.142061"
latest: "3.0.7--he1b5a44_2"
container_url: "https://biocontainers.pro/tools/sibelia"
aliases:
 - "C-Sibelia.py"
 - "Sibelia"
 - "snpEffAnnotate.py"
versions:
 - "3.0.7--he1b5a44_2"
description: "shpc-registry automated BioContainers addition for sibelia"
config: {"url": "https://biocontainers.pro/tools/sibelia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sibelia", "latest": {"3.0.7--he1b5a44_2": "sha256:98599ed0b20ff26aa59a76d685d0609f13ccbbb017f3920dc69b3b667115cfd9"}, "tags": {"3.0.7--he1b5a44_2": "sha256:98599ed0b20ff26aa59a76d685d0609f13ccbbb017f3920dc69b3b667115cfd9"}, "docker": "quay.io/biocontainers/sibelia", "aliases": {"C-Sibelia.py": "/usr/local/bin/C-Sibelia.py", "Sibelia": "/usr/local/bin/Sibelia", "snpEffAnnotate.py": "/usr/local/bin/snpEffAnnotate.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sibelia.
shpc-registry automated BioContainers addition for sibelia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sibelia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sibelia:3.0.7--he1b5a44_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sibelia/3.0.7--he1b5a44_2
$ module help quay.io/biocontainers/sibelia/3.0.7--he1b5a44_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sibelia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sibelia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sibelia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sibelia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sibelia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sibelia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### C-Sibelia.py

```bash
$ singularity exec <container> /usr/local/bin/C-Sibelia.py
$ podman run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/C-Sibelia.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sibelia

```bash
$ singularity exec <container> /usr/local/bin/Sibelia
$ podman run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sibelia   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEffAnnotate.py

```bash
$ singularity exec <container> /usr/local/bin/snpEffAnnotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEffAnnotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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