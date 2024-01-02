---
layout: container
name:  "quay.io/biocontainers/capc-map"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/capc-map/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/capc-map/container.yaml"
updated_at: "2024-01-02 03:07:51.323304"
latest: "1.1.3--py36hffcf100_6"
container_url: "https://biocontainers.pro/tools/capc-map"
aliases:
 - "capC-MAP"
 - "capCdigestfastq"
 - "capClocation2fragment"
 - "capCmain"
 - "capCpair2bg"
 - "capCpileup2binned"
 - "cutadapt"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
versions:
 - "1.1.3--py36hffcf100_6"
description: "shpc-registry automated BioContainers addition for capc-map"
config: {"url": "https://biocontainers.pro/tools/capc-map", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for capc-map", "latest": {"1.1.3--py36hffcf100_6": "sha256:0b1f59dd54ce8bcd640d5f614d08f05d7bb17ef74c543bb3d28c997b39e2730f"}, "tags": {"1.1.3--py36hffcf100_6": "sha256:0b1f59dd54ce8bcd640d5f614d08f05d7bb17ef74c543bb3d28c997b39e2730f"}, "docker": "quay.io/biocontainers/capc-map", "aliases": {"capC-MAP": "/usr/local/bin/capC-MAP", "capCdigestfastq": "/usr/local/bin/capCdigestfastq", "capClocation2fragment": "/usr/local/bin/capClocation2fragment", "capCmain": "/usr/local/bin/capCmain", "capCpair2bg": "/usr/local/bin/capCpair2bg", "capCpileup2binned": "/usr/local/bin/capCpileup2binned", "cutadapt": "/usr/local/bin/cutadapt", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/capc-map.
shpc-registry automated BioContainers addition for capc-map
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/capc-map
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/capc-map:1.1.3--py36hffcf100_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/capc-map/1.1.3--py36hffcf100_6
$ module help quay.io/biocontainers/capc-map/1.1.3--py36hffcf100_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### capc-map-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### capc-map-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### capc-map-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### capc-map-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### capc-map-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### capc-map-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### capC-MAP

```bash
$ singularity exec <container> /usr/local/bin/capC-MAP
$ podman run --it --rm --entrypoint /usr/local/bin/capC-MAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capC-MAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capCdigestfastq

```bash
$ singularity exec <container> /usr/local/bin/capCdigestfastq
$ podman run --it --rm --entrypoint /usr/local/bin/capCdigestfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capCdigestfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capClocation2fragment

```bash
$ singularity exec <container> /usr/local/bin/capClocation2fragment
$ podman run --it --rm --entrypoint /usr/local/bin/capClocation2fragment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capClocation2fragment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capCmain

```bash
$ singularity exec <container> /usr/local/bin/capCmain
$ podman run --it --rm --entrypoint /usr/local/bin/capCmain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capCmain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capCpair2bg

```bash
$ singularity exec <container> /usr/local/bin/capCpair2bg
$ podman run --it --rm --entrypoint /usr/local/bin/capCpair2bg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capCpair2bg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capCpileup2binned

```bash
$ singularity exec <container> /usr/local/bin/capCpileup2binned
$ podman run --it --rm --entrypoint /usr/local/bin/capCpileup2binned   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capCpileup2binned   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
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