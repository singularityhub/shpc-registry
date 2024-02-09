---
layout: container
name:  "quay.io/biocontainers/bioconductor-moe430bcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moe430bcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moe430bcdf/container.yaml"
updated_at: "2024-02-09 02:26:41.890071"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-moe430bcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-moe430bcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moe430bcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moe430bcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:f2aebdb3fef6bb2ba5f441183b66eed3ad6b31883c37291de315ad5fea75ea7e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a8804e44ebbc7c4bcc22aff0912d2ab59672471982f7c2343c3333624f901f50", "2.18.0--r42hdfd78af_10": "sha256:f029ac1a2b7b0f9fb6c4ec86367fb6cf2d900e722430c2b8d127f662e1a7be48", "2.18.0--r43hdfd78af_11": "sha256:a961ebc6f75bb17dcced6ba221dbeb719414290f96ed714a4003a27e68a374d2", "2.18.0--r43hdfd78af_12": "sha256:f2aebdb3fef6bb2ba5f441183b66eed3ad6b31883c37291de315ad5fea75ea7e"}, "docker": "quay.io/biocontainers/bioconductor-moe430bcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moe430bcdf.
shpc-registry automated BioContainers addition for bioconductor-moe430bcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430bcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430bcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moe430bcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-moe430bcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moe430bcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430bcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430bcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moe430bcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moe430bcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moe430bcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moe430bcdf

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