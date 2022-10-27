---
layout: container
name:  "quay.io/biocontainers/tabixpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tabixpp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tabixpp/container.yaml"
updated_at: "2022-10-27 01:01:26.106379"
latest: "1.1.0--h470d46e_9"
container_url: "https://biocontainers.pro/tools/tabixpp"

versions:
 - "1.1.0--h470d46e_9"
description: "shpc-registry automated BioContainers addition for tabixpp"
config: {"url": "https://biocontainers.pro/tools/tabixpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tabixpp", "latest": {"1.1.0--h470d46e_9": "sha256:5213a96cc511c795ed76b49764adc51b7970ff8f9932dd10b8e2997c057e350a"}, "tags": {"1.1.0--h470d46e_9": "sha256:5213a96cc511c795ed76b49764adc51b7970ff8f9932dd10b8e2997c057e350a"}, "docker": "quay.io/biocontainers/tabixpp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/tabixpp.
shpc-registry automated BioContainers addition for tabixpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tabixpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tabixpp:1.1.0--h470d46e_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tabixpp/1.1.0--h470d46e_9
$ module help quay.io/biocontainers/tabixpp/1.1.0--h470d46e_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tabixpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tabixpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tabixpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tabixpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tabixpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tabixpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tabixpp

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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