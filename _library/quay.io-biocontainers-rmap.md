---
layout: container
name:  "quay.io/biocontainers/rmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rmap/container.yaml"
updated_at: "2025-02-12 03:18:39.696739"
latest: "2.1--h2d50403_1"
container_url: "https://biocontainers.pro/tools/rmap"
aliases:
 - "bedoverlap"
 - "binreads"
 - "deadzones"
 - "mapsifter"
 - "rmap"
 - "rmap-pe"
 - "rmapbs"
 - "rmapbs-pe"
 - "sigoverlap"
 - "simreads"
 - "simreadsbs"
 - "simreadspe"
 - "extractseq"
versions:
 - "2.1--h2d50403_1"
description: "shpc-registry automated BioContainers addition for rmap"
config: {"url": "https://biocontainers.pro/tools/rmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rmap", "latest": {"2.1--h2d50403_1": "sha256:42953f59f6f9fa137ae402da4842c2be733fe268a131ac2bf706a8afb27647a8"}, "tags": {"2.1--h2d50403_1": "sha256:42953f59f6f9fa137ae402da4842c2be733fe268a131ac2bf706a8afb27647a8"}, "docker": "quay.io/biocontainers/rmap", "aliases": {"bedoverlap": "/usr/local/bin/bedoverlap", "binreads": "/usr/local/bin/binreads", "deadzones": "/usr/local/bin/deadzones", "mapsifter": "/usr/local/bin/mapsifter", "rmap": "/usr/local/bin/rmap", "rmap-pe": "/usr/local/bin/rmap-pe", "rmapbs": "/usr/local/bin/rmapbs", "rmapbs-pe": "/usr/local/bin/rmapbs-pe", "sigoverlap": "/usr/local/bin/sigoverlap", "simreads": "/usr/local/bin/simreads", "simreadsbs": "/usr/local/bin/simreadsbs", "simreadspe": "/usr/local/bin/simreadspe", "extractseq": "/usr/local/bin/extractseq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rmap.
shpc-registry automated BioContainers addition for rmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rmap:2.1--h2d50403_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rmap/2.1--h2d50403_1
$ module help quay.io/biocontainers/rmap/2.1--h2d50403_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedoverlap

```bash
$ singularity exec <container> /usr/local/bin/bedoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/bedoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### binreads

```bash
$ singularity exec <container> /usr/local/bin/binreads
$ podman run --it --rm --entrypoint /usr/local/bin/binreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deadzones

```bash
$ singularity exec <container> /usr/local/bin/deadzones
$ podman run --it --rm --entrypoint /usr/local/bin/deadzones   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deadzones   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapsifter

```bash
$ singularity exec <container> /usr/local/bin/mapsifter
$ podman run --it --rm --entrypoint /usr/local/bin/mapsifter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapsifter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmap

```bash
$ singularity exec <container> /usr/local/bin/rmap
$ podman run --it --rm --entrypoint /usr/local/bin/rmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmap-pe

```bash
$ singularity exec <container> /usr/local/bin/rmap-pe
$ podman run --it --rm --entrypoint /usr/local/bin/rmap-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmap-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmapbs

```bash
$ singularity exec <container> /usr/local/bin/rmapbs
$ podman run --it --rm --entrypoint /usr/local/bin/rmapbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmapbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmapbs-pe

```bash
$ singularity exec <container> /usr/local/bin/rmapbs-pe
$ podman run --it --rm --entrypoint /usr/local/bin/rmapbs-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmapbs-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sigoverlap

```bash
$ singularity exec <container> /usr/local/bin/sigoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/sigoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sigoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreads

```bash
$ singularity exec <container> /usr/local/bin/simreads
$ podman run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreadsbs

```bash
$ singularity exec <container> /usr/local/bin/simreadsbs
$ podman run --it --rm --entrypoint /usr/local/bin/simreadsbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreadsbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreadspe

```bash
$ singularity exec <container> /usr/local/bin/simreadspe
$ podman run --it --rm --entrypoint /usr/local/bin/simreadspe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreadspe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractseq

```bash
$ singularity exec <container> /usr/local/bin/extractseq
$ podman run --it --rm --entrypoint /usr/local/bin/extractseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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