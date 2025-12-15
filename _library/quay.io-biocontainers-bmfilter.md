---
layout: container
name:  "quay.io/biocontainers/bmfilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bmfilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bmfilter/container.yaml"
updated_at: "2025-12-15 04:27:50.336968"
latest: "3.101--h9948957_6"
container_url: "https://biocontainers.pro/tools/bmfilter"
aliases:
 - "bmfilter"
versions:
 - "3.101--hc9558a2_3"
 - "3.101--h4ac6f70_5"
 - "3.101--h9948957_6"
description: "shpc-registry automated BioContainers addition for bmfilter"
config: {"url": "https://biocontainers.pro/tools/bmfilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bmfilter", "latest": {"3.101--h9948957_6": "sha256:10b740875224d2a893eeda98c489461256e290e10678b3b49fdbbb0e64d346dd"}, "tags": {"3.101--hc9558a2_3": "sha256:c01439297af9a0e35e6843a8b82c3e2854ae283407c9efb8ed44bf17f6e10fee", "3.101--h4ac6f70_5": "sha256:cc20cb7d0ba73b789e2171b87de3dbdaf785e7506bccb49d849a29be1d0aed39", "3.101--h9948957_6": "sha256:10b740875224d2a893eeda98c489461256e290e10678b3b49fdbbb0e64d346dd"}, "docker": "quay.io/biocontainers/bmfilter", "aliases": {"bmfilter": "/usr/local/bin/bmfilter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bmfilter.
shpc-registry automated BioContainers addition for bmfilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bmfilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bmfilter:3.101--h9948957_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bmfilter/3.101--h9948957_6
$ module help quay.io/biocontainers/bmfilter/3.101--h9948957_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bmfilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bmfilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bmfilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bmfilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bmfilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bmfilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bmfilter

```bash
$ singularity exec <container> /usr/local/bin/bmfilter
$ podman run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bmfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
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