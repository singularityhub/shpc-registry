---
layout: container
name:  "quay.io/biocontainers/bioconductor-exploremodelmatrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-exploremodelmatrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-exploremodelmatrix/container.yaml"
updated_at: "2023-07-21 02:46:08.504372"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-exploremodelmatrix"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-exploremodelmatrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-exploremodelmatrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-exploremodelmatrix", "latest": {"1.12.0--r43hdfd78af_0": "sha256:b0441998b451dc4289dbfeb8ffbce7780ff885ffe1ab4b783f363edabc9f5b12"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:4ec7ee7288a004b15f6eb5ba137d167a5755a245171f27baa8b1270edb581b78", "1.10.0--r42hdfd78af_0": "sha256:bbe7283acd865135b3ef93e246ea7512bedf94309d68d217794ba294255ca303", "1.12.0--r43hdfd78af_0": "sha256:b0441998b451dc4289dbfeb8ffbce7780ff885ffe1ab4b783f363edabc9f5b12"}, "docker": "quay.io/biocontainers/bioconductor-exploremodelmatrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-exploremodelmatrix.
shpc-registry automated BioContainers addition for bioconductor-exploremodelmatrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-exploremodelmatrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-exploremodelmatrix:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-exploremodelmatrix/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-exploremodelmatrix/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-exploremodelmatrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-exploremodelmatrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-exploremodelmatrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-exploremodelmatrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-exploremodelmatrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-exploremodelmatrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-exploremodelmatrix

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