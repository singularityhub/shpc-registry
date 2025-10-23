---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirnapath"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirnapath/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirnapath/container.yaml"
updated_at: "2025-10-23 03:57:21.876678"
latest: "1.66.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirnapath"

versions:
 - "1.54.0--r41hdfd78af_0"
 - "1.58.0--r42hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.62.0--r43hdfd78af_1"
 - "1.66.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirnapath"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirnapath", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirnapath", "latest": {"1.66.0--r44hdfd78af_0": "sha256:27eb54ba4d2ef006b345933020320ed7a4ee90eb576eaec672c3b20687131a27"}, "tags": {"1.54.0--r41hdfd78af_0": "sha256:de05189df8fe55ceaab6be490ab377c4de57a7c0ed735b4151602e4057f4dc96", "1.58.0--r42hdfd78af_0": "sha256:af56ad789c32bfbc43f21828d2403646adfbaa71ac5b6db2664f8687df9db3b4", "1.60.0--r43hdfd78af_0": "sha256:21d27eb8f2dc49b46829b079c8e9448f6244a68c8b77b80ed28aa338fee0f11e", "1.62.0--r43hdfd78af_1": "sha256:a418f5cfb4bd46a3507f7fd34a9aa9214e55f139b626209afddcdd3c883dd45a", "1.66.0--r44hdfd78af_0": "sha256:27eb54ba4d2ef006b345933020320ed7a4ee90eb576eaec672c3b20687131a27"}, "docker": "quay.io/biocontainers/bioconductor-mirnapath"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirnapath.
shpc-registry automated BioContainers addition for bioconductor-mirnapath
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnapath
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnapath:1.66.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirnapath/1.66.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirnapath/1.66.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirnapath-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnapath-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnapath-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirnapath-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirnapath-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirnapath-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirnapath

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