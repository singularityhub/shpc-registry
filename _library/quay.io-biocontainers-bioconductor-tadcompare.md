---
layout: container
name:  "quay.io/biocontainers/bioconductor-tadcompare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tadcompare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tadcompare/container.yaml"
updated_at: "2024-06-06 02:57:39.010784"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tadcompare"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tadcompare"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tadcompare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tadcompare", "latest": {"1.12.0--r43hdfd78af_0": "sha256:4f742f71094c814d8f995f1532f66c88ece0018791a32a96398346a300a0c2b6"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:0acabca236c5245a6c3f9bae2e448244208445f58ab1d83ab596dc97e40735c0", "1.8.0--r42hdfd78af_0": "sha256:6f25fa13b1e47b1e41b331dcdb91df487b763477333d38c21308010d7225db59", "1.10.0--r43hdfd78af_0": "sha256:675cefa9949f06ec6a6cbb5a8f0928ec1ab591ec822ef08c4acec5f437daeab9", "1.12.0--r43hdfd78af_0": "sha256:4f742f71094c814d8f995f1532f66c88ece0018791a32a96398346a300a0c2b6"}, "docker": "quay.io/biocontainers/bioconductor-tadcompare"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tadcompare.
shpc-registry automated BioContainers addition for bioconductor-tadcompare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tadcompare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tadcompare:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tadcompare/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tadcompare/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tadcompare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tadcompare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tadcompare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tadcompare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tadcompare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tadcompare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tadcompare

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