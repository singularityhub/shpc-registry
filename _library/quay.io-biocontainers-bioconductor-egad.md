---
layout: container
name:  "quay.io/biocontainers/bioconductor-egad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-egad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-egad/container.yaml"
updated_at: "2025-05-24 11:40:07.510832"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-egad"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-egad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-egad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-egad", "latest": {"1.34.0--r44hdfd78af_0": "sha256:d741c20cf17e6235507bcce40f30b19ead5a81a97361c7acfc4b7f7f082a4b15"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:fda1437f29f0d1317fb6fbe95bb610b3962926e42cb1b8d7d337216c2f8ee85f", "1.26.0--r42hdfd78af_0": "sha256:2a980de1e5614638e5eeb4a95d254f9c483d79704e8fecf12ba894772ee1f3ec", "1.28.0--r43hdfd78af_0": "sha256:b851ea82584d5c208f84199782a5be203522b2afbda7f7b6a33ac3d3e998b4de", "1.30.0--r43hdfd78af_0": "sha256:8806f3ca43d707ad649eec133287a7947beeaf8fcbdfc24904cd255f8889fee7", "1.34.0--r44hdfd78af_0": "sha256:d741c20cf17e6235507bcce40f30b19ead5a81a97361c7acfc4b7f7f082a4b15"}, "docker": "quay.io/biocontainers/bioconductor-egad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-egad.
shpc-registry automated BioContainers addition for bioconductor-egad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-egad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-egad:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-egad/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-egad/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-egad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-egad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-egad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-egad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-egad

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