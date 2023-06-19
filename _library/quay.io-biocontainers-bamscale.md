---
layout: container
name:  "quay.io/biocontainers/bamscale"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamscale/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamscale/container.yaml"
updated_at: "2023-06-19 03:35:27.883685"
latest: "0.0.5--h37b53dd_8"
container_url: "https://biocontainers.pro/tools/bamscale"
aliases:
 - "BAMscale"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.0.5--h380da64_6"
 - "0.0.5--hccf09c8_7"
 - "0.0.5--h37b53dd_8"
description: "shpc-registry automated BioContainers addition for bamscale"
config: {"url": "https://biocontainers.pro/tools/bamscale", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamscale", "latest": {"0.0.5--h37b53dd_8": "sha256:0d9ec955ba1e5e41642506969bfec3da0243532daa1bb5acd09377dc422910db"}, "tags": {"0.0.5--h380da64_6": "sha256:980935848ed8757eccb5ffe7b6de82221b5516a53b8ecddac1dc99198f0ec45f", "0.0.5--hccf09c8_7": "sha256:7fdce2144d3c8ebf6946596760f4d47ef0b73a6892ba08d262eab4b0b518573e", "0.0.5--h37b53dd_8": "sha256:0d9ec955ba1e5e41642506969bfec3da0243532daa1bb5acd09377dc422910db"}, "docker": "quay.io/biocontainers/bamscale", "aliases": {"BAMscale": "/usr/local/bin/BAMscale", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamscale.
shpc-registry automated BioContainers addition for bamscale
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamscale
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamscale:0.0.5--h37b53dd_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamscale/0.0.5--h37b53dd_8
$ module help quay.io/biocontainers/bamscale/0.0.5--h37b53dd_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamscale-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamscale-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamscale-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamscale-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamscale-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamscale-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BAMscale

```bash
$ singularity exec <container> /usr/local/bin/BAMscale
$ podman run --it --rm --entrypoint /usr/local/bin/BAMscale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BAMscale   -v ${PWD} -w ${PWD} <container> -c " $@"
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