---
layout: container
name:  "quay.io/biocontainers/biopet-sampleconfig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biopet-sampleconfig/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biopet-sampleconfig/container.yaml"
updated_at: "2022-10-27 00:33:28.526813"
latest: "0.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/biopet-sampleconfig"
aliases:
 - "biopet-sampleconfig"
versions:
 - "0.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for biopet-sampleconfig"
config: {"url": "https://biocontainers.pro/tools/biopet-sampleconfig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biopet-sampleconfig", "latest": {"0.3--hdfd78af_1": "sha256:0aa721324800ce9d1e1d68a6ea81916a3f486b447d81af9c2e364bb9cad6067f"}, "tags": {"0.3--hdfd78af_1": "sha256:0aa721324800ce9d1e1d68a6ea81916a3f486b447d81af9c2e364bb9cad6067f"}, "docker": "quay.io/biocontainers/biopet-sampleconfig", "aliases": {"biopet-sampleconfig": "/usr/local/bin/biopet-sampleconfig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biopet-sampleconfig.
shpc-registry automated BioContainers addition for biopet-sampleconfig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biopet-sampleconfig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biopet-sampleconfig:0.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biopet-sampleconfig/0.3--hdfd78af_1
$ module help quay.io/biocontainers/biopet-sampleconfig/0.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biopet-sampleconfig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biopet-sampleconfig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biopet-sampleconfig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biopet-sampleconfig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biopet-sampleconfig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biopet-sampleconfig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biopet-sampleconfig

```bash
$ singularity exec <container> /usr/local/bin/biopet-sampleconfig
$ podman run --it --rm --entrypoint /usr/local/bin/biopet-sampleconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biopet-sampleconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
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