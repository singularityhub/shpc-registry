---
layout: container
name:  "quay.io/biocontainers/cadd-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cadd-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cadd-scripts/container.yaml"
updated_at: "2022-10-29 05:40:11.981082"
latest: "1.6--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/cadd-scripts"
aliases:
 - "cadd-install.sh"
 - "cadd.sh"
 - "2to3-3.9"
 - "Magick++-config"
 - "MagickCore-config"
 - "MagickWand-config"
 - "acyclic"
 - "animate"
 - "annotate"
 - "asadmin"
 - "bcomps"
 - "bdftogd"
versions:
 - "1.6--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for cadd-scripts"
config: {"url": "https://biocontainers.pro/tools/cadd-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cadd-scripts", "latest": {"1.6--hdfd78af_1": "sha256:74bbc85ed86e868598b2438dfad64aa902f6a5a6d6af73a380698a3136169b74"}, "tags": {"1.6--hdfd78af_1": "sha256:74bbc85ed86e868598b2438dfad64aa902f6a5a6d6af73a380698a3136169b74"}, "docker": "quay.io/biocontainers/cadd-scripts", "aliases": {"cadd-install.sh": "/usr/local/bin/cadd-install.sh", "cadd.sh": "/usr/local/bin/cadd.sh", "2to3-3.9": "/usr/local/bin/2to3-3.9", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config", "MagickWand-config": "/usr/local/bin/MagickWand-config", "acyclic": "/usr/local/bin/acyclic", "animate": "/usr/local/bin/animate", "annotate": "/usr/local/bin/annotate", "asadmin": "/usr/local/bin/asadmin", "bcomps": "/usr/local/bin/bcomps", "bdftogd": "/usr/local/bin/bdftogd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cadd-scripts.
shpc-registry automated BioContainers addition for cadd-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cadd-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cadd-scripts:1.6--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cadd-scripts/1.6--hdfd78af_1
$ module help quay.io/biocontainers/cadd-scripts/1.6--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cadd-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cadd-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cadd-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cadd-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cadd-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cadd-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cadd-install.sh

```bash
$ singularity exec <container> /usr/local/bin/cadd-install.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cadd-install.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cadd-install.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cadd.sh

```bash
$ singularity exec <container> /usr/local/bin/cadd.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cadd.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cadd.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Magick++-config

```bash
$ singularity exec <container> /usr/local/bin/Magick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickCore-config

```bash
$ singularity exec <container> /usr/local/bin/MagickCore-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/MagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### animate

```bash
$ singularity exec <container> /usr/local/bin/animate
$ podman run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/animate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
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