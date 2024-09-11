---
layout: container
name:  "quay.io/biocontainers/bioconductor-pandar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pandar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pandar/container.yaml"
updated_at: "2024-09-11 03:10:24.381963"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pandar"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pandar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pandar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pandar", "latest": {"1.34.0--r43hdfd78af_0": "sha256:fc9cb31c980580252517a9b66e04c8efd64340274d98ef0c45e3f18d3c407d85"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:bb51fff2fd55848beb3e4b242126b25bb0bb0cd57e529d41bd2d29b6523b304e", "1.30.0--r42hdfd78af_0": "sha256:0ae86544880edaea2c42c450ab4361c77113489bb64fb9286101ad6aeeb025d8", "1.32.0--r43hdfd78af_0": "sha256:d1874d1c5e4b01586cf8366861c0287422b032643c110478fa9b978bd0239134", "1.34.0--r43hdfd78af_0": "sha256:fc9cb31c980580252517a9b66e04c8efd64340274d98ef0c45e3f18d3c407d85"}, "docker": "quay.io/biocontainers/bioconductor-pandar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pandar.
shpc-registry automated BioContainers addition for bioconductor-pandar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pandar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pandar:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pandar/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pandar/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pandar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pandar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pandar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pandar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pandar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pandar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pandar

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