---
layout: container
name:  "quay.io/biocontainers/bioconductor-cntools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cntools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cntools/container.yaml"
updated_at: "2024-12-11 03:20:10.369479"
latest: "1.58.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-cntools"

versions:
 - "1.50.0--r41hc0cfd56_2"
 - "1.54.0--r42hc0cfd56_0"
 - "1.54.0--r42ha9d7317_1"
 - "1.56.0--r43ha9d7317_0"
 - "1.58.0--r43ha9d7317_0"
 - "1.58.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-cntools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cntools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cntools", "latest": {"1.58.0--r43ha9d7317_1": "sha256:fe990f17a03ebce571444be6fa8180621db754ff1c526dc7d0758ff906226d57"}, "tags": {"1.50.0--r41hc0cfd56_2": "sha256:0d0d4bea26c7062e3305028914fd14609be7d56c5fbcab8467462d5f666db578", "1.54.0--r42hc0cfd56_0": "sha256:c82743ab660328cf0fbef0d8a9250d9e4b7d9ced388fb4b488a4d961397f025f", "1.54.0--r42ha9d7317_1": "sha256:da15c3204e4ef2fb319f76a28f950bd0e8424e6f381c622ebde07582e193b81d", "1.56.0--r43ha9d7317_0": "sha256:fcbaa2e812ff5dd6704eb541e06cad8087e4826e8e202a9124c18abbee246db4", "1.58.0--r43ha9d7317_0": "sha256:ec0b263f435dce189057ba65ea2820486c62bf08fa57d3409ed2e2d5ca9bfe04", "1.58.0--r43ha9d7317_1": "sha256:fe990f17a03ebce571444be6fa8180621db754ff1c526dc7d0758ff906226d57"}, "docker": "quay.io/biocontainers/bioconductor-cntools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cntools.
shpc-registry automated BioContainers addition for bioconductor-cntools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cntools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cntools:1.58.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cntools/1.58.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-cntools/1.58.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cntools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cntools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cntools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cntools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cntools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cntools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cntools

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