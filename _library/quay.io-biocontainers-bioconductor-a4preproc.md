---
layout: container
name:  "quay.io/biocontainers/bioconductor-a4preproc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-a4preproc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-a4preproc/container.yaml"
updated_at: "2024-06-28 02:48:50.121374"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-a4preproc"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-a4preproc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-a4preproc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-a4preproc", "latest": {"1.50.0--r43hdfd78af_0": "sha256:9df0759771efb45f0df0315fe7a2becd7e84d56fb0acf2659a2d29763aa302c4"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:ae935cba2cfd9540eefd618092636b7c82c832035d0ed9ecc804e5a456540dd4", "1.46.0--r42hdfd78af_0": "sha256:ab59ec980ca2305421a2cfa89cf7fdeb19e549990f0d7f07b183b7cb037935c9", "1.48.0--r43hdfd78af_0": "sha256:8f6780f48b91006771af80e52cecabb6dd54050ab486a19c711ef3bfc46a13a0", "1.50.0--r43hdfd78af_0": "sha256:9df0759771efb45f0df0315fe7a2becd7e84d56fb0acf2659a2d29763aa302c4"}, "docker": "quay.io/biocontainers/bioconductor-a4preproc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-a4preproc.
shpc-registry automated BioContainers addition for bioconductor-a4preproc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-a4preproc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-a4preproc:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-a4preproc/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-a4preproc/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-a4preproc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4preproc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4preproc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-a4preproc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-a4preproc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-a4preproc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-a4preproc

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