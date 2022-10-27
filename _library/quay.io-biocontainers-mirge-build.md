---
layout: container
name:  "quay.io/biocontainers/mirge-build"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirge-build/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mirge-build/container.yaml"
updated_at: "2022-10-27 00:59:43.245142"
latest: "0.0.1--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/mirge-build"
aliases:
 - "miRge-build"
 - "perl5.30.3"
versions:
 - "0.0.1--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for mirge-build"
config: {"url": "https://biocontainers.pro/tools/mirge-build", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirge-build", "latest": {"0.0.1--pyh3252c3a_0": "sha256:106ba135c277c7fcc6418a89e8d6c1525f614df75bff50d3830d625d55dbefc5"}, "tags": {"0.0.1--pyh3252c3a_0": "sha256:106ba135c277c7fcc6418a89e8d6c1525f614df75bff50d3830d625d55dbefc5"}, "docker": "quay.io/biocontainers/mirge-build", "aliases": {"miRge-build": "/usr/local/bin/miRge-build", "perl5.30.3": "/usr/local/bin/perl5.30.3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirge-build.
shpc-registry automated BioContainers addition for mirge-build
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirge-build
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirge-build:0.0.1--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirge-build/0.0.1--pyh3252c3a_0
$ module help quay.io/biocontainers/mirge-build/0.0.1--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirge-build-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirge-build-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirge-build-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirge-build-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirge-build-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirge-build-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miRge-build

```bash
$ singularity exec <container> /usr/local/bin/miRge-build
$ podman run --it --rm --entrypoint /usr/local/bin/miRge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.30.3

```bash
$ singularity exec <container> /usr/local/bin/perl5.30.3
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.30.3   -v ${PWD} -w ${PWD} <container> -c " $@"
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