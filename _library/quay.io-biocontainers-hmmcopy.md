---
layout: container
name:  "quay.io/biocontainers/hmmcopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmcopy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmmcopy/container.yaml"
updated_at: "2022-10-27 00:57:55.268144"
latest: "0.1.1--h5b5514e_8"
container_url: "https://biocontainers.pro/tools/hmmcopy"
aliases:
 - "bigWigInfo"
 - "bigWigSummary"
 - "bigWigToWig"
 - "fastaToRead"
 - "gcCounter"
 - "generateMap.pl"
 - "mapCounter"
 - "readCounter"
 - "readToMap.pl"
 - "renameChr.pl"
 - "segToGc"
 - "segToMap"
versions:
 - "0.1.1--h5b5514e_8"
description: "shpc-registry automated BioContainers addition for hmmcopy"
config: {"url": "https://biocontainers.pro/tools/hmmcopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmcopy", "latest": {"0.1.1--h5b5514e_8": "sha256:af9470030886895e010bd5cde44340d23043c76fd38467536ac2625f2aa9437a"}, "tags": {"0.1.1--h5b5514e_8": "sha256:af9470030886895e010bd5cde44340d23043c76fd38467536ac2625f2aa9437a"}, "docker": "quay.io/biocontainers/hmmcopy", "aliases": {"bigWigInfo": "/usr/local/bin/bigWigInfo", "bigWigSummary": "/usr/local/bin/bigWigSummary", "bigWigToWig": "/usr/local/bin/bigWigToWig", "fastaToRead": "/usr/local/bin/fastaToRead", "gcCounter": "/usr/local/bin/gcCounter", "generateMap.pl": "/usr/local/bin/generateMap.pl", "mapCounter": "/usr/local/bin/mapCounter", "readCounter": "/usr/local/bin/readCounter", "readToMap.pl": "/usr/local/bin/readToMap.pl", "renameChr.pl": "/usr/local/bin/renameChr.pl", "segToGc": "/usr/local/bin/segToGc", "segToMap": "/usr/local/bin/segToMap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmcopy.
shpc-registry automated BioContainers addition for hmmcopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmcopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmcopy:0.1.1--h5b5514e_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmcopy/0.1.1--h5b5514e_8
$ module help quay.io/biocontainers/hmmcopy/0.1.1--h5b5514e_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmcopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmcopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmcopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmcopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmcopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmcopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigInfo

```bash
$ singularity exec <container> /usr/local/bin/bigWigInfo
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigInfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigSummary

```bash
$ singularity exec <container> /usr/local/bin/bigWigSummary
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigSummary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToWig

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaToRead

```bash
$ singularity exec <container> /usr/local/bin/fastaToRead
$ podman run --it --rm --entrypoint /usr/local/bin/fastaToRead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaToRead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcCounter

```bash
$ singularity exec <container> /usr/local/bin/gcCounter
$ podman run --it --rm --entrypoint /usr/local/bin/gcCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generateMap.pl

```bash
$ singularity exec <container> /usr/local/bin/generateMap.pl
$ podman run --it --rm --entrypoint /usr/local/bin/generateMap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generateMap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapCounter

```bash
$ singularity exec <container> /usr/local/bin/mapCounter
$ podman run --it --rm --entrypoint /usr/local/bin/mapCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readCounter

```bash
$ singularity exec <container> /usr/local/bin/readCounter
$ podman run --it --rm --entrypoint /usr/local/bin/readCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readToMap.pl

```bash
$ singularity exec <container> /usr/local/bin/readToMap.pl
$ podman run --it --rm --entrypoint /usr/local/bin/readToMap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readToMap.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### renameChr.pl

```bash
$ singularity exec <container> /usr/local/bin/renameChr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/renameChr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renameChr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segToGc

```bash
$ singularity exec <container> /usr/local/bin/segToGc
$ podman run --it --rm --entrypoint /usr/local/bin/segToGc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segToGc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segToMap

```bash
$ singularity exec <container> /usr/local/bin/segToMap
$ podman run --it --rm --entrypoint /usr/local/bin/segToMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segToMap   -v ${PWD} -w ${PWD} <container> -c " $@"
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