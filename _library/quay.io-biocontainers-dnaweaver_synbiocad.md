---
layout: container
name:  "quay.io/biocontainers/dnaweaver_synbiocad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnaweaver_synbiocad/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dnaweaver_synbiocad/container.yaml"
updated_at: "2022-10-27 00:41:32.484918"
latest: "1.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dnaweaver_synbiocad"
aliases:
 - "dnachisel"
 - "weasyprint"
versions:
 - "1.0.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dnaweaver_synbiocad"
config: {"url": "https://biocontainers.pro/tools/dnaweaver_synbiocad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnaweaver_synbiocad", "latest": {"1.0.2--pyhdfd78af_0": "sha256:24c6e54a301fc0b9b1beec429b1b7e98e539c82c43dcc2d23949146340a98f62"}, "tags": {"1.0.2--pyhdfd78af_0": "sha256:24c6e54a301fc0b9b1beec429b1b7e98e539c82c43dcc2d23949146340a98f62"}, "docker": "quay.io/biocontainers/dnaweaver_synbiocad", "aliases": {"dnachisel": "/usr/local/bin/dnachisel", "weasyprint": "/usr/local/bin/weasyprint"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnaweaver_synbiocad.
shpc-registry automated BioContainers addition for dnaweaver_synbiocad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnaweaver_synbiocad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnaweaver_synbiocad:1.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnaweaver_synbiocad/1.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/dnaweaver_synbiocad/1.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnaweaver_synbiocad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnaweaver_synbiocad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnaweaver_synbiocad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnaweaver_synbiocad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnaweaver_synbiocad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnaweaver_synbiocad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnachisel

```bash
$ singularity exec <container> /usr/local/bin/dnachisel
$ podman run --it --rm --entrypoint /usr/local/bin/dnachisel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnachisel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weasyprint

```bash
$ singularity exec <container> /usr/local/bin/weasyprint
$ podman run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weasyprint   -v ${PWD} -w ${PWD} <container> -c " $@"
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