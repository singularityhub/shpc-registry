---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocset/container.yaml"
updated_at: "2024-12-08 03:11:54.768013"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocset"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocset", "latest": {"1.16.0--r43hdfd78af_0": "sha256:9a866592f4c37a851ad1d29563fad8c2507d6f1f325d13c96f9d8561ca869a96"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:3a0229fa75b86859d100b37e7c6c885d9739c6c3ee1b36e1a64771be9bb8e747", "1.12.0--r42hdfd78af_0": "sha256:f33a3bb23d5901b9b6b212e394ad1bd5c4b245a3fc31c97d22395718269149e9", "1.14.0--r43hdfd78af_0": "sha256:52f598e0de9b0c547bac43884c2e30355570520d5780ef6aa4ab8ce2792bbed6", "1.16.0--r43hdfd78af_0": "sha256:9a866592f4c37a851ad1d29563fad8c2507d6f1f325d13c96f9d8561ca869a96"}, "docker": "quay.io/biocontainers/bioconductor-biocset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocset.
shpc-registry automated BioContainers addition for bioconductor-biocset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocset:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocset/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocset/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocset

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