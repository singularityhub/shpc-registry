---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomeintervals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomeintervals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomeintervals/container.yaml"
updated_at: "2025-10-07 03:26:54.129927"
latest: "1.62.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomeintervals"

versions:
 - "1.50.0--r41hdfd78af_0"
 - "1.54.0--r42hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.62.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomeintervals"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomeintervals", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomeintervals", "latest": {"1.62.0--r44hdfd78af_0": "sha256:a964d628c840b1bf371f50d6060b7ad3b9e545b09f028d20aa4c1a1462930509"}, "tags": {"1.50.0--r41hdfd78af_0": "sha256:95d8e7a3d49a15af4c8dce8dbe8843fe23b610c5fb859f2aaaab67273de4132f", "1.54.0--r42hdfd78af_0": "sha256:c84e050822f7adb249195922e8c9619badcc9cf57c4bef453b5e875c69eaa81a", "1.56.0--r43hdfd78af_0": "sha256:bb4e0ac7ea25b76600c55d9a531730916abed38a25d419286ad0481408202c40", "1.58.0--r43hdfd78af_0": "sha256:d3ba3622fb3b23face34991056852bb27770af939c77412875f272acfc38b0a1", "1.62.0--r44hdfd78af_0": "sha256:a964d628c840b1bf371f50d6060b7ad3b9e545b09f028d20aa4c1a1462930509"}, "docker": "quay.io/biocontainers/bioconductor-genomeintervals"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomeintervals.
shpc-registry automated BioContainers addition for bioconductor-genomeintervals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomeintervals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomeintervals:1.62.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomeintervals/1.62.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomeintervals/1.62.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomeintervals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomeintervals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomeintervals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomeintervals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomeintervals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomeintervals-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomeintervals

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