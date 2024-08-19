---
layout: container
name:  "quay.io/biocontainers/bioconductor-spectra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spectra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spectra/container.yaml"
updated_at: "2024-08-19 03:45:33.694760"
latest: "1.10.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spectra"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spectra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spectra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spectra", "latest": {"1.10.1--r43hdfd78af_0": "sha256:1cb9e134c2442e632156d557dbe46bb44f47fea861ed3e1c2c42a88fbb8f701e"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:84d16b4313d4c1084bc191e047da977ebf5cc742b676067f84dbf6e0ca4a7d24", "1.8.0--r42hdfd78af_0": "sha256:28c74176eee6e81c16a8bfc699b1c61e0aab9db6b5ceb8dde23945b42d27e2d6", "1.10.1--r43hdfd78af_0": "sha256:1cb9e134c2442e632156d557dbe46bb44f47fea861ed3e1c2c42a88fbb8f701e"}, "docker": "quay.io/biocontainers/bioconductor-spectra"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spectra.
shpc-registry automated BioContainers addition for bioconductor-spectra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spectra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spectra:1.10.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spectra/1.10.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spectra/1.10.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spectra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spectra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spectra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spectra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spectra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spectra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spectra

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