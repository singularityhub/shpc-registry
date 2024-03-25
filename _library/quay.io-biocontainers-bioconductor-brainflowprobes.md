---
layout: container
name:  "quay.io/biocontainers/bioconductor-brainflowprobes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-brainflowprobes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-brainflowprobes/container.yaml"
updated_at: "2024-03-25 03:02:46.589348"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-brainflowprobes"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-brainflowprobes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-brainflowprobes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-brainflowprobes", "latest": {"1.16.0--r43hdfd78af_0": "sha256:9b72cedf9e43b482cbd516ac4c4075dfc48ed8a4793bb5a055fb892ec3c16e3c"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:23557130ada74541b9dd4c594624e992b389086dc709a9f0a8d877db8d6d7341", "1.12.0--r42hdfd78af_0": "sha256:e32273991629c92d4f369fa220ac06468f7d73430b150bd3c807a90c9af01a6e", "1.14.0--r43hdfd78af_0": "sha256:9f174166a3c1e311a2fb1426066b9da31ad28601701c7b2f3c5b4c036cebea0b", "1.16.0--r43hdfd78af_0": "sha256:9b72cedf9e43b482cbd516ac4c4075dfc48ed8a4793bb5a055fb892ec3c16e3c"}, "docker": "quay.io/biocontainers/bioconductor-brainflowprobes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-brainflowprobes.
shpc-registry automated BioContainers addition for bioconductor-brainflowprobes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-brainflowprobes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-brainflowprobes:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-brainflowprobes/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-brainflowprobes/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-brainflowprobes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brainflowprobes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brainflowprobes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-brainflowprobes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-brainflowprobes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-brainflowprobes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-brainflowprobes

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