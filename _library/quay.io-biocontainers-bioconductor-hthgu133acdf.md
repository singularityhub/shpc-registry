---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133acdf/container.yaml"
updated_at: "2024-12-02 03:15:16.518099"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133acdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:c496d0cc06277e1ccbcea1501cf4006b2ac83bbb2f3da8708cfc865a596d5c2c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0303159581f59a974e68f8e2a0a0707b88437860e22128999a7153ee5161214e", "2.18.0--r42hdfd78af_10": "sha256:f32b3d9712887f63e3a3a0de3dce25600d1b5933b0dcfb7a4c540f6d91e4fcbb", "2.18.0--r43hdfd78af_11": "sha256:0c3705f89dd93ca2cbaaac91f63c61fd8c7233668871dfa0b3130bbd0e9a0917", "2.18.0--r43hdfd78af_12": "sha256:c496d0cc06277e1ccbcea1501cf4006b2ac83bbb2f3da8708cfc865a596d5c2c"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133acdf.
shpc-registry automated BioContainers addition for bioconductor-hthgu133acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133acdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133acdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hthgu133acdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hthgu133acdf

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