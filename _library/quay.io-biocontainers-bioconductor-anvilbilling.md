---
layout: container
name:  "quay.io/biocontainers/bioconductor-anvilbilling"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anvilbilling/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anvilbilling/container.yaml"
updated_at: "2024-08-12 03:53:23.740468"
latest: "1.12.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-anvilbilling"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-anvilbilling"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anvilbilling", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anvilbilling", "latest": {"1.12.0--r43hdfd78af_1": "sha256:b90d1e7418678040889b1c8e4e3857dc79a99e6e8622328be9f331ea59b8f665"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:716ba39d17a0505c332775698ca850de9ec9dfc5553cfcd0c58bbe20f5637b3b", "1.8.0--r42hdfd78af_0": "sha256:d10cc264490830a536f8d19b8408517c21f4b500793c69a92b994ee4d7138007", "1.10.0--r43hdfd78af_0": "sha256:c8d5390129a1b7c0a4cb0eeb7a54f99c342489decbcdd94d801e382815efd628", "1.12.0--r43hdfd78af_1": "sha256:b90d1e7418678040889b1c8e4e3857dc79a99e6e8622328be9f331ea59b8f665"}, "docker": "quay.io/biocontainers/bioconductor-anvilbilling"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anvilbilling.
shpc-registry automated BioContainers addition for bioconductor-anvilbilling
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anvilbilling
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anvilbilling:1.12.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anvilbilling/1.12.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-anvilbilling/1.12.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anvilbilling-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvilbilling-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvilbilling-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anvilbilling-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anvilbilling-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anvilbilling-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-anvilbilling

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