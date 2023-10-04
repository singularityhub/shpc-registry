---
layout: container
name:  "quay.io/biocontainers/bioconductor-scfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scfa/container.yaml"
updated_at: "2023-10-04 04:41:52.148251"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scfa"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scfa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scfa", "latest": {"1.10.0--r43hdfd78af_0": "sha256:ac089a768541d1503a8c6897be39315124ca6c76e615cb2c3714fa59eaa9eb2d"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:f7f6016aedea93366b69b7c1e7a04bb8cddb145bf17e0d7f7847860e98e85c93", "1.8.0--r42hdfd78af_0": "sha256:9a51a8a26c62c5ac029c118b5b8ced150dcd236f64c0d47393ad4a8b39b85b7c", "1.10.0--r43hdfd78af_0": "sha256:ac089a768541d1503a8c6897be39315124ca6c76e615cb2c3714fa59eaa9eb2d"}, "docker": "quay.io/biocontainers/bioconductor-scfa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scfa.
shpc-registry automated BioContainers addition for bioconductor-scfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scfa:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scfa/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scfa/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scfa

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