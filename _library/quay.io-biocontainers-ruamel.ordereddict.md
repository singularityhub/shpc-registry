---
layout: container
name:  "quay.io/biocontainers/ruamel.ordereddict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ruamel.ordereddict/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ruamel.ordereddict/container.yaml"
updated_at: "2022-10-27 00:53:45.410997"
latest: "0.4.6--py27_0"
container_url: "https://biocontainers.pro/tools/ruamel.ordereddict"
aliases:
 - "smtpd.pyc"
versions:
 - "0.4.6--py27_0"
description: "shpc-registry automated BioContainers addition for ruamel.ordereddict"
config: {"url": "https://biocontainers.pro/tools/ruamel.ordereddict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ruamel.ordereddict", "latest": {"0.4.6--py27_0": "sha256:ba9d519b3b331dee0b24842bdab5dc0e41743b815f0d47b877c0a4b2b8b20f5d"}, "tags": {"0.4.6--py27_0": "sha256:ba9d519b3b331dee0b24842bdab5dc0e41743b815f0d47b877c0a4b2b8b20f5d"}, "docker": "quay.io/biocontainers/ruamel.ordereddict", "aliases": {"smtpd.pyc": "/usr/local/bin/smtpd.pyc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ruamel.ordereddict.
shpc-registry automated BioContainers addition for ruamel.ordereddict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ruamel.ordereddict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ruamel.ordereddict:0.4.6--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ruamel.ordereddict/0.4.6--py27_0
$ module help quay.io/biocontainers/ruamel.ordereddict/0.4.6--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ruamel.ordereddict-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ruamel.ordereddict-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ruamel.ordereddict-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ruamel.ordereddict-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ruamel.ordereddict-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruamel.ordereddict-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smtpd.pyc

```bash
$ singularity exec <container> /usr/local/bin/smtpd.pyc
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.pyc   -v ${PWD} -w ${PWD} <container> -c " $@"
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