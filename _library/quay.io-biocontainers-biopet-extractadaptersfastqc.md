---
layout: container
name:  "quay.io/biocontainers/biopet-extractadaptersfastqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biopet-extractadaptersfastqc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biopet-extractadaptersfastqc/container.yaml"
updated_at: "2022-10-27 00:43:37.267227"
latest: "0.2--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/biopet-extractadaptersfastqc"
aliases:
 - "biopet-extractadaptersfastqc"
versions:
 - "0.2--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for biopet-extractadaptersfastqc"
config: {"url": "https://biocontainers.pro/tools/biopet-extractadaptersfastqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biopet-extractadaptersfastqc", "latest": {"0.2--hdfd78af_3": "sha256:21e18cb23477e460b7ac555b91be2d4583f7f52a737d40da59ae9a43ebb658e6"}, "tags": {"0.2--hdfd78af_3": "sha256:21e18cb23477e460b7ac555b91be2d4583f7f52a737d40da59ae9a43ebb658e6"}, "docker": "quay.io/biocontainers/biopet-extractadaptersfastqc", "aliases": {"biopet-extractadaptersfastqc": "/usr/local/bin/biopet-extractadaptersfastqc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biopet-extractadaptersfastqc.
shpc-registry automated BioContainers addition for biopet-extractadaptersfastqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biopet-extractadaptersfastqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biopet-extractadaptersfastqc:0.2--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biopet-extractadaptersfastqc/0.2--hdfd78af_3
$ module help quay.io/biocontainers/biopet-extractadaptersfastqc/0.2--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biopet-extractadaptersfastqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biopet-extractadaptersfastqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biopet-extractadaptersfastqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biopet-extractadaptersfastqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biopet-extractadaptersfastqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biopet-extractadaptersfastqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biopet-extractadaptersfastqc

```bash
$ singularity exec <container> /usr/local/bin/biopet-extractadaptersfastqc
$ podman run --it --rm --entrypoint /usr/local/bin/biopet-extractadaptersfastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biopet-extractadaptersfastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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