---
layout: container
name:  "quay.io/biocontainers/bioconductor-htratfocuscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htratfocuscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htratfocuscdf/container.yaml"
updated_at: "2025-05-22 03:47:37.703738"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-htratfocuscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-htratfocuscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htratfocuscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htratfocuscdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:f8006e17126d3c430aae8068b392a3a1a2789d19d453086fbc7fd717c92a8380"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:e43b4731dfc0f082093a6aeb1d5dd7027427b34c3e976c9ad083181c88cc1e8a", "2.18.0--r42hdfd78af_10": "sha256:a78b4185e519f0420edc5fa6c01f0ddf34091e66a98ea524ee88c4f680ab87c6", "2.18.0--r43hdfd78af_11": "sha256:322829eca1708d630c45f0c27a7da141d858600c85d0c0b22980b8a71ac34aaf", "2.18.0--r43hdfd78af_12": "sha256:92f202fddff9d50ddbb3fed79e349d91ac2c7e932481bd1541a9c93f291182e3", "2.18.0--r44hdfd78af_13": "sha256:f8006e17126d3c430aae8068b392a3a1a2789d19d453086fbc7fd717c92a8380"}, "docker": "quay.io/biocontainers/bioconductor-htratfocuscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htratfocuscdf.
shpc-registry automated BioContainers addition for bioconductor-htratfocuscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htratfocuscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htratfocuscdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htratfocuscdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-htratfocuscdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htratfocuscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htratfocuscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htratfocuscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htratfocuscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htratfocuscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htratfocuscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htratfocuscdf

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