---
layout: container
name:  "quay.io/biocontainers/bioconductor-ashkenazimsonchr21"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ashkenazimsonchr21/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ashkenazimsonchr21/container.yaml"
updated_at: "2024-11-13 03:37:40.805409"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ashkenazimsonchr21"

versions:
 - "1.24.0--r41hdfd78af_1"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ashkenazimsonchr21"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ashkenazimsonchr21", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ashkenazimsonchr21", "latest": {"1.32.0--r43hdfd78af_0": "sha256:e0626d2554465d2241a31f2794a3a5345bf38e433f69acf3921e2dd62315bcb8"}, "tags": {"1.24.0--r41hdfd78af_1": "sha256:8eb01423ea092e3f6b7efc7a28845970a9bd95e1657dde8f72b38123287d9f1d", "1.28.0--r42hdfd78af_0": "sha256:4269b08bb43e5f160b2bac4a85d99a27cc89751c93146f31e7050db6bd8289df", "1.30.0--r43hdfd78af_0": "sha256:639b6ad8bfc3ba4c024147e53df7cf793a14f851e4b949b9924de4b9c5d72232", "1.32.0--r43hdfd78af_0": "sha256:e0626d2554465d2241a31f2794a3a5345bf38e433f69acf3921e2dd62315bcb8"}, "docker": "quay.io/biocontainers/bioconductor-ashkenazimsonchr21"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ashkenazimsonchr21.
shpc-registry automated BioContainers addition for bioconductor-ashkenazimsonchr21
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ashkenazimsonchr21
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ashkenazimsonchr21:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ashkenazimsonchr21/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ashkenazimsonchr21/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ashkenazimsonchr21-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ashkenazimsonchr21-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ashkenazimsonchr21-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ashkenazimsonchr21-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ashkenazimsonchr21-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ashkenazimsonchr21-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ashkenazimsonchr21

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