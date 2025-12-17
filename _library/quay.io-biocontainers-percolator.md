---
layout: container
name:  "quay.io/biocontainers/percolator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/percolator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/percolator/container.yaml"
updated_at: "2025-12-17 03:35:09.309582"
latest: "3.7.1--h3b5f4bd_2"
container_url: "https://biocontainers.pro/tools/percolator"

versions:
 - "3.5--hfd1433f_1"
 - "3.6.5--h6351f2a_0"
 - "3.7.1--h6351f2a_0"
 - "3.7.1--h3b5f4bd_2"
description: "shpc-registry automated BioContainers addition for percolator"
config: {"url": "https://biocontainers.pro/tools/percolator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for percolator", "latest": {"3.7.1--h3b5f4bd_2": "sha256:4a1adac966b750d456068c44aac31dfcacf644460701d2345e18a6093060c2a3"}, "tags": {"3.5--hfd1433f_1": "sha256:4ce8cd765f340f4fb6c0775a018326dd700953ac55cc1c7fe8c55da633c7d817", "3.6.5--h6351f2a_0": "sha256:8e1282f46ef47d950605cc0be4797cedef4b2f70fe552519350d48510b6987af", "3.7.1--h6351f2a_0": "sha256:9931ae0159b6176c6d38f64a7ef6d6d82899c44510487a053acc6cf0b76f8354", "3.7.1--h3b5f4bd_2": "sha256:4a1adac966b750d456068c44aac31dfcacf644460701d2345e18a6093060c2a3"}, "docker": "quay.io/biocontainers/percolator"}
---

This module is a singularity container wrapper for quay.io/biocontainers/percolator.
shpc-registry automated BioContainers addition for percolator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/percolator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/percolator:3.7.1--h3b5f4bd_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/percolator/3.7.1--h3b5f4bd_2
$ module help quay.io/biocontainers/percolator/3.7.1--h3b5f4bd_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### percolator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### percolator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### percolator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### percolator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### percolator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### percolator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### percolator

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