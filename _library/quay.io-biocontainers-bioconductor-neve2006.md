---
layout: container
name:  "quay.io/biocontainers/bioconductor-neve2006"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-neve2006/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-neve2006/container.yaml"
updated_at: "2023-10-04 04:57:02.331706"
latest: "0.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-neve2006"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.36.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-neve2006"
config: {"url": "https://biocontainers.pro/tools/bioconductor-neve2006", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-neve2006", "latest": {"0.38.0--r43hdfd78af_0": "sha256:1eb751e520e5cd768041c9b9f3bb0d49ab7a24fc585092400cb985d453b95ae2"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:f8b50cf9a41c4da68c4ab82bf8ae113ac2cf3224c0b868f48e0ef8c9e446496d", "0.36.0--r42hdfd78af_0": "sha256:9da9d9b7bc652c6afdf196b6ba2a2c3abbe295db5ba0c6392dcce607c3c2fbbe", "0.38.0--r43hdfd78af_0": "sha256:1eb751e520e5cd768041c9b9f3bb0d49ab7a24fc585092400cb985d453b95ae2"}, "docker": "quay.io/biocontainers/bioconductor-neve2006"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-neve2006.
shpc-registry automated BioContainers addition for bioconductor-neve2006
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-neve2006
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-neve2006:0.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-neve2006/0.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-neve2006/0.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-neve2006-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neve2006-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neve2006-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-neve2006-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-neve2006-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-neve2006-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-neve2006

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