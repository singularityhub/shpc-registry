---
layout: container
name:  "quay.io/biocontainers/bioconductor-pmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pmm/container.yaml"
updated_at: "2025-02-02 03:28:53.949637"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pmm"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pmm", "latest": {"1.38.0--r44hdfd78af_0": "sha256:ff65d6e1f14e1dd9f1a05d6241b0d0aa53091a6bf2b702cd427f129967e3e304"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:d1d42befba5c9a0ba6673756f422efeefdecc0075f29c482b3920fae886552a7", "1.30.0--r42hdfd78af_0": "sha256:564937b59147deeb8af50288159224bff465f8f880dd6d0ad82da75ea8c82cad", "1.32.0--r43hdfd78af_0": "sha256:71f36e0b2418c27b7241f9e2669e9f333494d4118b319763c08c9a9ffcdf6f13", "1.34.0--r43hdfd78af_0": "sha256:35515a38d3bbfb8ec36ab5c74f10b942f1c904a4a3e8c077bef93d173b7bc065", "1.38.0--r44hdfd78af_0": "sha256:ff65d6e1f14e1dd9f1a05d6241b0d0aa53091a6bf2b702cd427f129967e3e304"}, "docker": "quay.io/biocontainers/bioconductor-pmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pmm.
shpc-registry automated BioContainers addition for bioconductor-pmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pmm:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pmm/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pmm/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pmm

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