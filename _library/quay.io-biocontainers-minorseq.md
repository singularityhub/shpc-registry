---
layout: container
name:  "quay.io/biocontainers/minorseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minorseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minorseq/container.yaml"
updated_at: "2025-03-20 03:11:57.491157"
latest: "1.12.0--0"
container_url: "https://biocontainers.pro/tools/minorseq"
aliases:
 - "ccs"
 - "ccs-alt"
 - "cleric"
 - "fuse"
 - "juliet"
 - "julietflow"
 - "mixdata"
 - "pbmm2"
 - "ace2sam"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "interpolate_sam.pl"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
 - "plot-bamstats"
versions:
 - "1.12.0--0"
description: "shpc-registry automated BioContainers addition for minorseq"
config: {"url": "https://biocontainers.pro/tools/minorseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minorseq", "latest": {"1.12.0--0": "sha256:573b3de3d90fea8c71c5754e51dcb3845c675bf7d9cbe3856cadf68dd40321f8"}, "tags": {"1.12.0--0": "sha256:573b3de3d90fea8c71c5754e51dcb3845c675bf7d9cbe3856cadf68dd40321f8"}, "docker": "quay.io/biocontainers/minorseq", "aliases": {"ccs": "/usr/local/bin/ccs", "ccs-alt": "/usr/local/bin/ccs-alt", "cleric": "/usr/local/bin/cleric", "fuse": "/usr/local/bin/fuse", "juliet": "/usr/local/bin/juliet", "julietflow": "/usr/local/bin/julietflow", "mixdata": "/usr/local/bin/mixdata", "pbmm2": "/usr/local/bin/pbmm2", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "plot-bamstats": "/usr/local/bin/plot-bamstats"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minorseq.
shpc-registry automated BioContainers addition for minorseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minorseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minorseq:1.12.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minorseq/1.12.0--0
$ module help quay.io/biocontainers/minorseq/1.12.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minorseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minorseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minorseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minorseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minorseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minorseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccs

```bash
$ singularity exec <container> /usr/local/bin/ccs
$ podman run --it --rm --entrypoint /usr/local/bin/ccs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccs-alt

```bash
$ singularity exec <container> /usr/local/bin/ccs-alt
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-alt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-alt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleric

```bash
$ singularity exec <container> /usr/local/bin/cleric
$ podman run --it --rm --entrypoint /usr/local/bin/cleric   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleric   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse

```bash
$ singularity exec <container> /usr/local/bin/fuse
$ podman run --it --rm --entrypoint /usr/local/bin/fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juliet

```bash
$ singularity exec <container> /usr/local/bin/juliet
$ podman run --it --rm --entrypoint /usr/local/bin/juliet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juliet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### julietflow

```bash
$ singularity exec <container> /usr/local/bin/julietflow
$ podman run --it --rm --entrypoint /usr/local/bin/julietflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/julietflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mixdata

```bash
$ singularity exec <container> /usr/local/bin/mixdata
$ podman run --it --rm --entrypoint /usr/local/bin/mixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mixdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmm2

```bash
$ singularity exec <container> /usr/local/bin/pbmm2
$ podman run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### maq2sam-short

```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa

```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite

```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bamstats

```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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