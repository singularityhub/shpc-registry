---
layout: container
name:  "quay.io/biocontainers/slimm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slimm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slimm/container.yaml"
updated_at: "2025-06-26 04:28:19.508432"
latest: "0.3.4--hd6d6fdc_6"
container_url: "https://biocontainers.pro/tools/slimm"
aliases:
 - "slimm"
 - "slimm_build"
versions:
 - "0.3.4--hf1761c0_3"
 - "0.3.4--h6a68c12_5"
 - "0.3.4--hd6d6fdc_6"
description: "shpc-registry automated BioContainers addition for slimm"
config: {"url": "https://biocontainers.pro/tools/slimm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slimm", "latest": {"0.3.4--hd6d6fdc_6": "sha256:a007e9880696afae9bfd0791779c72d8fe45ac2f11e7165c49027a5b48a23d3f"}, "tags": {"0.3.4--hf1761c0_3": "sha256:f122e5f847a436bfc027174668445ce6c456cf8c57a613e57fb60e6ce0b2188e", "0.3.4--h6a68c12_5": "sha256:d7a741cbbfb8282981c8bc833834c24b4fb39b07d86240fa439adca802e0be1a", "0.3.4--hd6d6fdc_6": "sha256:a007e9880696afae9bfd0791779c72d8fe45ac2f11e7165c49027a5b48a23d3f"}, "docker": "quay.io/biocontainers/slimm", "aliases": {"slimm": "/usr/local/bin/slimm", "slimm_build": "/usr/local/bin/slimm_build"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slimm.
shpc-registry automated BioContainers addition for slimm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slimm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slimm:0.3.4--hd6d6fdc_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slimm/0.3.4--hd6d6fdc_6
$ module help quay.io/biocontainers/slimm/0.3.4--hd6d6fdc_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slimm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slimm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slimm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slimm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slimm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slimm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slimm

```bash
$ singularity exec <container> /usr/local/bin/slimm
$ podman run --it --rm --entrypoint /usr/local/bin/slimm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slimm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slimm_build

```bash
$ singularity exec <container> /usr/local/bin/slimm_build
$ podman run --it --rm --entrypoint /usr/local/bin/slimm_build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slimm_build   -v ${PWD} -w ${PWD} <container> -c " $@"
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