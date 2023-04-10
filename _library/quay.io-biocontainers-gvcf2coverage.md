---
layout: container
name:  "quay.io/biocontainers/gvcf2coverage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gvcf2coverage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gvcf2coverage/container.yaml"
updated_at: "2023-04-10 02:54:11.570633"
latest: "0.1--h04c669c_6"
container_url: "https://biocontainers.pro/tools/gvcf2coverage"
aliases:
 - "gvcf2coverage"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1--h8a6b41c_5"
 - "0.1--h04c669c_6"
description: "shpc-registry automated BioContainers addition for gvcf2coverage"
config: {"url": "https://biocontainers.pro/tools/gvcf2coverage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gvcf2coverage", "latest": {"0.1--h04c669c_6": "sha256:7dedb326f099820381b0013b14046b031905aba70fc8fc9779fa5da69a9bed9d"}, "tags": {"0.1--h8a6b41c_5": "sha256:d311bf1743e808c818bac6287d43554d65c26517b71480bb2f59f1e71eaca887", "0.1--h04c669c_6": "sha256:7dedb326f099820381b0013b14046b031905aba70fc8fc9779fa5da69a9bed9d"}, "docker": "quay.io/biocontainers/gvcf2coverage", "aliases": {"gvcf2coverage": "/usr/local/bin/gvcf2coverage", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gvcf2coverage.
shpc-registry automated BioContainers addition for gvcf2coverage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gvcf2coverage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gvcf2coverage:0.1--h04c669c_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gvcf2coverage/0.1--h04c669c_6
$ module help quay.io/biocontainers/gvcf2coverage/0.1--h04c669c_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gvcf2coverage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gvcf2coverage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gvcf2coverage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gvcf2coverage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gvcf2coverage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gvcf2coverage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gvcf2coverage

```bash
$ singularity exec <container> /usr/local/bin/gvcf2coverage
$ podman run --it --rm --entrypoint /usr/local/bin/gvcf2coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gvcf2coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
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