---
layout: container
name:  "quay.io/biocontainers/bioconductor-htmg430acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htmg430acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htmg430acdf/container.yaml"
updated_at: "2025-10-09 04:53:45.470954"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-htmg430acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-htmg430acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htmg430acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htmg430acdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:be13a1440c6e7367bc0484432a6a987db440d0a717fd9e6114baf3524a7309a2"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:152eabe1f24019d7a8400c5a9fd4856991704e03503a5fa6ead73a9974d1b5e0", "2.18.0--r42hdfd78af_10": "sha256:fc06d8382d9154ea65b2e80c5649ade2791e5ee7437f799fb8e71ff8cead89e9", "2.18.0--r43hdfd78af_11": "sha256:58ffa2929263c4980167133283c8ab1537aaf5425e071b10e4345a7500d75216", "2.18.0--r43hdfd78af_12": "sha256:d7ffecef3cb1ad8b552dc8fb5a3055c7dc96f385ac566ab9e52778db8559fb71", "2.18.0--r44hdfd78af_13": "sha256:be13a1440c6e7367bc0484432a6a987db440d0a717fd9e6114baf3524a7309a2"}, "docker": "quay.io/biocontainers/bioconductor-htmg430acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htmg430acdf.
shpc-registry automated BioContainers addition for bioconductor-htmg430acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htmg430acdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htmg430acdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-htmg430acdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htmg430acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htmg430acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htmg430acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htmg430acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htmg430acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htmg430acdf

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