---
layout: container
name:  "quay.io/biocontainers/bamm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bamm/container.yaml"
updated_at: "2022-10-29 05:41:35.607569"
latest: "1.7.3--py27hf4361d6_8"
container_url: "https://biocontainers.pro/tools/bamm"
aliases:
 - "bamFlags"
 - "bamm"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "bwa"
 - "export2sam.pl"
 - "f2py2"
 - "f2py2.7"
 - "fasta-sanitize.pl"
 - "htsfile"
versions:
 - "1.7.3--py27hf4361d6_8"
description: "shpc-registry automated BioContainers addition for bamm"
config: {"url": "https://biocontainers.pro/tools/bamm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamm", "latest": {"1.7.3--py27hf4361d6_8": "sha256:6375c3c260bfa8e4e4ab6f195303f265e34af4cad2a856a828951965efb7a88d"}, "tags": {"1.7.3--py27hf4361d6_8": "sha256:6375c3c260bfa8e4e4ab6f195303f265e34af4cad2a856a828951965efb7a88d"}, "docker": "quay.io/biocontainers/bamm", "aliases": {"bamFlags": "/usr/local/bin/bamFlags", "bamm": "/usr/local/bin/bamm", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "bwa": "/usr/local/bin/bwa", "export2sam.pl": "/usr/local/bin/export2sam.pl", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "htsfile": "/usr/local/bin/htsfile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamm.
shpc-registry automated BioContainers addition for bamm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamm:1.7.3--py27hf4361d6_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamm/1.7.3--py27hf4361d6_8
$ module help quay.io/biocontainers/bamm/1.7.3--py27hf4361d6_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamFlags

```bash
$ singularity exec <container> /usr/local/bin/bamFlags
$ podman run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamFlags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamm

```bash
$ singularity exec <container> /usr/local/bin/bamm
$ podman run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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