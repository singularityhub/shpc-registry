---
layout: container
name:  "quay.io/biocontainers/bioconductor-scatac.explorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scatac.explorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scatac.explorer/container.yaml"
updated_at: "2024-05-16 03:01:13.444505"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scatac.explorer"

versions:
 - "1.0.1--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scatac.explorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scatac.explorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scatac.explorer", "latest": {"1.8.0--r43hdfd78af_0": "sha256:eb38ee527f5a48f9cac5d21d4c77adb0321c18051710d7c19f0bb3dc89541e5a"}, "tags": {"1.0.1--r41hdfd78af_1": "sha256:29edc141012c44c9bdd7c0c93bf90e071cf49e47bf80f3d3f053b5bb71b63fc5", "1.4.0--r42hdfd78af_0": "sha256:cc4501d2bd8fbba963f5093514a9fde1b610caa40d23a15c19b0127653acd8f4", "1.6.0--r43hdfd78af_0": "sha256:ffec303575f71b96725c635182b2c56cd1ee9273fd196e6f8011a045f270b56f", "1.8.0--r43hdfd78af_0": "sha256:eb38ee527f5a48f9cac5d21d4c77adb0321c18051710d7c19f0bb3dc89541e5a"}, "docker": "quay.io/biocontainers/bioconductor-scatac.explorer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scatac.explorer.
shpc-registry automated BioContainers addition for bioconductor-scatac.explorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scatac.explorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scatac.explorer:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scatac.explorer/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scatac.explorer/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scatac.explorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scatac.explorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scatac.explorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scatac.explorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scatac.explorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scatac.explorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scatac.explorer

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