---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodist/container.yaml"
updated_at: "2025-12-20 04:01:17.802779"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodist"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodist"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodist", "latest": {"1.78.0--r44hdfd78af_0": "sha256:ecd828275df3e434e4900c1af5dae144292536c294ad89dee3bd9311e803d179"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:1e1b4f6eed2205f5497e18301708f54a37bb181622b8c1c3efdacf052dac5493", "1.70.0--r42hdfd78af_0": "sha256:84906835dfe7f1783ff0c2b3c9a9ef3906677c0a5a25dcb33c832ee9c9edfcdf", "1.72.0--r43hdfd78af_0": "sha256:84475f614b438dacd7fa70e708366b77732d2807b6eadc0fc3e79232e2e2cc6d", "1.74.0--r43hdfd78af_0": "sha256:5ca8211061518c00e3999597825540e3aedc38c6bacc2ad7d66e152a45f5b2f2", "1.78.0--r44hdfd78af_0": "sha256:ecd828275df3e434e4900c1af5dae144292536c294ad89dee3bd9311e803d179"}, "docker": "quay.io/biocontainers/bioconductor-biodist"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodist.
shpc-registry automated BioContainers addition for bioconductor-biodist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodist:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodist/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodist/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodist

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