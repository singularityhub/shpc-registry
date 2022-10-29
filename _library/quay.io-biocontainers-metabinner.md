---
layout: container
name:  "quay.io/biocontainers/metabinner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabinner/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metabinner/container.yaml"
updated_at: "2022-10-29 05:57:04.141925"
latest: "1.4.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metabinner"
aliases:
 - "run_metabinner.sh"
 - "2to3-3.7"
 - "FragGeneScan"
 - "ace2sam"
 - "alimask"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "bwa"
 - "checkm"
 - "dendropy-format"
versions:
 - "1.4.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for metabinner"
config: {"url": "https://biocontainers.pro/tools/metabinner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabinner", "latest": {"1.4.4--hdfd78af_0": "sha256:88196b3069c92bf87c0612cf0e84eec2232b66cad0fa5cf0185579c2f9278772"}, "tags": {"1.4.4--hdfd78af_0": "sha256:88196b3069c92bf87c0612cf0e84eec2232b66cad0fa5cf0185579c2f9278772"}, "docker": "quay.io/biocontainers/metabinner", "aliases": {"run_metabinner.sh": "/usr/local/bin/run_metabinner.sh", "2to3-3.7": "/usr/local/bin/2to3-3.7", "FragGeneScan": "/usr/local/bin/FragGeneScan", "ace2sam": "/usr/local/bin/ace2sam", "alimask": "/usr/local/bin/alimask", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "bwa": "/usr/local/bin/bwa", "checkm": "/usr/local/bin/checkm", "dendropy-format": "/usr/local/bin/dendropy-format"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabinner.
shpc-registry automated BioContainers addition for metabinner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabinner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabinner:1.4.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabinner/1.4.4--hdfd78af_0
$ module help quay.io/biocontainers/metabinner/1.4.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabinner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabinner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabinner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabinner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabinner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabinner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run_metabinner.sh

```bash
$ singularity exec <container> /usr/local/bin/run_metabinner.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_metabinner.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_metabinner.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
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