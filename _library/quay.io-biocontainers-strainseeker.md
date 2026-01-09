---
layout: container
name:  "quay.io/biocontainers/strainseeker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainseeker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainseeker/container.yaml"
updated_at: "2026-01-09 04:23:11.487486"
latest: "1.5.1--h7b50bb2_5"
container_url: "https://biocontainers.pro/tools/strainseeker"
aliases:
 - "builder.pl"
 - "cov.R"
 - "drawtree.R"
 - "gdistribution"
 - "glistcompare"
 - "glistmaker"
 - "glistquery"
 - "gmer_counter"
 - "oe.R"
 - "seeker.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.5.1--hec16e2b_2"
 - "1.5.1--h031d066_4"
 - "1.5.1--h7b50bb2_5"
description: "shpc-registry automated BioContainers addition for strainseeker"
config: {"url": "https://biocontainers.pro/tools/strainseeker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strainseeker", "latest": {"1.5.1--h7b50bb2_5": "sha256:05a545f4f509aafdb00728650d8ed67861e445e0e040a995534205c73ead92ad"}, "tags": {"1.5.1--hec16e2b_2": "sha256:be4bb3c9bf5d80b0623a5acc096b7b28bffdccdc28ef07e07b31d62a2dba5696", "1.5.1--h031d066_4": "sha256:c03e0c06623c5a20e894085517e83b67b26d7602e310b852aa9004d048856774", "1.5.1--h7b50bb2_5": "sha256:05a545f4f509aafdb00728650d8ed67861e445e0e040a995534205c73ead92ad"}, "docker": "quay.io/biocontainers/strainseeker", "aliases": {"builder.pl": "/usr/local/bin/builder.pl", "cov.R": "/usr/local/bin/cov.R", "drawtree.R": "/usr/local/bin/drawtree.R", "gdistribution": "/usr/local/bin/gdistribution", "glistcompare": "/usr/local/bin/glistcompare", "glistmaker": "/usr/local/bin/glistmaker", "glistquery": "/usr/local/bin/glistquery", "gmer_counter": "/usr/local/bin/gmer_counter", "oe.R": "/usr/local/bin/oe.R", "seeker.pl": "/usr/local/bin/seeker.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainseeker.
shpc-registry automated BioContainers addition for strainseeker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainseeker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainseeker:1.5.1--h7b50bb2_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainseeker/1.5.1--h7b50bb2_5
$ module help quay.io/biocontainers/strainseeker/1.5.1--h7b50bb2_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainseeker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainseeker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainseeker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainseeker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainseeker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainseeker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### builder.pl

```bash
$ singularity exec <container> /usr/local/bin/builder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/builder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/builder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cov.R

```bash
$ singularity exec <container> /usr/local/bin/cov.R
$ podman run --it --rm --entrypoint /usr/local/bin/cov.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cov.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### drawtree.R

```bash
$ singularity exec <container> /usr/local/bin/drawtree.R
$ podman run --it --rm --entrypoint /usr/local/bin/drawtree.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drawtree.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdistribution

```bash
$ singularity exec <container> /usr/local/bin/gdistribution
$ podman run --it --rm --entrypoint /usr/local/bin/gdistribution   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdistribution   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glistcompare

```bash
$ singularity exec <container> /usr/local/bin/glistcompare
$ podman run --it --rm --entrypoint /usr/local/bin/glistcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glistmaker

```bash
$ singularity exec <container> /usr/local/bin/glistmaker
$ podman run --it --rm --entrypoint /usr/local/bin/glistmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistmaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glistquery

```bash
$ singularity exec <container> /usr/local/bin/glistquery
$ podman run --it --rm --entrypoint /usr/local/bin/glistquery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glistquery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmer_counter

```bash
$ singularity exec <container> /usr/local/bin/gmer_counter
$ podman run --it --rm --entrypoint /usr/local/bin/gmer_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmer_counter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oe.R

```bash
$ singularity exec <container> /usr/local/bin/oe.R
$ podman run --it --rm --entrypoint /usr/local/bin/oe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oe.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seeker.pl

```bash
$ singularity exec <container> /usr/local/bin/seeker.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seeker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seeker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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