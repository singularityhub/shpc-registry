---
layout: container
name:  "quay.io/biocontainers/bioconductor-mdqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mdqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mdqc/container.yaml"
updated_at: "2026-01-31 04:36:59.925887"
latest: "1.68.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mdqc"

versions:
 - "1.56.0--r41hdfd78af_0"
 - "1.60.0--r42hdfd78af_0"
 - "1.62.0--r43hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
 - "1.68.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mdqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mdqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mdqc", "latest": {"1.68.0--r44hdfd78af_0": "sha256:fe051f3dc3f90fdd8adf6a6f75e3277ef40a45244d680c52b7119fa743f2012c"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:d07be10810270a6b819f597c100e2b7c5a795a5d68cfbc9753cdb54e5eece3f0", "1.60.0--r42hdfd78af_0": "sha256:4efa2d306877e15f15a88d30d74cd1d93023b46f4463f3455fedd01131154675", "1.62.0--r43hdfd78af_0": "sha256:485e6d54a56dcd68e9223a0cfc8680a953c4b9fd5ca1c5bb55ed848cd8391883", "1.64.0--r43hdfd78af_0": "sha256:ec516f5cb547a69d68f982d8b045258fbd73691a64464f5c3294b775ef8469b3", "1.68.0--r44hdfd78af_0": "sha256:fe051f3dc3f90fdd8adf6a6f75e3277ef40a45244d680c52b7119fa743f2012c"}, "docker": "quay.io/biocontainers/bioconductor-mdqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mdqc.
shpc-registry automated BioContainers addition for bioconductor-mdqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mdqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mdqc:1.68.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mdqc/1.68.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mdqc/1.68.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mdqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mdqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mdqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mdqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mdqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mdqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mdqc

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