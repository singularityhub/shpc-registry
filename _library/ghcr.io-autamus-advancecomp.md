---
layout: container
name:  "ghcr.io/autamus/advancecomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/advancecomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/advancecomp/container.yaml"
updated_at: "2024-02-01 02:25:20.255226"
latest: "2.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/advancecomp"
aliases:
 - "advdef"
 - "advmng"
 - "advpng"
 - "advzip"
versions:
 - "2.1"
 - "latest"
description: "AdvanceCOMP is a set of cross-platform command line data (re-)compression tools."
config: {"docker": "ghcr.io/autamus/advancecomp", "url": "https://github.com/orgs/autamus/packages/container/package/advancecomp", "maintainer": "@vsoch", "description": "AdvanceCOMP is a set of cross-platform command line data (re-)compression tools.", "latest": {"2.1": "sha256:afa119f8df0887fdb6cf8afae6f6e48dc33d12d726d5b3064880cc096a095d5a"}, "tags": {"2.1": "sha256:afa119f8df0887fdb6cf8afae6f6e48dc33d12d726d5b3064880cc096a095d5a", "latest": "sha256:afa119f8df0887fdb6cf8afae6f6e48dc33d12d726d5b3064880cc096a095d5a"}, "aliases": {"advdef": "/opt/view/bin/advdef", "advmng": "/opt/view/bin/advmng", "advpng": "/opt/view/bin/advpng", "advzip": "/opt/view/bin/advzip"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/advancecomp.
AdvanceCOMP is a set of cross-platform command line data (re-)compression tools.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/advancecomp
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/advancecomp:2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/advancecomp/2.1
$ module help ghcr.io/autamus/advancecomp/2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### advancecomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### advancecomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### advancecomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### advancecomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### advancecomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### advancecomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### advdef

```bash
$ singularity exec <container> /opt/view/bin/advdef
$ podman run --it --rm --entrypoint /opt/view/bin/advdef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/advdef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### advmng

```bash
$ singularity exec <container> /opt/view/bin/advmng
$ podman run --it --rm --entrypoint /opt/view/bin/advmng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/advmng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### advpng

```bash
$ singularity exec <container> /opt/view/bin/advpng
$ podman run --it --rm --entrypoint /opt/view/bin/advpng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/advpng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### advzip

```bash
$ singularity exec <container> /opt/view/bin/advzip
$ podman run --it --rm --entrypoint /opt/view/bin/advzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/advzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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