---
layout: container
name:  "quay.io/biocontainers/bioconductor-test3probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-test3probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-test3probe/container.yaml"
updated_at: "2024-02-23 02:24:08.513930"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-test3probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-test3probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-test3probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-test3probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:8ef093c307ac6d1b2172a5d8649413769c8946bd30374bdfb074230948a27e72"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:80bab38daecbf9ac460feff49d99598c13b9f9ca12c6d727de13becdd97d90e0", "2.18.0--r42hdfd78af_10": "sha256:17f585079facdd80ccc1d282ee6ffd3f4ee120f602b79ecb636f3b47e53de497", "2.18.0--r43hdfd78af_11": "sha256:13337d287bed9a5c83cb04a6398a9ffa28608e08f119ef3611331894c64a0525", "2.18.0--r43hdfd78af_12": "sha256:8ef093c307ac6d1b2172a5d8649413769c8946bd30374bdfb074230948a27e72"}, "docker": "quay.io/biocontainers/bioconductor-test3probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-test3probe.
shpc-registry automated BioContainers addition for bioconductor-test3probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-test3probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-test3probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-test3probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-test3probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-test3probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-test3probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-test3probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-test3probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-test3probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-test3probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-test3probe

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