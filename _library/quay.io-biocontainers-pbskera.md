---
layout: container
name:  "quay.io/biocontainers/pbskera"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbskera/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbskera/container.yaml"
updated_at: "2024-10-24 11:17:15.051876"
latest: "1.2.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pbskera"
aliases:
 - "skera"
versions:
 - "0.1.0--hdfd78af_0"
 - "1.1.0--hdfd78af_0"
 - "1.2.0--hdfd78af_0"
description: "singularity registry hpc automated addition for pbskera"
config: {"url": "https://biocontainers.pro/tools/pbskera", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbskera", "latest": {"1.2.0--hdfd78af_0": "sha256:fdcec73a8b08e57cc2232cfafa2a4b615bf211ccb068400e7cebcc3d78c844f0"}, "tags": {"0.1.0--hdfd78af_0": "sha256:8a78b9f0aad4e26df6d9648451f49df80e096c3f4b96314cab35ea2f4709c34e", "1.1.0--hdfd78af_0": "sha256:752cf06f463a539fbf6b42be73c1deface2a2eea6d8dbfe37e21582ac3f93b26", "1.2.0--hdfd78af_0": "sha256:fdcec73a8b08e57cc2232cfafa2a4b615bf211ccb068400e7cebcc3d78c844f0"}, "docker": "quay.io/biocontainers/pbskera", "aliases": {"skera": "/usr/local/bin/skera"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbskera.
singularity registry hpc automated addition for pbskera
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbskera
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbskera:1.2.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbskera/1.2.0--hdfd78af_0
$ module help quay.io/biocontainers/pbskera/1.2.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbskera-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbskera-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbskera-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbskera-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbskera-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbskera-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skera

```bash
$ singularity exec <container> /usr/local/bin/skera
$ podman run --it --rm --entrypoint /usr/local/bin/skera   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skera   -v ${PWD} -w ${PWD} <container> -c " $@"
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