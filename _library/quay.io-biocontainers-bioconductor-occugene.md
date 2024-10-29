---
layout: container
name:  "quay.io/biocontainers/bioconductor-occugene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-occugene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-occugene/container.yaml"
updated_at: "2024-10-29 03:01:48.871093"
latest: "1.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-occugene"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-occugene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-occugene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-occugene", "latest": {"1.62.0--r43hdfd78af_0": "sha256:3e18720d899a24845a41a820b657696f4e90457b10a05ca42ceeda6173e40b66"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:760936c64cb848488d5be6ab1ba36462af9b3493511e8a9a864562e898a9a9d4", "1.58.0--r42hdfd78af_0": "sha256:706b314b0f63787f0989d292b4b0be79194094200e5fc1d5d81b2c4bc41efe94", "1.60.0--r43hdfd78af_0": "sha256:f518e80885c81c12608fce7f5c1689efc5dcc975fadc809fa27be5d0c6dd428d", "1.62.0--r43hdfd78af_0": "sha256:3e18720d899a24845a41a820b657696f4e90457b10a05ca42ceeda6173e40b66"}, "docker": "quay.io/biocontainers/bioconductor-occugene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-occugene.
shpc-registry automated BioContainers addition for bioconductor-occugene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-occugene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-occugene:1.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-occugene/1.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-occugene/1.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-occugene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-occugene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-occugene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-occugene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-occugene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-occugene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-occugene

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