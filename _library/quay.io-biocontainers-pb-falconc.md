---
layout: container
name:  "quay.io/biocontainers/pb-falconc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pb-falconc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pb-falconc/container.yaml"
updated_at: "2025-03-01 03:37:30.386539"
latest: "1.15.0--h41535f3_3"
container_url: "https://biocontainers.pro/tools/pb-falconc"
aliases:
 - "falconc"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.15.0--h3279499_0"
 - "1.15.0--h3279499_1"
 - "1.15.0--haabb649_2"
 - "1.15.0--h41535f3_3"
description: "shpc-registry automated BioContainers addition for pb-falconc"
config: {"url": "https://biocontainers.pro/tools/pb-falconc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pb-falconc", "latest": {"1.15.0--h41535f3_3": "sha256:2bd25229e39d95bf999225fd59686d075a84dd4c42e37caa74e1e7d5a4529db0"}, "tags": {"1.15.0--h3279499_0": "sha256:305f8aee4ff4aa2fcb66f2417f2ae4e82cc00b2eac9b5eef5a4cb1673e00fa23", "1.15.0--h3279499_1": "sha256:d04b658176d97aeaddd7b419339d9194d6e40cb02cc4afba0555cf458d69a5db", "1.15.0--haabb649_2": "sha256:90cf14e741ebb5e9d4f8d67c31339ddd9bf972914701cba4676aa5306fa9a433", "1.15.0--h41535f3_3": "sha256:2bd25229e39d95bf999225fd59686d075a84dd4c42e37caa74e1e7d5a4529db0"}, "docker": "quay.io/biocontainers/pb-falconc", "aliases": {"falconc": "/usr/local/bin/falconc", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pb-falconc.
shpc-registry automated BioContainers addition for pb-falconc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pb-falconc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pb-falconc:1.15.0--h41535f3_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pb-falconc/1.15.0--h41535f3_3
$ module help quay.io/biocontainers/pb-falconc/1.15.0--h41535f3_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pb-falconc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pb-falconc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pb-falconc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pb-falconc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pb-falconc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pb-falconc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### falconc

```bash
$ singularity exec <container> /usr/local/bin/falconc
$ podman run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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