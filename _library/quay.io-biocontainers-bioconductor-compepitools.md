---
layout: container
name:  "quay.io/biocontainers/bioconductor-compepitools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-compepitools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-compepitools/container.yaml"
updated_at: "2022-10-29 05:55:35.867196"
latest: "1.27.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-compepitools"
aliases:
 - "R"
 - "Rscript"
 - "acountry"
 - "adig"
 - "ahost"
 - "autopoint"
 - "bunzip2"
 - "bzcat"
 - "bzcmp"
 - "bzdiff"
versions:
 - "1.27.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-compepitools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-compepitools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-compepitools", "latest": {"1.27.0--r41hdfd78af_0": "sha256:041c0c2d3d617c665ef4c966f8b9b9bce12de7262dddc32be531771e45dd064b"}, "tags": {"1.27.0--r41hdfd78af_0": "sha256:041c0c2d3d617c665ef4c966f8b9b9bce12de7262dddc32be531771e45dd064b"}, "docker": "quay.io/biocontainers/bioconductor-compepitools", "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript", "acountry": "/usr/local/bin/acountry", "adig": "/usr/local/bin/adig", "ahost": "/usr/local/bin/ahost", "autopoint": "/usr/local/bin/autopoint", "bunzip2": "/usr/local/bin/bunzip2", "bzcat": "/usr/local/bin/bzcat", "bzcmp": "/usr/local/bin/bzcmp", "bzdiff": "/usr/local/bin/bzdiff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-compepitools.
shpc-registry automated BioContainers addition for bioconductor-compepitools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-compepitools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-compepitools:1.27.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-compepitools/1.27.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-compepitools/1.27.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-compepitools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compepitools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-compepitools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-compepitools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-compepitools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-compepitools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acountry

```bash
$ singularity exec <container> /usr/local/bin/acountry
$ podman run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adig

```bash
$ singularity exec <container> /usr/local/bin/adig
$ podman run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ahost

```bash
$ singularity exec <container> /usr/local/bin/ahost
$ podman run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autopoint

```bash
$ singularity exec <container> /usr/local/bin/autopoint
$ podman run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autopoint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bunzip2

```bash
$ singularity exec <container> /usr/local/bin/bunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/bunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzcat

```bash
$ singularity exec <container> /usr/local/bin/bzcat
$ podman run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzcmp

```bash
$ singularity exec <container> /usr/local/bin/bzcmp
$ podman run --it --rm --entrypoint /usr/local/bin/bzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bzdiff

```bash
$ singularity exec <container> /usr/local/bin/bzdiff
$ podman run --it --rm --entrypoint /usr/local/bin/bzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
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