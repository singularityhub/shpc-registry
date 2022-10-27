---
layout: container
name:  "quay.io/biocontainers/gemoma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gemoma/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gemoma/container.yaml"
updated_at: "2022-10-27 00:48:22.135674"
latest: "1.7.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/gemoma"
aliases:
 - "GeMoMa"
versions:
 - "1.7.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for gemoma"
config: {"url": "https://biocontainers.pro/tools/gemoma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gemoma", "latest": {"1.7.1--hdfd78af_0": "sha256:04f16e69e42bdf754165ca71899cd3bdfe6a5c462a9e5e928e0c4d66e179daa5"}, "tags": {"1.7.1--hdfd78af_0": "sha256:04f16e69e42bdf754165ca71899cd3bdfe6a5c462a9e5e928e0c4d66e179daa5"}, "docker": "quay.io/biocontainers/gemoma", "aliases": {"GeMoMa": "/usr/local/bin/GeMoMa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gemoma.
shpc-registry automated BioContainers addition for gemoma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gemoma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gemoma:1.7.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gemoma/1.7.1--hdfd78af_0
$ module help quay.io/biocontainers/gemoma/1.7.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gemoma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gemoma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gemoma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gemoma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gemoma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gemoma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeMoMa

```bash
$ singularity exec <container> /usr/local/bin/GeMoMa
$ podman run --it --rm --entrypoint /usr/local/bin/GeMoMa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeMoMa   -v ${PWD} -w ${PWD} <container> -c " $@"
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