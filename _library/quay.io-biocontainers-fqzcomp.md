---
layout: container
name:  "quay.io/biocontainers/fqzcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fqzcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fqzcomp/container.yaml"
updated_at: "2023-08-28 03:12:07.490504"
latest: "4.6--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/fqzcomp"
aliases:
 - "fqz_comp"
versions:
 - "4.6--hd03093a_3"
 - "4.6--hd03093a_4"
 - "4.6--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for fqzcomp"
config: {"url": "https://biocontainers.pro/tools/fqzcomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fqzcomp", "latest": {"4.6--hdcf5f25_5": "sha256:e98818d8a5f5207c5c1fbc59b898016f2377e66330e73ff1be2ca80409e1da39"}, "tags": {"4.6--hd03093a_3": "sha256:94f34b44472d749e0832eeaaa24cd1e2d6a358d6a8406d6e0adbb94bff9db8a3", "4.6--hd03093a_4": "sha256:af97e7af72a0a858c7bc9e820051e95af87f55564a15e478e674b8235b7411fe", "4.6--hdcf5f25_5": "sha256:e98818d8a5f5207c5c1fbc59b898016f2377e66330e73ff1be2ca80409e1da39"}, "docker": "quay.io/biocontainers/fqzcomp", "aliases": {"fqz_comp": "/usr/local/bin/fqz_comp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fqzcomp.
shpc-registry automated BioContainers addition for fqzcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fqzcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fqzcomp:4.6--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fqzcomp/4.6--hdcf5f25_5
$ module help quay.io/biocontainers/fqzcomp/4.6--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fqzcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fqzcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fqzcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fqzcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fqzcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fqzcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqz_comp

```bash
$ singularity exec <container> /usr/local/bin/fqz_comp
$ podman run --it --rm --entrypoint /usr/local/bin/fqz_comp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqz_comp   -v ${PWD} -w ${PWD} <container> -c " $@"
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