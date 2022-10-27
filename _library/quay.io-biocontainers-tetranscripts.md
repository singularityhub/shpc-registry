---
layout: container
name:  "quay.io/biocontainers/tetranscripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tetranscripts/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tetranscripts/container.yaml"
updated_at: "2022-10-27 00:33:57.503271"
latest: "2.2.1--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/tetranscripts"
aliases:
 - "TEcount"
 - "TEtranscripts"
versions:
 - "2.2.1--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for tetranscripts"
config: {"url": "https://biocontainers.pro/tools/tetranscripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tetranscripts", "latest": {"2.2.1--pyh864c0ab_1": "sha256:bbe6f70f7f31dc3687d16ed1fad9f8b6e9415c805eb79db1bcc794361bc1a3e7"}, "tags": {"2.2.1--pyh864c0ab_1": "sha256:bbe6f70f7f31dc3687d16ed1fad9f8b6e9415c805eb79db1bcc794361bc1a3e7"}, "docker": "quay.io/biocontainers/tetranscripts", "aliases": {"TEcount": "/usr/local/bin/TEcount", "TEtranscripts": "/usr/local/bin/TEtranscripts"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tetranscripts.
shpc-registry automated BioContainers addition for tetranscripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tetranscripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tetranscripts:2.2.1--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tetranscripts/2.2.1--pyh864c0ab_1
$ module help quay.io/biocontainers/tetranscripts/2.2.1--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tetranscripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tetranscripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tetranscripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tetranscripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tetranscripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tetranscripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TEcount

```bash
$ singularity exec <container> /usr/local/bin/TEcount
$ podman run --it --rm --entrypoint /usr/local/bin/TEcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TEtranscripts

```bash
$ singularity exec <container> /usr/local/bin/TEtranscripts
$ podman run --it --rm --entrypoint /usr/local/bin/TEtranscripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEtranscripts   -v ${PWD} -w ${PWD} <container> -c " $@"
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