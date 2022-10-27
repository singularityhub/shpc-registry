---
layout: container
name:  "quay.io/biocontainers/rgi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rgi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rgi/container.yaml"
updated_at: "2022-10-27 00:43:32.132065"
latest: "6.0.0--pyha8f3691_0"
container_url: "https://biocontainers.pro/tools/rgi"
aliases:
 - "ct-energy"
 - "ct2rnaml"
 - "filetype"
 - "h-num.pl"
 - "hybrid-min"
 - "hybrid-ss-min"
 - "melt.pl"
 - "rgi"
 - "ss-count.pl"
versions:
 - "6.0.0--pyha8f3691_0"
description: "shpc-registry automated BioContainers addition for rgi"
config: {"url": "https://biocontainers.pro/tools/rgi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rgi", "latest": {"6.0.0--pyha8f3691_0": "sha256:e65160a3b5a83fb0fdc03b3c32be37125bc5d6e546a27f0fd5fad81dd8f70af4"}, "tags": {"6.0.0--pyha8f3691_0": "sha256:e65160a3b5a83fb0fdc03b3c32be37125bc5d6e546a27f0fd5fad81dd8f70af4"}, "docker": "quay.io/biocontainers/rgi", "aliases": {"ct-energy": "/usr/local/bin/ct-energy", "ct2rnaml": "/usr/local/bin/ct2rnaml", "filetype": "/usr/local/bin/filetype", "h-num.pl": "/usr/local/bin/h-num.pl", "hybrid-min": "/usr/local/bin/hybrid-min", "hybrid-ss-min": "/usr/local/bin/hybrid-ss-min", "melt.pl": "/usr/local/bin/melt.pl", "rgi": "/usr/local/bin/rgi", "ss-count.pl": "/usr/local/bin/ss-count.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rgi.
shpc-registry automated BioContainers addition for rgi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rgi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rgi:6.0.0--pyha8f3691_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rgi/6.0.0--pyha8f3691_0
$ module help quay.io/biocontainers/rgi/6.0.0--pyha8f3691_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rgi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rgi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rgi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rgi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rgi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rgi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ct-energy

```bash
$ singularity exec <container> /usr/local/bin/ct-energy
$ podman run --it --rm --entrypoint /usr/local/bin/ct-energy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct-energy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2rnaml

```bash
$ singularity exec <container> /usr/local/bin/ct2rnaml
$ podman run --it --rm --entrypoint /usr/local/bin/ct2rnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2rnaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filetype

```bash
$ singularity exec <container> /usr/local/bin/filetype
$ podman run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filetype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h-num.pl

```bash
$ singularity exec <container> /usr/local/bin/h-num.pl
$ podman run --it --rm --entrypoint /usr/local/bin/h-num.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h-num.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybrid-min

```bash
$ singularity exec <container> /usr/local/bin/hybrid-min
$ podman run --it --rm --entrypoint /usr/local/bin/hybrid-min   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybrid-min   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hybrid-ss-min

```bash
$ singularity exec <container> /usr/local/bin/hybrid-ss-min
$ podman run --it --rm --entrypoint /usr/local/bin/hybrid-ss-min   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hybrid-ss-min   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### melt.pl

```bash
$ singularity exec <container> /usr/local/bin/melt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/melt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/melt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgi

```bash
$ singularity exec <container> /usr/local/bin/rgi
$ podman run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ss-count.pl

```bash
$ singularity exec <container> /usr/local/bin/ss-count.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ss-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ss-count.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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