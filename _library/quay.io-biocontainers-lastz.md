---
layout: container
name:  "quay.io/biocontainers/lastz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lastz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lastz/container.yaml"
updated_at: "2024-06-05 03:12:57.123992"
latest: "1.04.22--h031d066_0"
container_url: "https://biocontainers.pro/tools/lastz"
aliases:
 - "lastz"
 - "lastz_32"
 - "lastz_D"
versions:
 - "1.04.15--hec16e2b_1"
 - "1.04.15--h031d066_3"
 - "1.04.22--h031d066_0"
description: "shpc-registry automated BioContainers addition for lastz"
config: {"url": "https://biocontainers.pro/tools/lastz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lastz", "latest": {"1.04.22--h031d066_0": "sha256:8d2e3f87ddaf39481086c6726516242c6ee8d96190b1f0c0da7d0e455d525d00"}, "tags": {"1.04.15--hec16e2b_1": "sha256:bca1bdeabf63ea0c19eaf9128d2c5075a50400a594ee71e97e8ebf03c7661b89", "1.04.15--h031d066_3": "sha256:70dddce735229fa858b5dad176ab09baf82c63db1634694569f4a1d0da34afe6", "1.04.22--h031d066_0": "sha256:8d2e3f87ddaf39481086c6726516242c6ee8d96190b1f0c0da7d0e455d525d00"}, "docker": "quay.io/biocontainers/lastz", "aliases": {"lastz": "/usr/local/bin/lastz", "lastz_32": "/usr/local/bin/lastz_32", "lastz_D": "/usr/local/bin/lastz_D"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lastz.
shpc-registry automated BioContainers addition for lastz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lastz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lastz:1.04.22--h031d066_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lastz/1.04.22--h031d066_0
$ module help quay.io/biocontainers/lastz/1.04.22--h031d066_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lastz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lastz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lastz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lastz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lastz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lastz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lastz

```bash
$ singularity exec <container> /usr/local/bin/lastz
$ podman run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_32

```bash
$ singularity exec <container> /usr/local/bin/lastz_32
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_D

```bash
$ singularity exec <container> /usr/local/bin/lastz_D
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
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