---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneticsped"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneticsped/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneticsped/container.yaml"
updated_at: "2023-11-10 02:25:39.663255"
latest: "1.62.1--r43ha1e849b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneticsped"

versions:
 - "1.56.0--r41h38f54d8_2"
 - "1.60.0--r42h38f54d8_0"
 - "1.60.0--r42ha1e849b_1"
 - "1.62.1--r43ha1e849b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneticsped"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneticsped", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneticsped", "latest": {"1.62.1--r43ha1e849b_0": "sha256:a48dbe38314d756baf1fb8b2e29034b9d9f062b288a41c7fc96522eca65a2a9b"}, "tags": {"1.56.0--r41h38f54d8_2": "sha256:f1eec506d1fd6f2e369b2e8eea8f3d8f49693ef08952429ee63676de432e2277", "1.60.0--r42h38f54d8_0": "sha256:4b337e642b65ba084cec459117899c701e7f9f9ef4643d359437f157946beb2a", "1.60.0--r42ha1e849b_1": "sha256:548a349569ada3daa7e896f283da1ffe0f7094edd7e0ce2e53cbfc03b5c5641f", "1.62.1--r43ha1e849b_0": "sha256:a48dbe38314d756baf1fb8b2e29034b9d9f062b288a41c7fc96522eca65a2a9b"}, "docker": "quay.io/biocontainers/bioconductor-geneticsped"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneticsped.
shpc-registry automated BioContainers addition for bioconductor-geneticsped
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneticsped
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneticsped:1.62.1--r43ha1e849b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneticsped/1.62.1--r43ha1e849b_0
$ module help quay.io/biocontainers/bioconductor-geneticsped/1.62.1--r43ha1e849b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneticsped-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneticsped-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneticsped-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneticsped-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneticsped-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneticsped-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneticsped

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