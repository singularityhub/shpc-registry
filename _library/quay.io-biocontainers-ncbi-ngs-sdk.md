---
layout: container
name:  "quay.io/biocontainers/ncbi-ngs-sdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-ngs-sdk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-ngs-sdk/container.yaml"
updated_at: "2022-10-29 05:55:45.078425"
latest: "2.9.3--h550f44e_0"
container_url: "https://biocontainers.pro/tools/ncbi-ngs-sdk"
aliases:
 - "activate"
 - "conda"
 - "deactivate"
 - "derb"
 - "genbrk"
 - "gencfu"
 - "gencnval"
 - "gendict"
 - "genrb"
 - "iconv"
versions:
 - "2.9.3--h550f44e_0"
description: "shpc-registry automated BioContainers addition for ncbi-ngs-sdk"
config: {"url": "https://biocontainers.pro/tools/ncbi-ngs-sdk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-ngs-sdk", "latest": {"2.9.3--h550f44e_0": "sha256:1c812d0ca140f83a5d6ffe5ddcae56ba22b0ce1319c874e3e686eee3f3da4b4b"}, "tags": {"2.9.3--h550f44e_0": "sha256:1c812d0ca140f83a5d6ffe5ddcae56ba22b0ce1319c874e3e686eee3f3da4b4b"}, "docker": "quay.io/biocontainers/ncbi-ngs-sdk", "aliases": {"activate": "/usr/local/bin/activate", "conda": "/usr/local/bin/conda", "deactivate": "/usr/local/bin/deactivate", "derb": "/usr/local/bin/derb", "genbrk": "/usr/local/bin/genbrk", "gencfu": "/usr/local/bin/gencfu", "gencnval": "/usr/local/bin/gencnval", "gendict": "/usr/local/bin/gendict", "genrb": "/usr/local/bin/genrb", "iconv": "/usr/local/bin/iconv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-ngs-sdk.
shpc-registry automated BioContainers addition for ncbi-ngs-sdk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-ngs-sdk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-ngs-sdk:2.9.3--h550f44e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-ngs-sdk/2.9.3--h550f44e_0
$ module help quay.io/biocontainers/ncbi-ngs-sdk/2.9.3--h550f44e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-ngs-sdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-ngs-sdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-ngs-sdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-ngs-sdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-ngs-sdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-ngs-sdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### activate

```bash
$ singularity exec <container> /usr/local/bin/activate
$ podman run --it --rm --entrypoint /usr/local/bin/activate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda

```bash
$ singularity exec <container> /usr/local/bin/conda
$ podman run --it --rm --entrypoint /usr/local/bin/conda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deactivate

```bash
$ singularity exec <container> /usr/local/bin/deactivate
$ podman run --it --rm --entrypoint /usr/local/bin/deactivate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deactivate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### derb

```bash
$ singularity exec <container> /usr/local/bin/derb
$ podman run --it --rm --entrypoint /usr/local/bin/derb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/derb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbrk

```bash
$ singularity exec <container> /usr/local/bin/genbrk
$ podman run --it --rm --entrypoint /usr/local/bin/genbrk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbrk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencfu

```bash
$ singularity exec <container> /usr/local/bin/gencfu
$ podman run --it --rm --entrypoint /usr/local/bin/gencfu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencfu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gencnval

```bash
$ singularity exec <container> /usr/local/bin/gencnval
$ podman run --it --rm --entrypoint /usr/local/bin/gencnval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencnval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gendict

```bash
$ singularity exec <container> /usr/local/bin/gendict
$ podman run --it --rm --entrypoint /usr/local/bin/gendict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gendict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genrb

```bash
$ singularity exec <container> /usr/local/bin/genrb
$ podman run --it --rm --entrypoint /usr/local/bin/genrb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genrb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iconv

```bash
$ singularity exec <container> /usr/local/bin/iconv
$ podman run --it --rm --entrypoint /usr/local/bin/iconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iconv   -v ${PWD} -w ${PWD} <container> -c " $@"
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