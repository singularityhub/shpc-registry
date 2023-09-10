---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133atagprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133atagprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133atagprobe/container.yaml"
updated_at: "2023-09-10 03:03:43.312772"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133atagprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133atagprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133atagprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133atagprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:89030895a82aeae7802c5aa92b340c6327a23b71eca5ace7455616e15c8bdfc8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:69b7ef0dc051f7a15062d9f14205c218660e3d353ac6b26c420a5dee3d8d7925", "2.18.0--r42hdfd78af_10": "sha256:cb65f60af0bf408cb2fdc732231de89d2410cac747d381f72e2d25ba8c4e5dc6", "2.18.0--r43hdfd78af_11": "sha256:89030895a82aeae7802c5aa92b340c6327a23b71eca5ace7455616e15c8bdfc8"}, "docker": "quay.io/biocontainers/bioconductor-hgu133atagprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133atagprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu133atagprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133atagprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133atagprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133atagprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-hgu133atagprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133atagprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133atagprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133atagprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133atagprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133atagprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133atagprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133atagprobe

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