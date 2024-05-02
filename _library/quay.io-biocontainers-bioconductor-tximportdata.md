---
layout: container
name:  "quay.io/biocontainers/bioconductor-tximportdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tximportdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tximportdata/container.yaml"
updated_at: "2024-05-02 03:32:22.328856"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tximportdata"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tximportdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tximportdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tximportdata", "latest": {"1.30.0--r43hdfd78af_0": "sha256:e0e3caf0513adf62e82635f1eaadebed1d3e120c549d81fac713180eb0191871"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:d77a156fb317956ea698f58e2e9ce1e549ddd473581a4d9e6725886d63e86d02", "1.25.0--r42hdfd78af_0": "sha256:09b36c2bd943940755c70c8b4191157dcaa83b9c75fdc2b1a78141a4e4dfc392", "1.28.0--r43hdfd78af_0": "sha256:84d87466660b96facf65244411f9c82583309c9c96ca869d3f774bac0f0dc044", "1.30.0--r43hdfd78af_0": "sha256:e0e3caf0513adf62e82635f1eaadebed1d3e120c549d81fac713180eb0191871"}, "docker": "quay.io/biocontainers/bioconductor-tximportdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tximportdata.
shpc-registry automated BioContainers addition for bioconductor-tximportdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tximportdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tximportdata:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tximportdata/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tximportdata/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tximportdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximportdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tximportdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tximportdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tximportdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tximportdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tximportdata

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