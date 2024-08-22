---
layout: container
name:  "quay.io/biocontainers/bioconductor-derfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-derfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-derfinder/container.yaml"
updated_at: "2024-08-22 03:07:16.392498"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-derfinder"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-derfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-derfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-derfinder", "latest": {"1.36.0--r43hdfd78af_0": "sha256:603c2131dcc2e7325c57a4a348b6c9ddb290e38277195d37aa4a782d93410ef6"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:7fd6b77392a01de04414ac77be6bbfb043df4575cc20066973c8d74f5f0eaa40", "1.32.0--r42hdfd78af_0": "sha256:33adb6dbffed891a17611d910a526c2a34617167517efbfb2380e7fd75f63759", "1.34.0--r43hdfd78af_0": "sha256:155762db1642adf8435549692bc791150798eb5f584afcfa33cdfa7592a25774", "1.36.0--r43hdfd78af_0": "sha256:603c2131dcc2e7325c57a4a348b6c9ddb290e38277195d37aa4a782d93410ef6"}, "docker": "quay.io/biocontainers/bioconductor-derfinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-derfinder.
shpc-registry automated BioContainers addition for bioconductor-derfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-derfinder:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-derfinder/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-derfinder/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-derfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-derfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-derfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-derfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-derfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-derfinder

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