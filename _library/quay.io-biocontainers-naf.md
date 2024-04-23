---
layout: container
name:  "quay.io/biocontainers/naf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/naf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/naf/container.yaml"
updated_at: "2024-04-23 02:58:05.423668"
latest: "1.3.0--h031d066_4"
container_url: "https://biocontainers.pro/tools/naf"
aliases:
 - "ennaf"
 - "unnaf"
versions:
 - "1.3.0--hec16e2b_2"
 - "1.3.0--h031d066_4"
description: "shpc-registry automated BioContainers addition for naf"
config: {"url": "https://biocontainers.pro/tools/naf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for naf", "latest": {"1.3.0--h031d066_4": "sha256:ea9012c88ba5e8ad460c809cec1a182a4f3d317bad0701dda90155caf8f36338"}, "tags": {"1.3.0--hec16e2b_2": "sha256:80fc33cd777cd2d54eea4e5fcf5742603c35b5b1443418b7e751e45b543ac436", "1.3.0--h031d066_4": "sha256:ea9012c88ba5e8ad460c809cec1a182a4f3d317bad0701dda90155caf8f36338"}, "docker": "quay.io/biocontainers/naf", "aliases": {"ennaf": "/usr/local/bin/ennaf", "unnaf": "/usr/local/bin/unnaf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/naf.
shpc-registry automated BioContainers addition for naf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/naf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/naf:1.3.0--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/naf/1.3.0--h031d066_4
$ module help quay.io/biocontainers/naf/1.3.0--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### naf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### naf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### naf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### naf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### naf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### naf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ennaf

```bash
$ singularity exec <container> /usr/local/bin/ennaf
$ podman run --it --rm --entrypoint /usr/local/bin/ennaf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ennaf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unnaf

```bash
$ singularity exec <container> /usr/local/bin/unnaf
$ podman run --it --rm --entrypoint /usr/local/bin/unnaf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unnaf   -v ${PWD} -w ${PWD} <container> -c " $@"
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