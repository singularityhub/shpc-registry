---
layout: container
name:  "quay.io/biocontainers/velvet-sc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/velvet-sc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/velvet-sc/container.yaml"
updated_at: "2024-07-22 03:46:28.005761"
latest: "0.7.62--h7132678_5"
container_url: "https://biocontainers.pro/tools/velvet-sc"
aliases:
 - "shuffleSequences_fasta.pl"
 - "shuffleSequences_fastq.pl"
 - "velvetg"
 - "velveth"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.7.62--h7132678_5"
description: "shpc-registry automated BioContainers addition for velvet-sc"
config: {"url": "https://biocontainers.pro/tools/velvet-sc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for velvet-sc", "latest": {"0.7.62--h7132678_5": "sha256:0fb5ecb2fea2547e4b5fe981217004f65710b2c1eb173cb03bbbd03b1a56ee36"}, "tags": {"0.7.62--h7132678_5": "sha256:0fb5ecb2fea2547e4b5fe981217004f65710b2c1eb173cb03bbbd03b1a56ee36"}, "docker": "quay.io/biocontainers/velvet-sc", "aliases": {"shuffleSequences_fasta.pl": "/usr/local/bin/shuffleSequences_fasta.pl", "shuffleSequences_fastq.pl": "/usr/local/bin/shuffleSequences_fastq.pl", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/velvet-sc.
shpc-registry automated BioContainers addition for velvet-sc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/velvet-sc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/velvet-sc:0.7.62--h7132678_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/velvet-sc/0.7.62--h7132678_5
$ module help quay.io/biocontainers/velvet-sc/0.7.62--h7132678_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### velvet-sc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### velvet-sc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### velvet-sc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### velvet-sc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### velvet-sc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### velvet-sc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shuffleSequences_fasta.pl

```bash
$ singularity exec <container> /usr/local/bin/shuffleSequences_fasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleSequences_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleSequences_fasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleSequences_fastq.pl

```bash
$ singularity exec <container> /usr/local/bin/shuffleSequences_fastq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/shuffleSequences_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shuffleSequences_fastq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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