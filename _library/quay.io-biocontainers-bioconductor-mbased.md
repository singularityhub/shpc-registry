---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbased"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbased/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbased/container.yaml"
updated_at: "2025-01-30 03:34:37.494284"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbased"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbased"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbased", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbased", "latest": {"1.36.0--r43hdfd78af_0": "sha256:46add26235cd35163bf472ed44520633c9e03d5e41ffc76aee49379d934c0e6a"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:b66cf347497c4a60d7f63aa731933c3d319709b2b69adaf0a6654674036a6667", "1.32.0--r42hdfd78af_0": "sha256:078e7647dd701f9bb99ee1551367a2205d5728e54e9f4bbbbad53d6f747b88bb", "1.34.0--r43hdfd78af_0": "sha256:5aa22fbd0309ba5002bfa0416d635927961529fdbb3a0500f3f88868b8fd29e4", "1.36.0--r43hdfd78af_0": "sha256:46add26235cd35163bf472ed44520633c9e03d5e41ffc76aee49379d934c0e6a"}, "docker": "quay.io/biocontainers/bioconductor-mbased"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbased.
shpc-registry automated BioContainers addition for bioconductor-mbased
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbased
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbased:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbased/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbased/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbased-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbased-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbased-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbased-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbased-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbased-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mbased

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