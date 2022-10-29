---
layout: container
name:  "quay.io/biocontainers/genomedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomedata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genomedata/container.yaml"
updated_at: "2022-10-29 05:48:45.268615"
latest: "1.5.0--py310h35e684e_3"
container_url: "https://biocontainers.pro/tools/genomedata"
aliases:
 - "bigWigToBedGraph"
 - "filter"
 - "genomedata-close-data"
 - "genomedata-erase-data"
 - "genomedata-hardmask"
 - "genomedata-histogram"
 - "genomedata-info"
 - "genomedata-load"
 - "genomedata-load-assembly"
 - "genomedata-load-data"
 - "genomedata-load-seq"
 - "genomedata-open-data"
 - "genomedata-query"
 - "genomedata-report"
 - "hidehead"
 - "innerjoin"
 - "intersect"
 - "mean"
 - "nohead"
 - "run_genomedata_tests.py"
 - "test_genomedata.py"
 - "2to3-3.10"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
versions:
 - "1.5.0--py310h35e684e_3"
description: "shpc-registry automated BioContainers addition for genomedata"
config: {"url": "https://biocontainers.pro/tools/genomedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genomedata", "latest": {"1.5.0--py310h35e684e_3": "sha256:f0e3df8a4b6a9f5808571434d2bcd2c96a002d8e2055f172458754705d103480"}, "tags": {"1.5.0--py310h35e684e_3": "sha256:f0e3df8a4b6a9f5808571434d2bcd2c96a002d8e2055f172458754705d103480"}, "docker": "quay.io/biocontainers/genomedata", "aliases": {"bigWigToBedGraph": "/usr/local/bin/bigWigToBedGraph", "filter": "/usr/local/bin/filter", "genomedata-close-data": "/usr/local/bin/genomedata-close-data", "genomedata-erase-data": "/usr/local/bin/genomedata-erase-data", "genomedata-hardmask": "/usr/local/bin/genomedata-hardmask", "genomedata-histogram": "/usr/local/bin/genomedata-histogram", "genomedata-info": "/usr/local/bin/genomedata-info", "genomedata-load": "/usr/local/bin/genomedata-load", "genomedata-load-assembly": "/usr/local/bin/genomedata-load-assembly", "genomedata-load-data": "/usr/local/bin/genomedata-load-data", "genomedata-load-seq": "/usr/local/bin/genomedata-load-seq", "genomedata-open-data": "/usr/local/bin/genomedata-open-data", "genomedata-query": "/usr/local/bin/genomedata-query", "genomedata-report": "/usr/local/bin/genomedata-report", "hidehead": "/usr/local/bin/hidehead", "innerjoin": "/usr/local/bin/innerjoin", "intersect": "/usr/local/bin/intersect", "mean": "/usr/local/bin/mean", "nohead": "/usr/local/bin/nohead", "run_genomedata_tests.py": "/usr/local/bin/run_genomedata_tests.py", "test_genomedata.py": "/usr/local/bin/test_genomedata.py", "2to3-3.10": "/usr/local/bin/2to3-3.10", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomedata.
shpc-registry automated BioContainers addition for genomedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomedata:1.5.0--py310h35e684e_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomedata/1.5.0--py310h35e684e_3
$ module help quay.io/biocontainers/genomedata/1.5.0--py310h35e684e_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bigWigToBedGraph

```bash
$ singularity exec <container> /usr/local/bin/bigWigToBedGraph
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToBedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter

```bash
$ singularity exec <container> /usr/local/bin/filter
$ podman run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-close-data

```bash
$ singularity exec <container> /usr/local/bin/genomedata-close-data
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-close-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-close-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-erase-data

```bash
$ singularity exec <container> /usr/local/bin/genomedata-erase-data
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-erase-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-erase-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-hardmask

```bash
$ singularity exec <container> /usr/local/bin/genomedata-hardmask
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-hardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-hardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-histogram

```bash
$ singularity exec <container> /usr/local/bin/genomedata-histogram
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-info

```bash
$ singularity exec <container> /usr/local/bin/genomedata-info
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-load

```bash
$ singularity exec <container> /usr/local/bin/genomedata-load
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-load-assembly

```bash
$ singularity exec <container> /usr/local/bin/genomedata-load-assembly
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-load-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-load-assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-load-data

```bash
$ singularity exec <container> /usr/local/bin/genomedata-load-data
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-load-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-load-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-load-seq

```bash
$ singularity exec <container> /usr/local/bin/genomedata-load-seq
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-load-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-load-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-open-data

```bash
$ singularity exec <container> /usr/local/bin/genomedata-open-data
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-open-data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-open-data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-query

```bash
$ singularity exec <container> /usr/local/bin/genomedata-query
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomedata-report

```bash
$ singularity exec <container> /usr/local/bin/genomedata-report
$ podman run --it --rm --entrypoint /usr/local/bin/genomedata-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomedata-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hidehead

```bash
$ singularity exec <container> /usr/local/bin/hidehead
$ podman run --it --rm --entrypoint /usr/local/bin/hidehead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hidehead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innerjoin

```bash
$ singularity exec <container> /usr/local/bin/innerjoin
$ podman run --it --rm --entrypoint /usr/local/bin/innerjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innerjoin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersect

```bash
$ singularity exec <container> /usr/local/bin/intersect
$ podman run --it --rm --entrypoint /usr/local/bin/intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mean

```bash
$ singularity exec <container> /usr/local/bin/mean
$ podman run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nohead

```bash
$ singularity exec <container> /usr/local/bin/nohead
$ podman run --it --rm --entrypoint /usr/local/bin/nohead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nohead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_genomedata_tests.py

```bash
$ singularity exec <container> /usr/local/bin/run_genomedata_tests.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_genomedata_tests.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_genomedata_tests.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_genomedata.py

```bash
$ singularity exec <container> /usr/local/bin/test_genomedata.py
$ podman run --it --rm --entrypoint /usr/local/bin/test_genomedata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_genomedata.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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