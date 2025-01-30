---
layout: container
name:  "quay.io/biocontainers/bioconductor-packfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-packfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-packfinder/container.yaml"
updated_at: "2025-01-30 03:30:56.337953"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-packfinder"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-packfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-packfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-packfinder", "latest": {"1.18.0--r44hdfd78af_0": "sha256:72b6ee39749bffe537d08f744accd5b71909cc39ee03026879a20dfdd4c83e84"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:b1b1aae7a80d64e707665117e14b0c8e5616d20ebff7561333f83071b9e533c0", "1.10.0--r42hdfd78af_0": "sha256:45538ca4870f116cdfc216d7a56336b06f85261b59b64542389df7f9a8f3a4e5", "1.12.0--r43hdfd78af_0": "sha256:5fe33a288233c494e382db584e53315289aef6be475e2e96e1e6eaaeb6d8acb4", "1.14.0--r43hdfd78af_0": "sha256:985faac5815f0698c43bad27622071fd02d4293cca867958afaac5754a2482d9", "1.18.0--r44hdfd78af_0": "sha256:72b6ee39749bffe537d08f744accd5b71909cc39ee03026879a20dfdd4c83e84"}, "docker": "quay.io/biocontainers/bioconductor-packfinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-packfinder.
shpc-registry automated BioContainers addition for bioconductor-packfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-packfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-packfinder:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-packfinder/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-packfinder/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-packfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-packfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-packfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-packfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-packfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-packfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-packfinder

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