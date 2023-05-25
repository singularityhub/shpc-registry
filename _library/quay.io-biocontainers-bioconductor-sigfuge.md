---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigfuge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigfuge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigfuge/container.yaml"
updated_at: "2023-05-25 03:19:49.187367"
latest: "1.36.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sigfuge"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sigfuge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigfuge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigfuge", "latest": {"1.36.0--r42hdfd78af_0": "sha256:b780d9a17811df414dbd219788248eb024a3f2386d581004833f6e161e8045e5"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:310f5b8f9a90f01d53c1f2e1eec674ac7586bc724d096d64e80736869988ac8c", "1.36.0--r42hdfd78af_0": "sha256:b780d9a17811df414dbd219788248eb024a3f2386d581004833f6e161e8045e5"}, "docker": "quay.io/biocontainers/bioconductor-sigfuge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigfuge.
shpc-registry automated BioContainers addition for bioconductor-sigfuge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigfuge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigfuge:1.36.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigfuge/1.36.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sigfuge/1.36.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigfuge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigfuge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigfuge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigfuge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigfuge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigfuge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sigfuge

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