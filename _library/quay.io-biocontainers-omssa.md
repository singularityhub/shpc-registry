---
layout: container
name:  "quay.io/biocontainers/omssa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/omssa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/omssa/container.yaml"
updated_at: "2023-05-22 03:15:30.086775"
latest: "2.1.9--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/omssa"
aliases:
 - "omssa2pepXML"
 - "omssacl"
 - "omssamerge"
versions:
 - "2.1.9--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for omssa"
config: {"url": "https://biocontainers.pro/tools/omssa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for omssa", "latest": {"2.1.9--h9ee0642_1": "sha256:d8f488ad6728a19175e1612e10b3762054d08062670a67548de1d758f129c96e"}, "tags": {"2.1.9--h9ee0642_1": "sha256:d8f488ad6728a19175e1612e10b3762054d08062670a67548de1d758f129c96e"}, "docker": "quay.io/biocontainers/omssa", "aliases": {"omssa2pepXML": "/usr/local/bin/omssa2pepXML", "omssacl": "/usr/local/bin/omssacl", "omssamerge": "/usr/local/bin/omssamerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/omssa.
shpc-registry automated BioContainers addition for omssa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/omssa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/omssa:2.1.9--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/omssa/2.1.9--h9ee0642_1
$ module help quay.io/biocontainers/omssa/2.1.9--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### omssa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### omssa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### omssa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### omssa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### omssa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### omssa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### omssa2pepXML

```bash
$ singularity exec <container> /usr/local/bin/omssa2pepXML
$ podman run --it --rm --entrypoint /usr/local/bin/omssa2pepXML   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/omssa2pepXML   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### omssacl

```bash
$ singularity exec <container> /usr/local/bin/omssacl
$ podman run --it --rm --entrypoint /usr/local/bin/omssacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/omssacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### omssamerge

```bash
$ singularity exec <container> /usr/local/bin/omssamerge
$ podman run --it --rm --entrypoint /usr/local/bin/omssamerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/omssamerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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