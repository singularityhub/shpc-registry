---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu11ksubbprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu11ksubbprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu11ksubbprobe/container.yaml"
updated_at: "2023-10-12 03:06:20.729490"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mu11ksubbprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mu11ksubbprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu11ksubbprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu11ksubbprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:1cb36e32df652dcf720f96c275f329e16feb3920c25492049771383c6bef2a95"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:741d8806ff2199993c331cb472c5063ac45e632623b5abc17c91bd92717ed790", "2.18.0--r42hdfd78af_10": "sha256:1ab401602867b7d0ac7a02785f25a1b369e529fb15d9b61c75ea61bed73dc2e7", "2.18.0--r43hdfd78af_11": "sha256:1cb36e32df652dcf720f96c275f329e16feb3920c25492049771383c6bef2a95"}, "docker": "quay.io/biocontainers/bioconductor-mu11ksubbprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu11ksubbprobe.
shpc-registry automated BioContainers addition for bioconductor-mu11ksubbprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubbprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksubbprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu11ksubbprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mu11ksubbprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu11ksubbprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubbprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksubbprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu11ksubbprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu11ksubbprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu11ksubbprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu11ksubbprobe

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