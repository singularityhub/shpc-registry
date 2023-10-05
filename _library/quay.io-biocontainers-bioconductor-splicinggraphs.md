---
layout: container
name:  "quay.io/biocontainers/bioconductor-splicinggraphs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splicinggraphs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splicinggraphs/container.yaml"
updated_at: "2023-10-05 02:38:57.071200"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splicinggraphs"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splicinggraphs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splicinggraphs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splicinggraphs", "latest": {"1.40.0--r43hdfd78af_0": "sha256:e16b18c1c74e22652ce83a1ce956cdd63f0f6b9bf6d608ba918ecc4e62d3bf86"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:861acb8e0fa0012eb5994ef1eb65adaffc4a50e372400a1bc08b348006bae0d2", "1.38.0--r42hdfd78af_0": "sha256:c3ccd1beb6b84677d1fb5a3ac51387822312e14a5bf593b76e48b43f5ca239a1", "1.40.0--r43hdfd78af_0": "sha256:e16b18c1c74e22652ce83a1ce956cdd63f0f6b9bf6d608ba918ecc4e62d3bf86"}, "docker": "quay.io/biocontainers/bioconductor-splicinggraphs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splicinggraphs.
shpc-registry automated BioContainers addition for bioconductor-splicinggraphs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splicinggraphs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splicinggraphs:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splicinggraphs/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splicinggraphs/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splicinggraphs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicinggraphs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicinggraphs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splicinggraphs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splicinggraphs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splicinggraphs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-splicinggraphs

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