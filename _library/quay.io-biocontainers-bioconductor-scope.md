---
layout: container
name:  "quay.io/biocontainers/bioconductor-scope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scope/container.yaml"
updated_at: "2024-12-10 03:12:04.574658"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scope"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scope"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scope", "latest": {"1.14.0--r43hdfd78af_0": "sha256:34641618d0205c50f5f14a40f9100d2290cfb1d2cf5159cda4ee5ab060ece5bb"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:c9d481b2cdf07962e53df2e07a7ed0e0d22f72bb68565e3986d2da7ca42c11d8", "1.10.0--r42hdfd78af_0": "sha256:bd6bd383d186ac5dcf78ba04782cf68bfba590b165ba510e9532f0fbaf62080d", "1.12.0--r43hdfd78af_0": "sha256:81a46b53caae17377a6181d2e8caa06854302b119d409ea3b5acf1fb1f6656e3", "1.14.0--r43hdfd78af_0": "sha256:34641618d0205c50f5f14a40f9100d2290cfb1d2cf5159cda4ee5ab060ece5bb"}, "docker": "quay.io/biocontainers/bioconductor-scope"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scope.
shpc-registry automated BioContainers addition for bioconductor-scope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scope:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scope/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scope/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scope

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