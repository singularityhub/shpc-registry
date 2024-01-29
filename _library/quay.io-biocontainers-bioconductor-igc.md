---
layout: container
name:  "quay.io/biocontainers/bioconductor-igc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-igc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-igc/container.yaml"
updated_at: "2024-01-29 02:37:09.622905"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-igc"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-igc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-igc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-igc", "latest": {"1.32.0--r43hdfd78af_0": "sha256:8f0a55f0eeaa5c817ac7b730d8136d5b9f35837abf55eaa75519f02254b28d65"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:d9384dbfff9640d00dd5a9023fbd90dedeb714781a3a1e9868c7e6716a74bafa", "1.28.0--r42hdfd78af_0": "sha256:b86839224fc7ec51ac04ceb0bae47fb6455a6bb1c896e481cd0c58cccf32afff", "1.30.0--r43hdfd78af_0": "sha256:9659f27bb2305c51fb7ab18610b63ddd1ad94fc3709187708231032fc771ad74", "1.32.0--r43hdfd78af_0": "sha256:8f0a55f0eeaa5c817ac7b730d8136d5b9f35837abf55eaa75519f02254b28d65"}, "docker": "quay.io/biocontainers/bioconductor-igc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-igc.
shpc-registry automated BioContainers addition for bioconductor-igc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-igc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-igc:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-igc/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-igc/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-igc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-igc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-igc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-igc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-igc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-igc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-igc

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