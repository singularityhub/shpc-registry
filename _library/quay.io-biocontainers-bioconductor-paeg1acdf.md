---
layout: container
name:  "quay.io/biocontainers/bioconductor-paeg1acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-paeg1acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-paeg1acdf/container.yaml"
updated_at: "2025-05-21 04:04:01.992749"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-paeg1acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-paeg1acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-paeg1acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-paeg1acdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:5c7e2836cd5fa5e47204cc56f371745bee471dfe236c1d3d9e2b39d96f6323cf"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:324a57bbf1f1b3e81f3e3995144d365daa6641c92ed8bb13e91bcf7ff62f4471", "2.18.0--r42hdfd78af_10": "sha256:bbf0ac698dec54cc8d22955c51b9c27189527f16391f2280b5fa1ec9e6c8c044", "2.18.0--r43hdfd78af_11": "sha256:4f3d21012f1948412da62e77820ed2b98a33483355049f1d71b57ddacd76877c", "2.18.0--r43hdfd78af_12": "sha256:ba6891688f747bb836aaceabde52e60f80967b70a24fe06bbeacb291a3ab8b2c", "2.18.0--r44hdfd78af_13": "sha256:5c7e2836cd5fa5e47204cc56f371745bee471dfe236c1d3d9e2b39d96f6323cf"}, "docker": "quay.io/biocontainers/bioconductor-paeg1acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-paeg1acdf.
shpc-registry automated BioContainers addition for bioconductor-paeg1acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-paeg1acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-paeg1acdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-paeg1acdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-paeg1acdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-paeg1acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paeg1acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paeg1acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-paeg1acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-paeg1acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-paeg1acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-paeg1acdf

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