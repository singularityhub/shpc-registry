---
layout: container
name:  "quay.io/biocontainers/bioconductor-simpintlists"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-simpintlists/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-simpintlists/container.yaml"
updated_at: "2025-02-05 03:05:27.703238"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-simpintlists"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-simpintlists"
config: {"url": "https://biocontainers.pro/tools/bioconductor-simpintlists", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-simpintlists", "latest": {"1.38.0--r43hdfd78af_0": "sha256:bdd427f5af10718303381158cf03a62eefbb680525cf61cb9b047e45a2afa384"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:be2ac42d70eb2186c153c686dbe582961d3ffee9084359265d2e541db40e5799", "1.33.0--r42hdfd78af_0": "sha256:5fb02f0a7deaac7579542f3acd8ed2354ec3c3154be4ec9ab091829a074fcd8d", "1.36.0--r43hdfd78af_0": "sha256:2c1ea61a0cbbfaef13a259497169e862343b1794c10e4017aecaf4e1931506ef", "1.38.0--r43hdfd78af_0": "sha256:bdd427f5af10718303381158cf03a62eefbb680525cf61cb9b047e45a2afa384"}, "docker": "quay.io/biocontainers/bioconductor-simpintlists"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-simpintlists.
shpc-registry automated BioContainers addition for bioconductor-simpintlists
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-simpintlists
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-simpintlists:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-simpintlists/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-simpintlists/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-simpintlists-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simpintlists-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-simpintlists-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-simpintlists-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-simpintlists-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-simpintlists-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-simpintlists

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