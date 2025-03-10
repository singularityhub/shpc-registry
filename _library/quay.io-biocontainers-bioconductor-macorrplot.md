---
layout: container
name:  "quay.io/biocontainers/bioconductor-macorrplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-macorrplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-macorrplot/container.yaml"
updated_at: "2025-03-10 03:06:00.118931"
latest: "1.76.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-macorrplot"

versions:
 - "1.64.0--r41hdfd78af_0"
 - "1.68.0--r42hdfd78af_0"
 - "1.70.0--r43hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.76.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-macorrplot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-macorrplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-macorrplot", "latest": {"1.76.0--r44hdfd78af_0": "sha256:ac23cfca46361cfde9e05fa7fb1807bc69d87cc9f5c55b8127ecf75ed0748efd"}, "tags": {"1.64.0--r41hdfd78af_0": "sha256:b56c70fb4e363e6bd87cf3228a58fbd67e651ba6d03540b841058fed346e2bc6", "1.68.0--r42hdfd78af_0": "sha256:2ed226994dbfeae00c1b31570f58ca034f4cb89bc1fc57ef3d929ce57228b7d8", "1.70.0--r43hdfd78af_0": "sha256:4116e8ab5d18d3acf34ade946bb18985745127e01892987bddb991fde0d3c99a", "1.72.0--r43hdfd78af_0": "sha256:5e346e51e4fdab164fa8f5e601f9d4f411905d961fc45b369ba7b0229fde11c6", "1.76.0--r44hdfd78af_0": "sha256:ac23cfca46361cfde9e05fa7fb1807bc69d87cc9f5c55b8127ecf75ed0748efd"}, "docker": "quay.io/biocontainers/bioconductor-macorrplot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-macorrplot.
shpc-registry automated BioContainers addition for bioconductor-macorrplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-macorrplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-macorrplot:1.76.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-macorrplot/1.76.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-macorrplot/1.76.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-macorrplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macorrplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macorrplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-macorrplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-macorrplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-macorrplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-macorrplot

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