---
layout: container
name:  "quay.io/biocontainers/idemuxcpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/idemuxcpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/idemuxcpp/container.yaml"
updated_at: "2023-08-11 02:49:47.689287"
latest: "0.1.9--h2d38e66_2"
container_url: "https://biocontainers.pro/tools/idemuxcpp"
aliases:
 - "idemuxCPP"
 - "bamtools"
versions:
 - "0.1.9--h1b026d1_1"
 - "0.1.9--h2d38e66_2"
description: "shpc-registry automated BioContainers addition for idemuxcpp"
config: {"url": "https://biocontainers.pro/tools/idemuxcpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for idemuxcpp", "latest": {"0.1.9--h2d38e66_2": "sha256:12cfbb4286131838df322c2d4693d3610ada259d6602df6cc81cdf2ff947c414"}, "tags": {"0.1.9--h1b026d1_1": "sha256:6c5232a90868114fa3155d46c59dc10c0a7d7422d32d242493a94a894e29fa3d", "0.1.9--h2d38e66_2": "sha256:12cfbb4286131838df322c2d4693d3610ada259d6602df6cc81cdf2ff947c414"}, "docker": "quay.io/biocontainers/idemuxcpp", "aliases": {"idemuxCPP": "/usr/local/bin/idemuxCPP", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/idemuxcpp.
shpc-registry automated BioContainers addition for idemuxcpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/idemuxcpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/idemuxcpp:0.1.9--h2d38e66_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/idemuxcpp/0.1.9--h2d38e66_2
$ module help quay.io/biocontainers/idemuxcpp/0.1.9--h2d38e66_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### idemuxcpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### idemuxcpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### idemuxcpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### idemuxcpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### idemuxcpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### idemuxcpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idemuxCPP

```bash
$ singularity exec <container> /usr/local/bin/idemuxCPP
$ podman run --it --rm --entrypoint /usr/local/bin/idemuxCPP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idemuxCPP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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