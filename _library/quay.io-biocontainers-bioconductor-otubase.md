---
layout: container
name:  "quay.io/biocontainers/bioconductor-otubase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-otubase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-otubase/container.yaml"
updated_at: "2024-04-25 02:49:17.570252"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-otubase"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-otubase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-otubase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-otubase", "latest": {"1.52.0--r43hdfd78af_0": "sha256:5faac5b405d540dfc92537decd7a1761325d7e0d1aa2a3d17c4ef7588988ffce"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:52f0b8efd231174b4ea641201566a4a560a5286aa43aeecf6cb48050f90eb8c6", "1.48.0--r42hdfd78af_0": "sha256:ee21251070861c38f614e749c4af9a347b018ed6df9f65985941e6f6675a0a7d", "1.50.0--r43hdfd78af_0": "sha256:f9f8ac5a5c6d55be70ad966983d59858e486d88f6d371679024897cbd09d98f9", "1.52.0--r43hdfd78af_0": "sha256:5faac5b405d540dfc92537decd7a1761325d7e0d1aa2a3d17c4ef7588988ffce"}, "docker": "quay.io/biocontainers/bioconductor-otubase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-otubase.
shpc-registry automated BioContainers addition for bioconductor-otubase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-otubase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-otubase:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-otubase/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-otubase/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-otubase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-otubase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-otubase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-otubase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-otubase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-otubase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-otubase

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