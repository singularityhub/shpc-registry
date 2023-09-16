---
layout: container
name:  "quay.io/biocontainers/bioconductor-methrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methrix/container.yaml"
updated_at: "2023-09-16 02:29:25.630866"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methrix"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methrix", "latest": {"1.14.0--r43hdfd78af_0": "sha256:e2d96c671a131d12f2846b48141969867db904b2447fcd2802a380883f99422a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:fe0186fc627ad64684cce4ebfcc216fde01d606a4222b4c7b67cb2e65fe79b16", "1.12.0--r42hdfd78af_0": "sha256:a0723606eecd5f5250b2d3942e7e1c64407d31e274141ca2808595a3b207fe84", "1.14.0--r43hdfd78af_0": "sha256:e2d96c671a131d12f2846b48141969867db904b2447fcd2802a380883f99422a"}, "docker": "quay.io/biocontainers/bioconductor-methrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methrix.
shpc-registry automated BioContainers addition for bioconductor-methrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methrix:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methrix/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methrix/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methrix

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