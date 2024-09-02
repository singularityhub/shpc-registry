---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylseekr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylseekr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylseekr/container.yaml"
updated_at: "2024-09-02 04:19:05.894636"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylseekr"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylseekr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylseekr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylseekr", "latest": {"1.42.0--r43hdfd78af_0": "sha256:5f2ae33622ca875fbf07986df34a857acf0521246426b952ea755be6c6da4120"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:fd810c9eb0ab5620b5c8915a51845e25d12796cd40ac70fe8e9229941f466cb7", "1.38.0--r42hdfd78af_0": "sha256:9772acf039a0dab82ecda3462d01165edfb40b33962a3c7f51f79fbd592b49b8", "1.40.0--r43hdfd78af_0": "sha256:2857b6ea2c4708ff179be4a8de7098c755a9dd12747d764c97edb6ff97671275", "1.42.0--r43hdfd78af_0": "sha256:5f2ae33622ca875fbf07986df34a857acf0521246426b952ea755be6c6da4120"}, "docker": "quay.io/biocontainers/bioconductor-methylseekr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylseekr.
shpc-registry automated BioContainers addition for bioconductor-methylseekr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylseekr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylseekr:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylseekr/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylseekr/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylseekr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylseekr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylseekr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylseekr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylseekr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylseekr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylseekr

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