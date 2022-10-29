---
layout: container
name:  "quay.io/biocontainers/parascopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parascopy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/parascopy/container.yaml"
updated_at: "2022-10-29 05:56:12.334274"
latest: "1.9.1--py39heba0655_0"
container_url: "https://biocontainers.pro/tools/parascopy"
aliases:
 - "_parascopy_freebayes"
 - "parascopy"
 - "2to3-3.9"
 - "ace2sam"
 - "bc"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "bwa"
 - "dc"
 - "export2sam.pl"
 - "f2py3.9"
versions:
 - "1.9.1--py39heba0655_0"
description: "shpc-registry automated BioContainers addition for parascopy"
config: {"url": "https://biocontainers.pro/tools/parascopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parascopy", "latest": {"1.9.1--py39heba0655_0": "sha256:510ea5bec833767af1c344ca772bae2d9bab06a4cf6c260cec1ebf528b5887c3"}, "tags": {"1.9.1--py39heba0655_0": "sha256:510ea5bec833767af1c344ca772bae2d9bab06a4cf6c260cec1ebf528b5887c3"}, "docker": "quay.io/biocontainers/parascopy", "aliases": {"_parascopy_freebayes": "/usr/local/bin/_parascopy_freebayes", "parascopy": "/usr/local/bin/parascopy", "2to3-3.9": "/usr/local/bin/2to3-3.9", "ace2sam": "/usr/local/bin/ace2sam", "bc": "/usr/local/bin/bc", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "bwa": "/usr/local/bin/bwa", "dc": "/usr/local/bin/dc", "export2sam.pl": "/usr/local/bin/export2sam.pl", "f2py3.9": "/usr/local/bin/f2py3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parascopy.
shpc-registry automated BioContainers addition for parascopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parascopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parascopy:1.9.1--py39heba0655_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parascopy/1.9.1--py39heba0655_0
$ module help quay.io/biocontainers/parascopy/1.9.1--py39heba0655_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parascopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parascopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parascopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parascopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parascopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parascopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _parascopy_freebayes

```bash
$ singularity exec <container> /usr/local/bin/_parascopy_freebayes
$ podman run --it --rm --entrypoint /usr/local/bin/_parascopy_freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_parascopy_freebayes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parascopy

```bash
$ singularity exec <container> /usr/local/bin/parascopy
$ podman run --it --rm --entrypoint /usr/local/bin/parascopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parascopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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