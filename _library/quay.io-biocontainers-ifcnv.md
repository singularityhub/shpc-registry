---
layout: container
name:  "quay.io/biocontainers/ifcnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ifcnv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ifcnv/container.yaml"
updated_at: "2023-07-22 02:37:43.580944"
latest: "0.2.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/ifcnv"
aliases:
 - "ifCNV"
 - "ifCNV_main"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
 - "clusterBed"
 - "complementBed"
 - "coverageBed"
 - "expandCols"
 - "fastaFromBed"
 - "flankBed"
 - "genomeCoverageBed"
 - "getOverlap"
 - "groupBy"
 - "intersectBed"
 - "linksBed"
 - "mapBed"
 - "maskFastaFromBed"
 - "mergeBed"
 - "multiBamCov"
versions:
 - "0.2.1--pyh5e36f6f_0"
description: "singularity registry hpc automated addition for ifcnv"
config: {"url": "https://biocontainers.pro/tools/ifcnv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ifcnv", "latest": {"0.2.1--pyh5e36f6f_0": "sha256:df61e8ca4b9e6ba1550c10afe31684b6ad5e7023350e99744e8822908467d3ad"}, "tags": {"0.2.1--pyh5e36f6f_0": "sha256:df61e8ca4b9e6ba1550c10afe31684b6ad5e7023350e99744e8822908467d3ad"}, "docker": "quay.io/biocontainers/ifcnv", "aliases": {"ifCNV": "/usr/local/bin/ifCNV", "ifCNV_main": "/usr/local/bin/ifCNV_main", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed", "flankBed": "/usr/local/bin/flankBed", "genomeCoverageBed": "/usr/local/bin/genomeCoverageBed", "getOverlap": "/usr/local/bin/getOverlap", "groupBy": "/usr/local/bin/groupBy", "intersectBed": "/usr/local/bin/intersectBed", "linksBed": "/usr/local/bin/linksBed", "mapBed": "/usr/local/bin/mapBed", "maskFastaFromBed": "/usr/local/bin/maskFastaFromBed", "mergeBed": "/usr/local/bin/mergeBed", "multiBamCov": "/usr/local/bin/multiBamCov"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ifcnv.
singularity registry hpc automated addition for ifcnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ifcnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ifcnv:0.2.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ifcnv/0.2.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/ifcnv/0.2.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ifcnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ifcnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ifcnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ifcnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ifcnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ifcnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ifCNV

```bash
$ singularity exec <container> /usr/local/bin/ifCNV
$ podman run --it --rm --entrypoint /usr/local/bin/ifCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifCNV_main

```bash
$ singularity exec <container> /usr/local/bin/ifCNV_main
$ podman run --it --rm --entrypoint /usr/local/bin/ifCNV_main   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifCNV_main   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed

```bash
$ singularity exec <container> /usr/local/bin/clusterBed
$ podman run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed

```bash
$ singularity exec <container> /usr/local/bin/complementBed
$ podman run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed

```bash
$ singularity exec <container> /usr/local/bin/coverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expandCols

```bash
$ singularity exec <container> /usr/local/bin/expandCols
$ podman run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/fastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flankBed

```bash
$ singularity exec <container> /usr/local/bin/flankBed
$ podman run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomeCoverageBed

```bash
$ singularity exec <container> /usr/local/bin/genomeCoverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getOverlap

```bash
$ singularity exec <container> /usr/local/bin/getOverlap
$ podman run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groupBy

```bash
$ singularity exec <container> /usr/local/bin/groupBy
$ podman run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectBed

```bash
$ singularity exec <container> /usr/local/bin/intersectBed
$ podman run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linksBed

```bash
$ singularity exec <container> /usr/local/bin/linksBed
$ podman run --it --rm --entrypoint /usr/local/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapBed

```bash
$ singularity exec <container> /usr/local/bin/mapBed
$ podman run --it --rm --entrypoint /usr/local/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/maskFastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeBed

```bash
$ singularity exec <container> /usr/local/bin/mergeBed
$ podman run --it --rm --entrypoint /usr/local/bin/mergeBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiBamCov

```bash
$ singularity exec <container> /usr/local/bin/multiBamCov
$ podman run --it --rm --entrypoint /usr/local/bin/multiBamCov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiBamCov   -v ${PWD} -w ${PWD} <container> -c " $@"
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