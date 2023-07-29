---
layout: container
name:  "quay.io/biocontainers/leptonica"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/leptonica/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/leptonica/container.yaml"
updated_at: "2023-07-29 03:09:32.728591"
latest: "1.73--1"
container_url: "https://biocontainers.pro/tools/leptonica"
aliases:
 - "convertfilestopdf"
 - "convertfilestops"
 - "convertformat"
 - "convertsegfilestopdf"
 - "convertsegfilestops"
 - "converttopdf"
 - "converttops"
 - "fileinfo"
 - "printimage"
 - "printsplitimage"
 - "printtiff"
 - "splitimage2pdf"
 - "xtractprotos"
versions:
 - "1.73--1"
description: "shpc-registry automated BioContainers addition for leptonica"
config: {"url": "https://biocontainers.pro/tools/leptonica", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for leptonica", "latest": {"1.73--1": "sha256:693619a9cefd6fc87876f80627e29a14fa05f0e35f3b6912aeac3287f8899dc9"}, "tags": {"1.73--1": "sha256:693619a9cefd6fc87876f80627e29a14fa05f0e35f3b6912aeac3287f8899dc9"}, "docker": "quay.io/biocontainers/leptonica", "aliases": {"convertfilestopdf": "/usr/local/bin/convertfilestopdf", "convertfilestops": "/usr/local/bin/convertfilestops", "convertformat": "/usr/local/bin/convertformat", "convertsegfilestopdf": "/usr/local/bin/convertsegfilestopdf", "convertsegfilestops": "/usr/local/bin/convertsegfilestops", "converttopdf": "/usr/local/bin/converttopdf", "converttops": "/usr/local/bin/converttops", "fileinfo": "/usr/local/bin/fileinfo", "printimage": "/usr/local/bin/printimage", "printsplitimage": "/usr/local/bin/printsplitimage", "printtiff": "/usr/local/bin/printtiff", "splitimage2pdf": "/usr/local/bin/splitimage2pdf", "xtractprotos": "/usr/local/bin/xtractprotos"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/leptonica.
shpc-registry automated BioContainers addition for leptonica
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/leptonica
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/leptonica:1.73--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/leptonica/1.73--1
$ module help quay.io/biocontainers/leptonica/1.73--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### leptonica-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### leptonica-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### leptonica-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### leptonica-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### leptonica-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### leptonica-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertformat

```bash
$ singularity exec <container> /usr/local/bin/convertformat
$ podman run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestopdf

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestopdf
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convertsegfilestops

```bash
$ singularity exec <container> /usr/local/bin/convertsegfilestops
$ podman run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convertsegfilestops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttopdf

```bash
$ singularity exec <container> /usr/local/bin/converttopdf
$ podman run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttopdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### converttops

```bash
$ singularity exec <container> /usr/local/bin/converttops
$ podman run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/converttops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fileinfo

```bash
$ singularity exec <container> /usr/local/bin/fileinfo
$ podman run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fileinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printimage

```bash
$ singularity exec <container> /usr/local/bin/printimage
$ podman run --it --rm --entrypoint /usr/local/bin/printimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printsplitimage

```bash
$ singularity exec <container> /usr/local/bin/printsplitimage
$ podman run --it --rm --entrypoint /usr/local/bin/printsplitimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printsplitimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printtiff

```bash
$ singularity exec <container> /usr/local/bin/printtiff
$ podman run --it --rm --entrypoint /usr/local/bin/printtiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printtiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitimage2pdf

```bash
$ singularity exec <container> /usr/local/bin/splitimage2pdf
$ podman run --it --rm --entrypoint /usr/local/bin/splitimage2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitimage2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtractprotos

```bash
$ singularity exec <container> /usr/local/bin/xtractprotos
$ podman run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtractprotos   -v ${PWD} -w ${PWD} <container> -c " $@"
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