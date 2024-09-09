---
layout: container
name:  "quay.io/biocontainers/bam2fastx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bam2fastx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bam2fastx/container.yaml"
updated_at: "2024-09-09 03:27:54.070220"
latest: "3.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/bam2fastx"
aliases:
 - "bam2fasta"
 - "bam2fastq"
 - "bam2sam"
 - "ccs-kinetics-bystrandify"
 - "pbbamify"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.3.1--hb7da652_2"
 - "3.0.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for bam2fastx"
config: {"url": "https://biocontainers.pro/tools/bam2fastx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bam2fastx", "latest": {"3.0.0--h9ee0642_0": "sha256:d00ab72ecf53deb749dbf19d7c1827ae9647dcb0ca09d81f2e90fdbb6bf15cd9"}, "tags": {"1.3.1--hb7da652_2": "sha256:1dd1a4249c16aa42a6961e37b59d7aa6678a161d1bf917cd5627097ac3a00be7", "3.0.0--h9ee0642_0": "sha256:d00ab72ecf53deb749dbf19d7c1827ae9647dcb0ca09d81f2e90fdbb6bf15cd9"}, "docker": "quay.io/biocontainers/bam2fastx", "aliases": {"bam2fasta": "/usr/local/bin/bam2fasta", "bam2fastq": "/usr/local/bin/bam2fastq", "bam2sam": "/usr/local/bin/bam2sam", "ccs-kinetics-bystrandify": "/usr/local/bin/ccs-kinetics-bystrandify", "pbbamify": "/usr/local/bin/pbbamify", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bam2fastx.
shpc-registry automated BioContainers addition for bam2fastx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bam2fastx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bam2fastx:3.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bam2fastx/3.0.0--h9ee0642_0
$ module help quay.io/biocontainers/bam2fastx/3.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bam2fastx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bam2fastx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bam2fastx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bam2fastx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bam2fastx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bam2fastx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2fasta

```bash
$ singularity exec <container> /usr/local/bin/bam2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2fastq

```bash
$ singularity exec <container> /usr/local/bin/bam2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2sam

```bash
$ singularity exec <container> /usr/local/bin/bam2sam
$ podman run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccs-kinetics-bystrandify

```bash
$ singularity exec <container> /usr/local/bin/ccs-kinetics-bystrandify
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbbamify

```bash
$ singularity exec <container> /usr/local/bin/pbbamify
$ podman run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbbamify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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