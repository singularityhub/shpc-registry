---
layout: container
name:  "quay.io/biocontainers/splicemap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/splicemap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/splicemap/container.yaml"
updated_at: "2025-01-21 02:52:23.243867"
latest: "3.3.5.2--h9948957_6"
container_url: "https://biocontainers.pro/tools/splicemap"
aliases:
 - "SpliceMap"
 - "amalgamateSAM"
 - "colorJunction"
 - "countsam"
 - "findNovelJunctions"
 - "neighborFilter"
 - "nnrFilter"
 - "precipitateSAM"
 - "randomJunctionFilter"
 - "runSpliceMap"
 - "sortsam"
 - "statSpliceMap"
 - "subseq"
 - "uniqueJunctionFilter"
 - "wig2barwig"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "2to3-3.9"
versions:
 - "3.3.5.2--h9f5acd7_4"
 - "3.3.5.2--h4ac6f70_5"
 - "3.3.5.2--h9948957_6"
description: "shpc-registry automated BioContainers addition for splicemap"
config: {"url": "https://biocontainers.pro/tools/splicemap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for splicemap", "latest": {"3.3.5.2--h9948957_6": "sha256:f74d5ca812effa892c41ddf3313f4d05796b25b4bebe92d4607c934672eb3b02"}, "tags": {"3.3.5.2--h9f5acd7_4": "sha256:570bbfc229dd65ee9fda0375bec232704a60773ce6b76678d02a370b8f3007bc", "3.3.5.2--h4ac6f70_5": "sha256:567888d0de7a736ba9fdf75ddd320eb80cf4738bad8c13cbb3514abdf291002b", "3.3.5.2--h9948957_6": "sha256:f74d5ca812effa892c41ddf3313f4d05796b25b4bebe92d4607c934672eb3b02"}, "docker": "quay.io/biocontainers/splicemap", "aliases": {"SpliceMap": "/usr/local/bin/SpliceMap", "amalgamateSAM": "/usr/local/bin/amalgamateSAM", "colorJunction": "/usr/local/bin/colorJunction", "countsam": "/usr/local/bin/countsam", "findNovelJunctions": "/usr/local/bin/findNovelJunctions", "neighborFilter": "/usr/local/bin/neighborFilter", "nnrFilter": "/usr/local/bin/nnrFilter", "precipitateSAM": "/usr/local/bin/precipitateSAM", "randomJunctionFilter": "/usr/local/bin/randomJunctionFilter", "runSpliceMap": "/usr/local/bin/runSpliceMap", "sortsam": "/usr/local/bin/sortsam", "statSpliceMap": "/usr/local/bin/statSpliceMap", "subseq": "/usr/local/bin/subseq", "uniqueJunctionFilter": "/usr/local/bin/uniqueJunctionFilter", "wig2barwig": "/usr/local/bin/wig2barwig", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "2to3-3.9": "/usr/local/bin/2to3-3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/splicemap.
shpc-registry automated BioContainers addition for splicemap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/splicemap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/splicemap:3.3.5.2--h9948957_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/splicemap/3.3.5.2--h9948957_6
$ module help quay.io/biocontainers/splicemap/3.3.5.2--h9948957_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### splicemap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### splicemap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### splicemap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### splicemap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### splicemap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### splicemap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpliceMap

```bash
$ singularity exec <container> /usr/local/bin/SpliceMap
$ podman run --it --rm --entrypoint /usr/local/bin/SpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amalgamateSAM

```bash
$ singularity exec <container> /usr/local/bin/amalgamateSAM
$ podman run --it --rm --entrypoint /usr/local/bin/amalgamateSAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amalgamateSAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colorJunction

```bash
$ singularity exec <container> /usr/local/bin/colorJunction
$ podman run --it --rm --entrypoint /usr/local/bin/colorJunction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorJunction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### countsam

```bash
$ singularity exec <container> /usr/local/bin/countsam
$ podman run --it --rm --entrypoint /usr/local/bin/countsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/countsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findNovelJunctions

```bash
$ singularity exec <container> /usr/local/bin/findNovelJunctions
$ podman run --it --rm --entrypoint /usr/local/bin/findNovelJunctions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findNovelJunctions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### neighborFilter

```bash
$ singularity exec <container> /usr/local/bin/neighborFilter
$ podman run --it --rm --entrypoint /usr/local/bin/neighborFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/neighborFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nnrFilter

```bash
$ singularity exec <container> /usr/local/bin/nnrFilter
$ podman run --it --rm --entrypoint /usr/local/bin/nnrFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nnrFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### precipitateSAM

```bash
$ singularity exec <container> /usr/local/bin/precipitateSAM
$ podman run --it --rm --entrypoint /usr/local/bin/precipitateSAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/precipitateSAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomJunctionFilter

```bash
$ singularity exec <container> /usr/local/bin/randomJunctionFilter
$ podman run --it --rm --entrypoint /usr/local/bin/randomJunctionFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randomJunctionFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runSpliceMap

```bash
$ singularity exec <container> /usr/local/bin/runSpliceMap
$ podman run --it --rm --entrypoint /usr/local/bin/runSpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runSpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortsam

```bash
$ singularity exec <container> /usr/local/bin/sortsam
$ podman run --it --rm --entrypoint /usr/local/bin/sortsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statSpliceMap

```bash
$ singularity exec <container> /usr/local/bin/statSpliceMap
$ podman run --it --rm --entrypoint /usr/local/bin/statSpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statSpliceMap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subseq

```bash
$ singularity exec <container> /usr/local/bin/subseq
$ podman run --it --rm --entrypoint /usr/local/bin/subseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniqueJunctionFilter

```bash
$ singularity exec <container> /usr/local/bin/uniqueJunctionFilter
$ podman run --it --rm --entrypoint /usr/local/bin/uniqueJunctionFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniqueJunctionFilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig2barwig

```bash
$ singularity exec <container> /usr/local/bin/wig2barwig
$ podman run --it --rm --entrypoint /usr/local/bin/wig2barwig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wig2barwig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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