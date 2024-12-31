---
layout: container
name:  "quay.io/biocontainers/gxf2bed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gxf2bed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gxf2bed/container.yaml"
updated_at: "2024-12-31 02:59:57.239091"
latest: "0.2.4--ha6fb395_0"
container_url: "https://biocontainers.pro/tools/gxf2bed"
aliases:
 - "gxf2bed"
versions:
 - "0.1.0--h4ac6f70_0"
 - "0.2.0--h4ac6f70_0"
 - "0.2.1--h4ac6f70_0"
 - "0.2.2--h4ac6f70_0"
 - "0.2.3--h919a2d8_1"
 - "0.2.4--ha6fb395_0"
description: "singularity registry hpc automated addition for gxf2bed"
config: {"url": "https://biocontainers.pro/tools/gxf2bed", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gxf2bed", "latest": {"0.2.4--ha6fb395_0": "sha256:465417657ded316ecadb733f100b20ef8d583439e671d1484f9d651818cec9f5"}, "tags": {"0.1.0--h4ac6f70_0": "sha256:8b0610cd1a25541b12e382bc35b1568815edadafd753cc3b91b401441087efff", "0.2.0--h4ac6f70_0": "sha256:b5824362836a68e71ce1c002b219023d91e8c88ed131808367ce5efbfb77df3c", "0.2.1--h4ac6f70_0": "sha256:d9ef314567e4a3c104c44e28739c21cc889bd54289583948c20e203e3b79e3ae", "0.2.2--h4ac6f70_0": "sha256:61b5e9bfde210a5bf4998da0d398cb1e6a94097f3ec71ab963eef14e919cd328", "0.2.3--h919a2d8_1": "sha256:0ce89631945422564d9645a6ac2c07aba08809062fb73a95d53f1837a54ed5f0", "0.2.4--ha6fb395_0": "sha256:465417657ded316ecadb733f100b20ef8d583439e671d1484f9d651818cec9f5"}, "docker": "quay.io/biocontainers/gxf2bed", "aliases": {"gxf2bed": "/usr/local/bin/gxf2bed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gxf2bed.
singularity registry hpc automated addition for gxf2bed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gxf2bed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gxf2bed:0.2.4--ha6fb395_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gxf2bed/0.2.4--ha6fb395_0
$ module help quay.io/biocontainers/gxf2bed/0.2.4--ha6fb395_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gxf2bed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gxf2bed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gxf2bed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gxf2bed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gxf2bed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gxf2bed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gxf2bed

```bash
$ singularity exec <container> /usr/local/bin/gxf2bed
$ podman run --it --rm --entrypoint /usr/local/bin/gxf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gxf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
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