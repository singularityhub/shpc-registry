---
layout: container
name:  "quay.io/biocontainers/quaqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/quaqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/quaqc/container.yaml"
updated_at: "2025-11-03 04:10:49.519662"
latest: "1.5--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/quaqc"
aliases:
 - "quaqc"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.3d--h577a1d6_0"
 - "1.3d--h577a1d6_1"
 - "1.5--h577a1d6_0"
 - "1.4--h577a1d6_0"
description: "singularity registry hpc automated addition for quaqc"
config: {"url": "https://biocontainers.pro/tools/quaqc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for quaqc", "latest": {"1.5--h577a1d6_0": "sha256:e127075cf82490e508867c97d4d3f0b377c8131f904b34bc06685caa56f8acce"}, "tags": {"1.3d--h577a1d6_0": "sha256:6a3a5c6afaea221e2087aa9a54a2a0a9ff755668299b48699cb81285639a46fa", "1.3d--h577a1d6_1": "sha256:e4d924aa3ff79389b522bae80c79c6f2f861495d1b390d2144da462126589251", "1.5--h577a1d6_0": "sha256:e127075cf82490e508867c97d4d3f0b377c8131f904b34bc06685caa56f8acce", "1.4--h577a1d6_0": "sha256:be72be2034316dd50c62ebf6c03cd53d5e2e9ab141cbb251c84b1fed2d334cec"}, "docker": "quay.io/biocontainers/quaqc", "aliases": {"quaqc": "/usr/local/bin/quaqc", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/quaqc.
singularity registry hpc automated addition for quaqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/quaqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/quaqc:1.5--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/quaqc/1.5--h577a1d6_0
$ module help quay.io/biocontainers/quaqc/1.5--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quaqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quaqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quaqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quaqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quaqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quaqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### quaqc

```bash
$ singularity exec <container> /usr/local/bin/quaqc
$ podman run --it --rm --entrypoint /usr/local/bin/quaqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quaqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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