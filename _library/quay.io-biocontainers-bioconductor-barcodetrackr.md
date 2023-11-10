---
layout: container
name:  "quay.io/biocontainers/bioconductor-barcodetrackr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-barcodetrackr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-barcodetrackr/container.yaml"
updated_at: "2023-11-10 02:36:21.779488"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-barcodetrackr"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-barcodetrackr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-barcodetrackr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-barcodetrackr", "latest": {"1.8.0--r43hdfd78af_0": "sha256:9fc5bc8bf074aa1362ab9ec5dabd56a8a93a9b880145380ecbc80cc900a756af"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:c920bd9215d067e9a186932f8659e1af1aada1a88c70129518b0af275239af16", "1.6.0--r42hdfd78af_0": "sha256:a658721edee1c8ca237cf3670605072b9e25706b2745dc9dcceeecf273506f82", "1.8.0--r43hdfd78af_0": "sha256:9fc5bc8bf074aa1362ab9ec5dabd56a8a93a9b880145380ecbc80cc900a756af"}, "docker": "quay.io/biocontainers/bioconductor-barcodetrackr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-barcodetrackr.
shpc-registry automated BioContainers addition for bioconductor-barcodetrackr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-barcodetrackr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-barcodetrackr:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-barcodetrackr/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-barcodetrackr/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-barcodetrackr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barcodetrackr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barcodetrackr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-barcodetrackr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-barcodetrackr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-barcodetrackr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-barcodetrackr

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