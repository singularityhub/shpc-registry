---
layout: container
name:  "quay.io/biocontainers/bioconductor-target"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-target/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-target/container.yaml"
updated_at: "2023-11-23 04:12:14.321881"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-target"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-target"
config: {"url": "https://biocontainers.pro/tools/bioconductor-target", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-target", "latest": {"1.14.0--r43hdfd78af_0": "sha256:f3e7ed8316a28c618e8d398750667bb8efe3014999bdc3d5c62db129798d31b5"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:c10438260530a2fe354e7904a8e72182d101aadce84916ad8758684b999f807a", "1.12.0--r42hdfd78af_0": "sha256:830a82022c4535909f51e82ca160adad94992eb4820d9541d71cc0a0ca6528bc", "1.14.0--r43hdfd78af_0": "sha256:f3e7ed8316a28c618e8d398750667bb8efe3014999bdc3d5c62db129798d31b5"}, "docker": "quay.io/biocontainers/bioconductor-target"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-target.
shpc-registry automated BioContainers addition for bioconductor-target
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-target
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-target:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-target/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-target/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-target-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-target-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-target-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-target-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-target-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-target-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-target

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