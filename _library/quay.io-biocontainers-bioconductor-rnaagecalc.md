---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaagecalc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaagecalc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaagecalc/container.yaml"
updated_at: "2024-12-11 03:22:00.455917"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaagecalc"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaagecalc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaagecalc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaagecalc", "latest": {"1.14.0--r43hdfd78af_0": "sha256:d28807bd8fa469fec4a8c0864b629927b61d1663096534353f2d63922f6bef5e"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:1385cf0b42fb7fcbda7498ea0e2abbb4898be695e30c653c22253b9d46d15bf0", "1.10.0--r42hdfd78af_0": "sha256:6187f851226644a5714b18276362dafe288bc37bb090527a87d001bd5bf7b44f", "1.12.0--r43hdfd78af_0": "sha256:21a26bb1d4e9dea850bd0f55f9312dabfe6e6c4b3913de3d383ff34fc1567369", "1.14.0--r43hdfd78af_0": "sha256:d28807bd8fa469fec4a8c0864b629927b61d1663096534353f2d63922f6bef5e"}, "docker": "quay.io/biocontainers/bioconductor-rnaagecalc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaagecalc.
shpc-registry automated BioContainers addition for bioconductor-rnaagecalc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaagecalc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaagecalc:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaagecalc/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaagecalc/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaagecalc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaagecalc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaagecalc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaagecalc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaagecalc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaagecalc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaagecalc

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