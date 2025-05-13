---
layout: container
name:  "quay.io/biocontainers/dsk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dsk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dsk/container.yaml"
updated_at: "2025-05-13 03:45:06.801616"
latest: "2.3.3--h5ca1c30_6"
container_url: "https://biocontainers.pro/tools/dsk"
aliases:
 - "dsk"
 - "dsk2ascii"
 - "h5cc"
versions:
 - "2.3.3--h5b5514e_2"
 - "2.3.3--h43eeafb_4"
 - "2.3.3--h43eeafb_5"
 - "2.3.3--h5ca1c30_6"
description: "shpc-registry automated BioContainers addition for dsk"
config: {"url": "https://biocontainers.pro/tools/dsk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dsk", "latest": {"2.3.3--h5ca1c30_6": "sha256:e231eda4450e32c15ab98d094ab13130418446c827c0968c70f3428ad34f3f13"}, "tags": {"2.3.3--h5b5514e_2": "sha256:7dc2b558c08c23666a3aedc8fcfff8c220991a4da4e44a71a3bfa31846fb43a3", "2.3.3--h43eeafb_4": "sha256:beddb088bf39626a7deb865c192af7b85e4d9cc6fdfa3cf7da9a63f044772a30", "2.3.3--h43eeafb_5": "sha256:251a30187fc3f4930784437100ad8804d88444f56cc18743aa8cd380cb368b0d", "2.3.3--h5ca1c30_6": "sha256:e231eda4450e32c15ab98d094ab13130418446c827c0968c70f3428ad34f3f13"}, "docker": "quay.io/biocontainers/dsk", "aliases": {"dsk": "/usr/local/bin/dsk", "dsk2ascii": "/usr/local/bin/dsk2ascii", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dsk.
shpc-registry automated BioContainers addition for dsk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dsk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dsk:2.3.3--h5ca1c30_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dsk/2.3.3--h5ca1c30_6
$ module help quay.io/biocontainers/dsk/2.3.3--h5ca1c30_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dsk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dsk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dsk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dsk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dsk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dsk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dsk

```bash
$ singularity exec <container> /usr/local/bin/dsk
$ podman run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsk2ascii

```bash
$ singularity exec <container> /usr/local/bin/dsk2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsk2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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