---
layout: container
name:  "quay.io/biocontainers/bioconductor-proteinprofiles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proteinprofiles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proteinprofiles/container.yaml"
updated_at: "2023-11-24 02:33:46.733547"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proteinprofiles"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proteinprofiles"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proteinprofiles", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proteinprofiles", "latest": {"1.40.0--r43hdfd78af_0": "sha256:aaa0f33c1525e0a456eb66dc927e7e0572aa5648755bf44b7e9d50be2b9b1056"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:505385e153c56ce8b33bfcefddfd636bf5379ecc05d1e97a3656f1cf76a64665", "1.38.0--r42hdfd78af_0": "sha256:77f94affd09ed53a927000eee3a06c5684c997f4033ec55400964f1f9d6cee0a", "1.40.0--r43hdfd78af_0": "sha256:aaa0f33c1525e0a456eb66dc927e7e0572aa5648755bf44b7e9d50be2b9b1056"}, "docker": "quay.io/biocontainers/bioconductor-proteinprofiles"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proteinprofiles.
shpc-registry automated BioContainers addition for bioconductor-proteinprofiles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proteinprofiles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proteinprofiles:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proteinprofiles/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proteinprofiles/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proteinprofiles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteinprofiles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteinprofiles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proteinprofiles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proteinprofiles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proteinprofiles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-proteinprofiles

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