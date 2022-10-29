---
layout: container
name:  "quay.io/biocontainers/frc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/frc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/frc/container.yaml"
updated_at: "2022-10-29 05:36:41.371655"
latest: "5b3f53e--boost1.64_0"
container_url: "https://biocontainers.pro/tools/frc"
aliases:
 - "FRC"
 - "bamtools-2.4.0"
 - "2to3-3.6"
 - "ace2sam"
 - "bamtools"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "easy_install-3.6"
 - "export2sam.pl"
 - "idle3.6"
 - "interpolate_sam.pl"
 - "maq2sam-long"
versions:
 - "5b3f53e--boost1.64_0"
description: "shpc-registry automated BioContainers addition for frc"
config: {"url": "https://biocontainers.pro/tools/frc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for frc", "latest": {"5b3f53e--boost1.64_0": "sha256:41ae5f229cb39b54122788ea30e5fc7653c710bcd7e41ce56add99e931ea4050"}, "tags": {"5b3f53e--boost1.64_0": "sha256:41ae5f229cb39b54122788ea30e5fc7653c710bcd7e41ce56add99e931ea4050"}, "docker": "quay.io/biocontainers/frc", "aliases": {"FRC": "/usr/local/bin/FRC", "bamtools-2.4.0": "/usr/local/bin/bamtools-2.4.0", "2to3-3.6": "/usr/local/bin/2to3-3.6", "ace2sam": "/usr/local/bin/ace2sam", "bamtools": "/usr/local/bin/bamtools", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "export2sam.pl": "/usr/local/bin/export2sam.pl", "idle3.6": "/usr/local/bin/idle3.6", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/frc.
shpc-registry automated BioContainers addition for frc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/frc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/frc:5b3f53e--boost1.64_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/frc/5b3f53e--boost1.64_0
$ module help quay.io/biocontainers/frc/5b3f53e--boost1.64_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### frc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### frc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### frc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### frc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### frc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### frc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FRC

```bash
$ singularity exec <container> /usr/local/bin/FRC
$ podman run --it --rm --entrypoint /usr/local/bin/FRC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FRC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools-2.4.0

```bash
$ singularity exec <container> /usr/local/bin/bamtools-2.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools-2.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
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