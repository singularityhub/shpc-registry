---
layout: container
name:  "quay.io/biocontainers/bioconductor-clustifyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clustifyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clustifyr/container.yaml"
updated_at: "2024-10-13 10:51:02.458458"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clustifyr"

versions:
 - "1.5.1--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clustifyr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clustifyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clustifyr", "latest": {"1.14.0--r43hdfd78af_0": "sha256:5f8b3eea3f0b51eb2a0488f9d10e23cdd9ef1b70254968a8c6d229886fd13e5e"}, "tags": {"1.5.1--r41hdfd78af_0": "sha256:d0a5d2f90b3ffdc4cfb419b08c3fe0a52946fb778299501e8adfc094153c3844", "1.10.0--r42hdfd78af_0": "sha256:db97d1965aa2898ca7bf7ab9ea8d968067ddee4b5b0ffffb29bd96cc382cc866", "1.12.0--r43hdfd78af_0": "sha256:50a6cc3c715912cd20c9e7e55fbca4de92acddb7abac9d02f71d91093629e682", "1.14.0--r43hdfd78af_0": "sha256:5f8b3eea3f0b51eb2a0488f9d10e23cdd9ef1b70254968a8c6d229886fd13e5e"}, "docker": "quay.io/biocontainers/bioconductor-clustifyr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clustifyr.
shpc-registry automated BioContainers addition for bioconductor-clustifyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clustifyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clustifyr:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clustifyr/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clustifyr/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clustifyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustifyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustifyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clustifyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clustifyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clustifyr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clustifyr

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