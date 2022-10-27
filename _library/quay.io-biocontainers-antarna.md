---
layout: container
name:  "quay.io/biocontainers/antarna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/antarna/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/antarna/container.yaml"
updated_at: "2022-10-27 01:14:50.557109"
latest: "2.0.1.2--py27_0"
container_url: "https://biocontainers.pro/tools/antarna"
aliases:
 - "antarna.py"
versions:
 - "2.0.1.2--py27_0"
description: "shpc-registry automated BioContainers addition for antarna"
config: {"url": "https://biocontainers.pro/tools/antarna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for antarna", "latest": {"2.0.1.2--py27_0": "sha256:fe5e4c16e3859fdc8260159949fc1773938aaac912ad654a5bc88fc235eee090"}, "tags": {"2.0.1.2--py27_0": "sha256:fe5e4c16e3859fdc8260159949fc1773938aaac912ad654a5bc88fc235eee090"}, "docker": "quay.io/biocontainers/antarna", "aliases": {"antarna.py": "/usr/local/bin/antarna.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/antarna.
shpc-registry automated BioContainers addition for antarna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/antarna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/antarna:2.0.1.2--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/antarna/2.0.1.2--py27_0
$ module help quay.io/biocontainers/antarna/2.0.1.2--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### antarna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### antarna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### antarna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### antarna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### antarna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### antarna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### antarna.py

```bash
$ singularity exec <container> /usr/local/bin/antarna.py
$ podman run --it --rm --entrypoint /usr/local/bin/antarna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antarna.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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