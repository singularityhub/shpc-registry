---
layout: container
name:  "quay.io/biocontainers/bioconductor-comet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-comet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-comet/container.yaml"
updated_at: "2023-06-12 04:51:04.231243"
latest: "1.30.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-comet"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-comet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-comet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-comet", "latest": {"1.30.0--r42hdfd78af_0": "sha256:14caa2ebf4f7df475477037e22845082de2b0d28c968aab534cc879de35e6fc3"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:7ad088e7b1589b6cb3b5e7f8707939bf5ca27119c9648d39071408fce8f5068f", "1.30.0--r42hdfd78af_0": "sha256:14caa2ebf4f7df475477037e22845082de2b0d28c968aab534cc879de35e6fc3"}, "docker": "quay.io/biocontainers/bioconductor-comet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-comet.
shpc-registry automated BioContainers addition for bioconductor-comet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-comet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-comet:1.30.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-comet/1.30.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-comet/1.30.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-comet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-comet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-comet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-comet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-comet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-comet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-comet

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