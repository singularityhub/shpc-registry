---
layout: container
name:  "quay.io/biocontainers/r-dpeak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dpeak/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-dpeak/container.yaml"
updated_at: "2024-08-27 06:15:01.212943"
latest: "2.0.1--r43h4ac6f70_9"
container_url: "https://biocontainers.pro/tools/r-dpeak"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.0.1--r41h9f5acd7_6"
 - "2.0.1--r42h9f5acd7_7"
 - "2.0.1--r42h4ac6f70_8"
 - "2.0.1--r43h4ac6f70_9"
description: "shpc-registry automated BioContainers addition for r-dpeak"
config: {"url": "https://biocontainers.pro/tools/r-dpeak", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-dpeak", "latest": {"2.0.1--r43h4ac6f70_9": "sha256:20da8e5eaae8e0eeaa54042b4407677525ee3f363d3c32938ee574ebcc231af4"}, "tags": {"2.0.1--r41h9f5acd7_6": "sha256:2d6e1ba36915ebe97faeb90af7bf0e17b1e362e8ff5afca70d9592f72f65bd64", "2.0.1--r42h9f5acd7_7": "sha256:7302245e5b1ecccc82e5b14c606f4644c5d29ef868c906343bf30d97097ec078", "2.0.1--r42h4ac6f70_8": "sha256:0829952e0878014f03852736f750e1e85946da4c16bd394a313ac9c6cc78cbe1", "2.0.1--r43h4ac6f70_9": "sha256:20da8e5eaae8e0eeaa54042b4407677525ee3f363d3c32938ee574ebcc231af4"}, "docker": "quay.io/biocontainers/r-dpeak", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dpeak.
shpc-registry automated BioContainers addition for r-dpeak
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dpeak
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dpeak:2.0.1--r43h4ac6f70_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dpeak/2.0.1--r43h4ac6f70_9
$ module help quay.io/biocontainers/r-dpeak/2.0.1--r43h4ac6f70_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dpeak-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dpeak-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dpeak-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dpeak-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dpeak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dpeak-inspect-deffile:

```bash
$ singularity inspect -d <container>
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