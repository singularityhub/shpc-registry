---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipseq/container.yaml"
updated_at: "2023-11-02 03:23:31.192784"
latest: "1.50.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipseq"

versions:
 - "1.44.0--r41hc0cfd56_2"
 - "1.48.0--r42hc0cfd56_0"
 - "1.48.0--r42ha9d7317_1"
 - "1.50.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipseq", "latest": {"1.50.0--r43ha9d7317_0": "sha256:3ec85dc74ba0397ddf8a43605c91d75bdddf84fddc7bed8d7befd612554ff126"}, "tags": {"1.44.0--r41hc0cfd56_2": "sha256:46557c6760698a5ec2655a4d39af68972b37a9fcf4b60839403a6cf97ff9b0fb", "1.48.0--r42hc0cfd56_0": "sha256:f878092225bbbfa38b02e51c9eae1b92e1c3759a90ab6ec26f00b0d5d722786c", "1.48.0--r42ha9d7317_1": "sha256:787f770d03682c1d744ab997c8f1f0a5d20b4a104e047dccdb2e275ca70a397c", "1.50.0--r43ha9d7317_0": "sha256:3ec85dc74ba0397ddf8a43605c91d75bdddf84fddc7bed8d7befd612554ff126"}, "docker": "quay.io/biocontainers/bioconductor-chipseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipseq.
shpc-registry automated BioContainers addition for bioconductor-chipseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseq:1.50.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipseq/1.50.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-chipseq/1.50.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chipseq

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