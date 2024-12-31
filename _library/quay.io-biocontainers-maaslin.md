---
layout: container
name:  "quay.io/biocontainers/maaslin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maaslin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maaslin/container.yaml"
updated_at: "2024-12-31 03:07:47.780722"
latest: "0.05--r351_0"
container_url: "https://biocontainers.pro/tools/maaslin"

versions:
 - "0.05--r351_0"
description: "shpc-registry automated BioContainers addition for maaslin"
config: {"url": "https://biocontainers.pro/tools/maaslin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for maaslin", "latest": {"0.05--r351_0": "sha256:20f403bf60cfbef747efea6a40abc71febb1990adaa37b37abeb8a738d4a2ec6"}, "tags": {"0.05--r351_0": "sha256:20f403bf60cfbef747efea6a40abc71febb1990adaa37b37abeb8a738d4a2ec6"}, "docker": "quay.io/biocontainers/maaslin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/maaslin.
shpc-registry automated BioContainers addition for maaslin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maaslin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maaslin:0.05--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maaslin/0.05--r351_0
$ module help quay.io/biocontainers/maaslin/0.05--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maaslin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maaslin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maaslin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maaslin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maaslin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maaslin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### maaslin

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