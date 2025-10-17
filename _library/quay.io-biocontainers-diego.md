---
layout: container
name:  "quay.io/biocontainers/diego"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/diego/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/diego/container.yaml"
updated_at: "2025-10-17 03:42:45.339609"
latest: "0.1.2--py_0"
container_url: "https://biocontainers.pro/tools/diego"
aliases:
 - "HTseq2DIEGO.pl"
 - "diego.py"
 - "gfftoDIEGObed.pl"
 - "pre_STAR.py"
 - "pre_segemehl.pl"
 - "pre_std.py"
 - "pre_tophat.pl"
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
versions:
 - "0.1.2--py_0"
description: "shpc-registry automated BioContainers addition for diego"
config: {"url": "https://biocontainers.pro/tools/diego", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for diego", "latest": {"0.1.2--py_0": "sha256:04d58f2fe5e2a10b3ed4c383a75c44c1680d4a109eef79824f01a897dea41890"}, "tags": {"0.1.2--py_0": "sha256:04d58f2fe5e2a10b3ed4c383a75c44c1680d4a109eef79824f01a897dea41890"}, "docker": "quay.io/biocontainers/diego", "aliases": {"HTseq2DIEGO.pl": "/usr/local/bin/HTseq2DIEGO.pl", "diego.py": "/usr/local/bin/diego.py", "gfftoDIEGObed.pl": "/usr/local/bin/gfftoDIEGObed.pl", "pre_STAR.py": "/usr/local/bin/pre_STAR.py", "pre_segemehl.pl": "/usr/local/bin/pre_segemehl.pl", "pre_std.py": "/usr/local/bin/pre_std.py", "pre_tophat.pl": "/usr/local/bin/pre_tophat.pl", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/diego.
shpc-registry automated BioContainers addition for diego
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/diego
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/diego:0.1.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/diego/0.1.2--py_0
$ module help quay.io/biocontainers/diego/0.1.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### diego-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### diego-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### diego-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### diego-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### diego-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### diego-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HTseq2DIEGO.pl

```bash
$ singularity exec <container> /usr/local/bin/HTseq2DIEGO.pl
$ podman run --it --rm --entrypoint /usr/local/bin/HTseq2DIEGO.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HTseq2DIEGO.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diego.py

```bash
$ singularity exec <container> /usr/local/bin/diego.py
$ podman run --it --rm --entrypoint /usr/local/bin/diego.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diego.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfftoDIEGObed.pl

```bash
$ singularity exec <container> /usr/local/bin/gfftoDIEGObed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gfftoDIEGObed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfftoDIEGObed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre_STAR.py

```bash
$ singularity exec <container> /usr/local/bin/pre_STAR.py
$ podman run --it --rm --entrypoint /usr/local/bin/pre_STAR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre_STAR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre_segemehl.pl

```bash
$ singularity exec <container> /usr/local/bin/pre_segemehl.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pre_segemehl.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre_segemehl.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre_std.py

```bash
$ singularity exec <container> /usr/local/bin/pre_std.py
$ podman run --it --rm --entrypoint /usr/local/bin/pre_std.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre_std.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre_tophat.pl

```bash
$ singularity exec <container> /usr/local/bin/pre_tophat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pre_tophat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre_tophat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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