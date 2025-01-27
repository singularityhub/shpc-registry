---
layout: container
name:  "quay.io/biocontainers/hmmcopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmcopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmmcopy/container.yaml"
updated_at: "2025-01-27 06:58:44.080734"
latest: "0.1.1--h5ca1c30_11"
container_url: "https://biocontainers.pro/tools/hmmcopy"
aliases:
 - "bigWigInfo"
 - "bigWigSummary"
 - "bigWigToBedGraph"
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
 - "wigToBigWig"
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
 - "0.1.1--h5b5514e_8"
 - "0.1.1--h43eeafb_9"
 - "0.1.1--h43eeafb_10"
 - "0.1.1--h5ca1c30_11"
description: "shpc-registry automated BioContainers addition for hmmcopy"
config: {"url": "https://biocontainers.pro/tools/hmmcopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmcopy", "latest": {"0.1.1--h5ca1c30_11": "sha256:c0c7f8baac1eb338debcc0e15086766da2ca8b60bed84074593f7dfaaf6c88cf"}, "tags": {"0.1.1--h5b5514e_8": "sha256:af9470030886895e010bd5cde44340d23043c76fd38467536ac2625f2aa9437a", "0.1.1--h43eeafb_9": "sha256:b54327b50b4b2ea820cb4e628fc8d534f13e4e2260f24dd9f786201d768d2f03", "0.1.1--h43eeafb_10": "sha256:7a848b7f5e3c5ddcf1d6e6979bf0756ed031630f0564c789965ffec2e043f50b", "0.1.1--h5ca1c30_11": "sha256:c0c7f8baac1eb338debcc0e15086766da2ca8b60bed84074593f7dfaaf6c88cf"}, "docker": "quay.io/biocontainers/hmmcopy", "aliases": {"bigWigInfo": "/usr/local/bin/bigWigInfo", "bigWigSummary": "/usr/local/bin/bigWigSummary", "bigWigToBedGraph": "/usr/local/bin/bigWigToBedGraph", "bigWigToWig": "/usr/local/bin/bigWigToWig", "fastaToRead": "/usr/local/bin/fastaToRead", "gcCounter": "/usr/local/bin/gcCounter", "generateMap.pl": "/usr/local/bin/generateMap.pl", "mapCounter": "/usr/local/bin/mapCounter", "readCounter": "/usr/local/bin/readCounter", "readToMap.pl": "/usr/local/bin/readToMap.pl", "renameChr.pl": "/usr/local/bin/renameChr.pl", "segToGc": "/usr/local/bin/segToGc", "segToMap": "/usr/local/bin/segToMap", "wigToBigWig": "/usr/local/bin/wigToBigWig", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmcopy.
shpc-registry automated BioContainers addition for hmmcopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmcopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmcopy:0.1.1--h5ca1c30_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmcopy/0.1.1--h5ca1c30_11
$ module help quay.io/biocontainers/hmmcopy/0.1.1--h5ca1c30_11
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


#### bigWigToBedGraph

```bash
$ singularity exec <container> /usr/local/bin/bigWigToBedGraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
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