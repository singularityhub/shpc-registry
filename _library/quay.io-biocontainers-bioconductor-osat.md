---
layout: container
name:  "quay.io/biocontainers/bioconductor-osat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-osat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-osat/container.yaml"
updated_at: "2024-02-06 03:03:49.207626"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-osat"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-osat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-osat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-osat", "latest": {"1.50.0--r43hdfd78af_0": "sha256:5fa1edff87bb32569a9f01a9649f68a750c142f4a408ea84c222df79d2fd74c4"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:8562b99eaec4811a521f4818835f508d0547a0f160e250ca26e2049dcb04133a", "1.46.0--r42hdfd78af_0": "sha256:10fd014cb46bded84c77606eadb8d5b71b930a3a1fabb621926c5afa1540dac2", "1.48.0--r43hdfd78af_0": "sha256:3c9dfafab093b21c966ed5e44a6b01017bf3d845a9f22d16a90e53d544ef92b7", "1.50.0--r43hdfd78af_0": "sha256:5fa1edff87bb32569a9f01a9649f68a750c142f4a408ea84c222df79d2fd74c4"}, "docker": "quay.io/biocontainers/bioconductor-osat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-osat.
shpc-registry automated BioContainers addition for bioconductor-osat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-osat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-osat:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-osat/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-osat/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-osat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-osat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-osat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-osat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-osat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-osat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-osat

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