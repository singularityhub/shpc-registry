---
layout: container
name:  "quay.io/biocontainers/bioconductor-varianttools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-varianttools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-varianttools/container.yaml"
updated_at: "2024-10-01 02:59:50.523075"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-varianttools"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-varianttools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-varianttools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-varianttools", "latest": {"1.44.0--r43hdfd78af_0": "sha256:265b9431d2a2b4a691ad5d9526b4f09eadc3c5b011c299a804882daf61d0a671"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:122e6d95315aac3f319005399bc4e27ff4a1e9a761261f2c38bad1dc1955a8f7", "1.40.0--r42hdfd78af_0": "sha256:ee418d3918a0b0e3de851e8061bc08b58e0b469054c777bb45e7b25ed25e1569", "1.42.0--r43hdfd78af_0": "sha256:7bba2504c6eb0b3d2417e2366d0ad0c18d8ff6207b49ef9ab6ebfd9a11e03643", "1.44.0--r43hdfd78af_0": "sha256:265b9431d2a2b4a691ad5d9526b4f09eadc3c5b011c299a804882daf61d0a671"}, "docker": "quay.io/biocontainers/bioconductor-varianttools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-varianttools.
shpc-registry automated BioContainers addition for bioconductor-varianttools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttools:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-varianttools/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-varianttools/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-varianttools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-varianttools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-varianttools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-varianttools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-varianttools

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