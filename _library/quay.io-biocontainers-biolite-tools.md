---
layout: container
name:  "quay.io/biocontainers/biolite-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biolite-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biolite-tools/container.yaml"
updated_at: "2023-10-05 03:48:35.158830"
latest: "0.4.0--hdcf5f25_8"
container_url: "https://biocontainers.pro/tools/biolite-tools"
aliases:
 - "bl-coverage"
 - "bl-exclude"
 - "bl-fasta2fastq"
 - "bl-fastq2fasta"
 - "bl-filter-illumina"
 - "bl-insert-stats"
 - "bl-interleave"
 - "bl-pair-reads"
 - "bl-pileup-stats"
 - "bl-randomize"
 - "bl-threshold"
versions:
 - "0.4.0--hd03093a_6"
 - "0.4.0--hd03093a_7"
 - "0.4.0--hdcf5f25_8"
description: "shpc-registry automated BioContainers addition for biolite-tools"
config: {"url": "https://biocontainers.pro/tools/biolite-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biolite-tools", "latest": {"0.4.0--hdcf5f25_8": "sha256:4ed3ae273da527ed2584b9dce9cbd57439d6d95ad4c175e2693a61c9b335f273"}, "tags": {"0.4.0--hd03093a_6": "sha256:63fb1431d4d78e1fd4c7bd30cd202a63c38aa47fb47d36d9270d7759b19eecc0", "0.4.0--hd03093a_7": "sha256:aab7b33cbbbeb79c8ed8073cb4180ac7c95b3fb62d2d8cb2dd2c9b702a621c9d", "0.4.0--hdcf5f25_8": "sha256:4ed3ae273da527ed2584b9dce9cbd57439d6d95ad4c175e2693a61c9b335f273"}, "docker": "quay.io/biocontainers/biolite-tools", "aliases": {"bl-coverage": "/usr/local/bin/bl-coverage", "bl-exclude": "/usr/local/bin/bl-exclude", "bl-fasta2fastq": "/usr/local/bin/bl-fasta2fastq", "bl-fastq2fasta": "/usr/local/bin/bl-fastq2fasta", "bl-filter-illumina": "/usr/local/bin/bl-filter-illumina", "bl-insert-stats": "/usr/local/bin/bl-insert-stats", "bl-interleave": "/usr/local/bin/bl-interleave", "bl-pair-reads": "/usr/local/bin/bl-pair-reads", "bl-pileup-stats": "/usr/local/bin/bl-pileup-stats", "bl-randomize": "/usr/local/bin/bl-randomize", "bl-threshold": "/usr/local/bin/bl-threshold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biolite-tools.
shpc-registry automated BioContainers addition for biolite-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biolite-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biolite-tools:0.4.0--hdcf5f25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biolite-tools/0.4.0--hdcf5f25_8
$ module help quay.io/biocontainers/biolite-tools/0.4.0--hdcf5f25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biolite-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biolite-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biolite-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biolite-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biolite-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biolite-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bl-coverage

```bash
$ singularity exec <container> /usr/local/bin/bl-coverage
$ podman run --it --rm --entrypoint /usr/local/bin/bl-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-exclude

```bash
$ singularity exec <container> /usr/local/bin/bl-exclude
$ podman run --it --rm --entrypoint /usr/local/bin/bl-exclude   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-exclude   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-fasta2fastq

```bash
$ singularity exec <container> /usr/local/bin/bl-fasta2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/bl-fasta2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-fasta2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-fastq2fasta

```bash
$ singularity exec <container> /usr/local/bin/bl-fastq2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bl-fastq2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-fastq2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-filter-illumina

```bash
$ singularity exec <container> /usr/local/bin/bl-filter-illumina
$ podman run --it --rm --entrypoint /usr/local/bin/bl-filter-illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-filter-illumina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-insert-stats

```bash
$ singularity exec <container> /usr/local/bin/bl-insert-stats
$ podman run --it --rm --entrypoint /usr/local/bin/bl-insert-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-insert-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-interleave

```bash
$ singularity exec <container> /usr/local/bin/bl-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/bl-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-pair-reads

```bash
$ singularity exec <container> /usr/local/bin/bl-pair-reads
$ podman run --it --rm --entrypoint /usr/local/bin/bl-pair-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-pair-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-pileup-stats

```bash
$ singularity exec <container> /usr/local/bin/bl-pileup-stats
$ podman run --it --rm --entrypoint /usr/local/bin/bl-pileup-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-pileup-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-randomize

```bash
$ singularity exec <container> /usr/local/bin/bl-randomize
$ podman run --it --rm --entrypoint /usr/local/bin/bl-randomize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-randomize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl-threshold

```bash
$ singularity exec <container> /usr/local/bin/bl-threshold
$ podman run --it --rm --entrypoint /usr/local/bin/bl-threshold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl-threshold   -v ${PWD} -w ${PWD} <container> -c " $@"
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