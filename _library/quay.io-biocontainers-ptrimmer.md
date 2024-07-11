---
layout: container
name:  "quay.io/biocontainers/ptrimmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ptrimmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ptrimmer/container.yaml"
updated_at: "2024-07-11 03:42:06.584169"
latest: "1.4.0--h50ea8bc_0"
container_url: "https://biocontainers.pro/tools/ptrimmer"
aliases:
 - "ptrimmer"
versions:
 - "1.3.3--h20b1175_3"
 - "1.3.3--h50ea8bc_5"
 - "1.4.0--h50ea8bc_0"
description: "shpc-registry automated BioContainers addition for ptrimmer"
config: {"url": "https://biocontainers.pro/tools/ptrimmer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ptrimmer", "latest": {"1.4.0--h50ea8bc_0": "sha256:4374f663b77681c9940403a4e2b6e45894cc09b17f8abd2fa5a93147636ca5e3"}, "tags": {"1.3.3--h20b1175_3": "sha256:d516a4370f67baf243fc19cf83f21ce3cec0b9f6112eab48ae9af6a9cf607f0e", "1.3.3--h50ea8bc_5": "sha256:18a091694e62e08b67237af54c6a592ef2887b6e684b90051c04675a5099dd34", "1.4.0--h50ea8bc_0": "sha256:4374f663b77681c9940403a4e2b6e45894cc09b17f8abd2fa5a93147636ca5e3"}, "docker": "quay.io/biocontainers/ptrimmer", "aliases": {"ptrimmer": "/usr/local/bin/ptrimmer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ptrimmer.
shpc-registry automated BioContainers addition for ptrimmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ptrimmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ptrimmer:1.4.0--h50ea8bc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ptrimmer/1.4.0--h50ea8bc_0
$ module help quay.io/biocontainers/ptrimmer/1.4.0--h50ea8bc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ptrimmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ptrimmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ptrimmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ptrimmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ptrimmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ptrimmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ptrimmer

```bash
$ singularity exec <container> /usr/local/bin/ptrimmer
$ podman run --it --rm --entrypoint /usr/local/bin/ptrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrimmer   -v ${PWD} -w ${PWD} <container> -c " $@"
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