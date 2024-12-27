---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnviz/container.yaml"
updated_at: "2024-12-27 03:20:43.374966"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnviz"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnviz", "latest": {"1.10.0--r43hdfd78af_0": "sha256:f9ded74869d18bc6c750471e3b2f4c6bf673ec7992fe367bbb42825351a9c5b1"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:5ba1ba9d59bd30f007cdd1a69e05e7aef32ef70235021b0931e042495fb7914a", "1.6.0--r42hdfd78af_0": "sha256:b827daa16ec86d530a309bbc51d499c9cc78e528dd1380239e8b3f17ae29f7d0", "1.8.0--r43hdfd78af_0": "sha256:dab06f5f080ddee7e21a299e93c3e1e4fb67ccde469b2266f1d31ff731f026b3", "1.10.0--r43hdfd78af_0": "sha256:f9ded74869d18bc6c750471e3b2f4c6bf673ec7992fe367bbb42825351a9c5b1"}, "docker": "quay.io/biocontainers/bioconductor-cnviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnviz.
shpc-registry automated BioContainers addition for bioconductor-cnviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnviz:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnviz/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnviz/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cnviz

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