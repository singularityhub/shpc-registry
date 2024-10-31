---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotate/container.yaml"
updated_at: "2024-10-31 03:51:03.345498"
latest: "1.80.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotate"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
 - "1.80.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotate"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotate", "latest": {"1.80.0--r43hdfd78af_0": "sha256:8cd97e6e7a6ddd4667c6328fa8d44ab58ab0afb6f44b73651ba132546c2a6146"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:f15a08a0e6e21164c6ed949598fc89d22b97012c991336184f45c2bf86d67446", "1.76.0--r42hdfd78af_0": "sha256:03da22ca47e1f3f6a7b264dad595e55a4993d73f8ba857bd3cada0365249e168", "1.78.0--r43hdfd78af_0": "sha256:043970351cf954730c6415b69e618ef179d4398330005df56790fbcd257cadf7", "1.80.0--r43hdfd78af_0": "sha256:8cd97e6e7a6ddd4667c6328fa8d44ab58ab0afb6f44b73651ba132546c2a6146"}, "docker": "quay.io/biocontainers/bioconductor-annotate"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotate.
shpc-registry automated BioContainers addition for bioconductor-annotate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotate:1.80.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotate/1.80.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotate/1.80.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-annotate

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