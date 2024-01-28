---
layout: container
name:  "quay.io/biocontainers/bioconductor-qpcrnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qpcrnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qpcrnorm/container.yaml"
updated_at: "2024-01-28 03:46:38.565232"
latest: "1.60.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qpcrnorm"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qpcrnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qpcrnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qpcrnorm", "latest": {"1.60.0--r43hdfd78af_0": "sha256:780074d946704132fb2330839b102b29812b88860e751d8709b9a2428a1b6ef8"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:233fa926d56e9498df9dac32fd9a5f2da555753814502f99726a23e2da4a1889", "1.56.0--r42hdfd78af_0": "sha256:58fa3afe2dd518c7766cbb50cc6e8ae48b0235f69da2319da831ce9a537925a1", "1.58.0--r43hdfd78af_0": "sha256:c72493964cf79ffe3557e41c967e354664d4c2f5101ba1f36ac53304b65ff896", "1.60.0--r43hdfd78af_0": "sha256:780074d946704132fb2330839b102b29812b88860e751d8709b9a2428a1b6ef8"}, "docker": "quay.io/biocontainers/bioconductor-qpcrnorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qpcrnorm.
shpc-registry automated BioContainers addition for bioconductor-qpcrnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qpcrnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qpcrnorm:1.60.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qpcrnorm/1.60.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qpcrnorm/1.60.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qpcrnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qpcrnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qpcrnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qpcrnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qpcrnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qpcrnorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qpcrnorm

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