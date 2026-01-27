---
layout: container
name:  "quay.io/biocontainers/bioconductor-humanstemcell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-humanstemcell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-humanstemcell/container.yaml"
updated_at: "2026-01-27 04:27:32.509200"
latest: "0.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-humanstemcell"

versions:
 - "0.34.0--r41hdfd78af_1"
 - "0.38.0--r42hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
 - "0.42.0--r43hdfd78af_0"
 - "0.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-humanstemcell"
config: {"url": "https://biocontainers.pro/tools/bioconductor-humanstemcell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-humanstemcell", "latest": {"0.46.0--r44hdfd78af_0": "sha256:97e04e543866751fa33060ae512d249e486409be9dd31ca511498cd330232795"}, "tags": {"0.34.0--r41hdfd78af_1": "sha256:4b8d46e1d738ebd8470b72ea25dc9fff33b5f9e95cb3b26e5dbeac478da89f36", "0.38.0--r42hdfd78af_0": "sha256:cad5c911521c3e8a2999dd0e434783cc78cc8f2a85b1a8e1df24d8505b81b8c8", "0.40.0--r43hdfd78af_0": "sha256:7493972944c1471e7975c6150b87da5c5548a398c44e1dd4b198c9e3f6f3b343", "0.42.0--r43hdfd78af_0": "sha256:8c0a681620a2c13bb594af8b96045f9f4ede8e8c97b3d3835bb09e439d883976", "0.46.0--r44hdfd78af_0": "sha256:97e04e543866751fa33060ae512d249e486409be9dd31ca511498cd330232795"}, "docker": "quay.io/biocontainers/bioconductor-humanstemcell"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-humanstemcell.
shpc-registry automated BioContainers addition for bioconductor-humanstemcell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-humanstemcell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-humanstemcell:0.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-humanstemcell/0.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-humanstemcell/0.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-humanstemcell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanstemcell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-humanstemcell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-humanstemcell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-humanstemcell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-humanstemcell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-humanstemcell

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