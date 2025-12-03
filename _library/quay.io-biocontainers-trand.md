---
layout: container
name:  "quay.io/biocontainers/trand"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trand/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trand/container.yaml"
updated_at: "2025-12-03 03:40:12.654950"
latest: "22.10.13--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/trand"
aliases:
 - "trand"
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
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
versions:
 - "22.10.13--pyhdfd78af_0"
description: "singularity registry hpc automated addition for trand"
config: {"url": "https://biocontainers.pro/tools/trand", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for trand", "latest": {"22.10.13--pyhdfd78af_0": "sha256:7c5987cc7c6f75f785f9a654a595a90ccf3bd274cbb173709829d281f19f8e77"}, "tags": {"22.10.13--pyhdfd78af_0": "sha256:7c5987cc7c6f75f785f9a654a595a90ccf3bd274cbb173709829d281f19f8e77"}, "docker": "quay.io/biocontainers/trand", "aliases": {"trand": "/usr/local/bin/trand", "x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed", "flankBed": "/usr/local/bin/flankBed", "genomeCoverageBed": "/usr/local/bin/genomeCoverageBed", "getOverlap": "/usr/local/bin/getOverlap", "groupBy": "/usr/local/bin/groupBy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trand.
singularity registry hpc automated addition for trand
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trand
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trand:22.10.13--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trand/22.10.13--pyhdfd78af_0
$ module help quay.io/biocontainers/trand/22.10.13--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trand-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trand-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trand-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trand-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trand-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trand-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trand

```bash
$ singularity exec <container> /usr/local/bin/trand
$ podman run --it --rm --entrypoint /usr/local/bin/trand   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trand   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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