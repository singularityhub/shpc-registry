---
layout: container
name:  "quay.io/biocontainers/ctat-mutations"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ctat-mutations/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ctat-mutations/container.yaml"
updated_at: "2022-10-29 05:33:40.838341"
latest: "2.0.1--py27_5"
container_url: "https://biocontainers.pro/tools/ctat-mutations"
aliases:
 - "ctat_mutations"
 - "STAR"
 - "STARlong"
 - "ace2sam"
 - "appletviewer"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "chardetect"
 - "color-chrs.pl"
versions:
 - "2.0.1--py27_5"
description: "shpc-registry automated BioContainers addition for ctat-mutations"
config: {"url": "https://biocontainers.pro/tools/ctat-mutations", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ctat-mutations", "latest": {"2.0.1--py27_5": "sha256:3cb88ef5e4ef8e40677f219c090d81f32f601df2e48b9ae37451a836ad85e335"}, "tags": {"2.0.1--py27_5": "sha256:3cb88ef5e4ef8e40677f219c090d81f32f601df2e48b9ae37451a836ad85e335"}, "docker": "quay.io/biocontainers/ctat-mutations", "aliases": {"ctat_mutations": "/usr/local/bin/ctat_mutations", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "ace2sam": "/usr/local/bin/ace2sam", "appletviewer": "/usr/local/bin/appletviewer", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "chardetect": "/usr/local/bin/chardetect", "color-chrs.pl": "/usr/local/bin/color-chrs.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ctat-mutations.
shpc-registry automated BioContainers addition for ctat-mutations
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ctat-mutations
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ctat-mutations:2.0.1--py27_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ctat-mutations/2.0.1--py27_5
$ module help quay.io/biocontainers/ctat-mutations/2.0.1--py27_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ctat-mutations-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ctat-mutations-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ctat-mutations-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ctat-mutations-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ctat-mutations-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ctat-mutations-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ctat_mutations

```bash
$ singularity exec <container> /usr/local/bin/ctat_mutations
$ podman run --it --rm --entrypoint /usr/local/bin/ctat_mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctat_mutations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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