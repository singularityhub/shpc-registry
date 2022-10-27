---
layout: container
name:  "quay.io/biocontainers/vcflatten"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcflatten/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vcflatten/container.yaml"
updated_at: "2022-10-27 00:38:07.521990"
latest: "0.5.2--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/vcflatten"
aliases:
 - "vcflatten"
versions:
 - "0.5.2--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for vcflatten"
config: {"url": "https://biocontainers.pro/tools/vcflatten", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vcflatten", "latest": {"0.5.2--hdfd78af_4": "sha256:0da6ab911e2ab34de8b6da9b6410aae0b9ff90e692fe0c400d879d81cf420c1c"}, "tags": {"0.5.2--hdfd78af_4": "sha256:0da6ab911e2ab34de8b6da9b6410aae0b9ff90e692fe0c400d879d81cf420c1c"}, "docker": "quay.io/biocontainers/vcflatten", "aliases": {"vcflatten": "/usr/local/bin/vcflatten"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcflatten.
shpc-registry automated BioContainers addition for vcflatten
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcflatten
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcflatten:0.5.2--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcflatten/0.5.2--hdfd78af_4
$ module help quay.io/biocontainers/vcflatten/0.5.2--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcflatten-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcflatten-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcflatten-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcflatten-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcflatten-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcflatten-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcflatten

```bash
$ singularity exec <container> /usr/local/bin/vcflatten
$ podman run --it --rm --entrypoint /usr/local/bin/vcflatten   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcflatten   -v ${PWD} -w ${PWD} <container> -c " $@"
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