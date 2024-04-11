---
layout: container
name:  "quay.io/biocontainers/bioconductor-psygenet2r"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-psygenet2r/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-psygenet2r/container.yaml"
updated_at: "2024-04-11 02:36:42.191401"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-psygenet2r"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.2--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-psygenet2r"
config: {"url": "https://biocontainers.pro/tools/bioconductor-psygenet2r", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-psygenet2r", "latest": {"1.34.0--r43hdfd78af_0": "sha256:0768052c20eacca7421e824632f08e6d4f03181a8d196c3c98d4ffc6ab6ad21a"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:3304b4151619eb0d3d13ab28b5a6aec7ebd5c7477c40b966aa324ecaa6eaec6b", "1.30.0--r42hdfd78af_0": "sha256:e6549459049025002e31ea0cc1978d338a1323075b40dc5252c58aa8b06af1c7", "1.32.2--r43hdfd78af_0": "sha256:4a0ded080a7a59bfa077f013f37ded0d301e1884503e8366516bd95eda71bf8e", "1.34.0--r43hdfd78af_0": "sha256:0768052c20eacca7421e824632f08e6d4f03181a8d196c3c98d4ffc6ab6ad21a"}, "docker": "quay.io/biocontainers/bioconductor-psygenet2r"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-psygenet2r.
shpc-registry automated BioContainers addition for bioconductor-psygenet2r
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-psygenet2r
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-psygenet2r:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-psygenet2r/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-psygenet2r/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-psygenet2r-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psygenet2r-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-psygenet2r-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-psygenet2r-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-psygenet2r-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-psygenet2r-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-psygenet2r

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