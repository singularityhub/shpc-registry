---
layout: container
name:  "quay.io/biocontainers/bioconductor-human1mduov3bcrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human1mduov3bcrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human1mduov3bcrlmm/container.yaml"
updated_at: "2025-01-27 03:29:10.150150"
latest: "1.0.4--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-human1mduov3bcrlmm"

versions:
 - "1.0.4--r41hdfd78af_9"
 - "1.0.4--r42hdfd78af_10"
 - "1.0.4--r43hdfd78af_11"
 - "1.0.4--r43hdfd78af_12"
 - "1.0.4--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-human1mduov3bcrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human1mduov3bcrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human1mduov3bcrlmm", "latest": {"1.0.4--r44hdfd78af_13": "sha256:a68dbe6670083886a0f19600d5fb582af5770525cbee55880d941293f57db12e"}, "tags": {"1.0.4--r41hdfd78af_9": "sha256:e7c32ab35e4b2b269a27b3dd4aa2781cca75cac423ad0651ce0753034e57ecd5", "1.0.4--r42hdfd78af_10": "sha256:6d8d4c67222dd894f43462dbd00591d38eb9016940f10e5e3b1c3ce46e19a58f", "1.0.4--r43hdfd78af_11": "sha256:517f528a52565c7e2067848604e10f3ed375df34e425b5dc9728d2a3ba353d83", "1.0.4--r43hdfd78af_12": "sha256:66cfb24b2f029a6e0f7961840ce055e3e6cebfe0be5de6f2a4b7e290dc84a75a", "1.0.4--r44hdfd78af_13": "sha256:a68dbe6670083886a0f19600d5fb582af5770525cbee55880d941293f57db12e"}, "docker": "quay.io/biocontainers/bioconductor-human1mduov3bcrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human1mduov3bcrlmm.
shpc-registry automated BioContainers addition for bioconductor-human1mduov3bcrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human1mduov3bcrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human1mduov3bcrlmm:1.0.4--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human1mduov3bcrlmm/1.0.4--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-human1mduov3bcrlmm/1.0.4--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human1mduov3bcrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human1mduov3bcrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human1mduov3bcrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human1mduov3bcrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human1mduov3bcrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human1mduov3bcrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human1mduov3bcrlmm

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