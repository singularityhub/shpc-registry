---
layout: container
name:  "quay.io/biocontainers/cistrome_beta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cistrome_beta/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cistrome_beta/container.yaml"
updated_at: "2022-10-27 00:56:07.673196"
latest: "1.0.7--py27h9801fc8_5"
container_url: "https://biocontainers.pro/tools/cistrome_beta"
aliases:
 - "BETA"
 - "misp"
versions:
 - "1.0.7--py27h9801fc8_5"
description: "shpc-registry automated BioContainers addition for cistrome_beta"
config: {"url": "https://biocontainers.pro/tools/cistrome_beta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cistrome_beta", "latest": {"1.0.7--py27h9801fc8_5": "sha256:ced86bf344fec552d67f2ad02cee0f8cfc7ab4b8a396c596c4d30409b72f83ca"}, "tags": {"1.0.7--py27h9801fc8_5": "sha256:ced86bf344fec552d67f2ad02cee0f8cfc7ab4b8a396c596c4d30409b72f83ca"}, "docker": "quay.io/biocontainers/cistrome_beta", "aliases": {"BETA": "/usr/local/bin/BETA", "misp": "/usr/local/bin/misp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cistrome_beta.
shpc-registry automated BioContainers addition for cistrome_beta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cistrome_beta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cistrome_beta:1.0.7--py27h9801fc8_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cistrome_beta/1.0.7--py27h9801fc8_5
$ module help quay.io/biocontainers/cistrome_beta/1.0.7--py27h9801fc8_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cistrome_beta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cistrome_beta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cistrome_beta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cistrome_beta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cistrome_beta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cistrome_beta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BETA

```bash
$ singularity exec <container> /usr/local/bin/BETA
$ podman run --it --rm --entrypoint /usr/local/bin/BETA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BETA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### misp

```bash
$ singularity exec <container> /usr/local/bin/misp
$ podman run --it --rm --entrypoint /usr/local/bin/misp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/misp   -v ${PWD} -w ${PWD} <container> -c " $@"
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