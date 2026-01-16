---
layout: container
name:  "quay.io/biocontainers/bioconductor-meat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-meat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-meat/container.yaml"
updated_at: "2026-01-16 04:07:48.034888"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-meat"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-meat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-meat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-meat", "latest": {"1.14.0--r43hdfd78af_0": "sha256:05d7db73742760ffbf5b57ba9f6e8e17063c12b0aa9b858a431582e31ac52e87"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:a3406ef8e296cf71264a4f5c223220b1e2ad0887c6296c382e9e1826a510978e", "1.10.0--r42hdfd78af_0": "sha256:4b58f7309ff67155e7c112f5e2532bb5ca4007f2d31f9a400059866452ec837e", "1.12.0--r43hdfd78af_0": "sha256:d90008b9e7f9804e6e18837c81f1639d81b481faf74f1728f21e98a6346f8744", "1.14.0--r43hdfd78af_0": "sha256:05d7db73742760ffbf5b57ba9f6e8e17063c12b0aa9b858a431582e31ac52e87"}, "docker": "quay.io/biocontainers/bioconductor-meat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-meat.
shpc-registry automated BioContainers addition for bioconductor-meat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-meat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-meat:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-meat/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-meat/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-meat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-meat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-meat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-meat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-meat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-meat

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