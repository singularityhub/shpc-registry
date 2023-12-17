---
layout: container
name:  "quay.io/biocontainers/bioconductor-treesummarizedexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-treesummarizedexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-treesummarizedexperiment/container.yaml"
updated_at: "2023-12-17 02:56:44.703816"
latest: "2.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-treesummarizedexperiment"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-treesummarizedexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-treesummarizedexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-treesummarizedexperiment", "latest": {"2.10.0--r43hdfd78af_0": "sha256:c22b31d28e96f502b87530ebcd8c9f1256d9c7d23ba08a3b2e083ad2ad22a407"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:07479a671c37ad4531b06b675e858f4d85f8171695c9654508346a506375e270", "2.6.0--r42hdfd78af_0": "sha256:05cea31702396ed638861b519fd7ab61f442fb63fb0461563d7e83ee58e3a5c7", "2.8.0--r43hdfd78af_0": "sha256:bc375fb28de91149994b551d5732a91ae9d5307c205b92e590b7002f8ddded1e", "2.10.0--r43hdfd78af_0": "sha256:c22b31d28e96f502b87530ebcd8c9f1256d9c7d23ba08a3b2e083ad2ad22a407"}, "docker": "quay.io/biocontainers/bioconductor-treesummarizedexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-treesummarizedexperiment.
shpc-registry automated BioContainers addition for bioconductor-treesummarizedexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-treesummarizedexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-treesummarizedexperiment:2.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-treesummarizedexperiment/2.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-treesummarizedexperiment/2.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-treesummarizedexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treesummarizedexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-treesummarizedexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-treesummarizedexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-treesummarizedexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-treesummarizedexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-treesummarizedexperiment

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