---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmdiffbamsubset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmdiffbamsubset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmdiffbamsubset/container.yaml"
updated_at: "2023-03-24 02:48:28.624623"
latest: "1.33.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mmdiffbamsubset"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mmdiffbamsubset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmdiffbamsubset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmdiffbamsubset", "latest": {"1.33.0--r42hdfd78af_0": "sha256:3c3ae463b2cd70e2cef98303c0d32ca98f4a40761231d1b22df822562139ae91"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:f653ec8d9ef3e26a4ac10f8e694f8ec653463fb84974b10a3b1a2552f03eb598", "1.33.0--r42hdfd78af_0": "sha256:3c3ae463b2cd70e2cef98303c0d32ca98f4a40761231d1b22df822562139ae91"}, "docker": "quay.io/biocontainers/bioconductor-mmdiffbamsubset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmdiffbamsubset.
shpc-registry automated BioContainers addition for bioconductor-mmdiffbamsubset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmdiffbamsubset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmdiffbamsubset:1.33.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmdiffbamsubset/1.33.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mmdiffbamsubset/1.33.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmdiffbamsubset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmdiffbamsubset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmdiffbamsubset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmdiffbamsubset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmdiffbamsubset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmdiffbamsubset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mmdiffbamsubset

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