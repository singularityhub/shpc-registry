---
layout: container
name:  "quay.io/biocontainers/bioconductor-icheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-icheck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-icheck/container.yaml"
updated_at: "2025-01-07 02:53:40.509788"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-icheck"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-icheck"
config: {"url": "https://biocontainers.pro/tools/bioconductor-icheck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-icheck", "latest": {"1.32.0--r43hdfd78af_0": "sha256:4174fb7ea4244c6f6a4574aeb85fb66d2a5f79a01cb94bfd6d36816e033ae41e"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:3f35eee52d4f58e9bc9d1a351abccc25df11c42c4c3b1fbc6778e395b9b515d6", "1.28.0--r42hdfd78af_0": "sha256:bba90b4fe2b6e597127f73ef90e763f2ba6fa74678926e60b6606bcef0d55285", "1.30.0--r43hdfd78af_0": "sha256:500c96bec6c5e057b83757faa3d850158162f9a9a47001de9be3598c5e089b3b", "1.32.0--r43hdfd78af_0": "sha256:4174fb7ea4244c6f6a4574aeb85fb66d2a5f79a01cb94bfd6d36816e033ae41e"}, "docker": "quay.io/biocontainers/bioconductor-icheck"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-icheck.
shpc-registry automated BioContainers addition for bioconductor-icheck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-icheck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-icheck:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-icheck/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-icheck/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-icheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-icheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-icheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-icheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-icheck

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