---
layout: container
name:  "quay.io/biocontainers/bioconductor-mosim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mosim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mosim/container.yaml"
updated_at: "2023-11-02 02:39:24.027879"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mosim"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mosim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mosim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mosim", "latest": {"1.14.0--r43hdfd78af_0": "sha256:79cc3a69d516798b73fa38474e55b705d608a2977bac9b4407f93b45550e0162"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:c707e5f8059dab47b872988f9ff6cef74ecb232cc5f1baa5855c2f9bfa9af179", "1.12.0--r42hdfd78af_0": "sha256:75165d9ae9e2eeb0f67c71f150d52c0c8b70f32d3711ac6a72967bbc1c973ef8", "1.14.0--r43hdfd78af_0": "sha256:79cc3a69d516798b73fa38474e55b705d608a2977bac9b4407f93b45550e0162"}, "docker": "quay.io/biocontainers/bioconductor-mosim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mosim.
shpc-registry automated BioContainers addition for bioconductor-mosim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mosim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mosim:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mosim/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mosim/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mosim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mosim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mosim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mosim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mosim

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