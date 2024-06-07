---
layout: container
name:  "quay.io/biocontainers/collect_mgf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/collect_mgf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/collect_mgf/container.yaml"
updated_at: "2024-06-07 02:35:51.949613"
latest: "1.0--h031d066_5"
container_url: "https://biocontainers.pro/tools/collect_mgf"
aliases:
 - "collect_mgf"
versions:
 - "1.0--hec16e2b_3"
 - "1.0--h031d066_5"
description: "shpc-registry automated BioContainers addition for collect_mgf"
config: {"url": "https://biocontainers.pro/tools/collect_mgf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for collect_mgf", "latest": {"1.0--h031d066_5": "sha256:db072db8aa13159c7a2fc873f4eabbc1c07e260ef1bff3b69f894ca0031d9b9c"}, "tags": {"1.0--hec16e2b_3": "sha256:c65a4f373bda875cd2c457946670d30d44f4f7485a84fcb53ed159fc8eeb2bd1", "1.0--h031d066_5": "sha256:db072db8aa13159c7a2fc873f4eabbc1c07e260ef1bff3b69f894ca0031d9b9c"}, "docker": "quay.io/biocontainers/collect_mgf", "aliases": {"collect_mgf": "/usr/local/bin/collect_mgf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/collect_mgf.
shpc-registry automated BioContainers addition for collect_mgf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/collect_mgf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/collect_mgf:1.0--h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/collect_mgf/1.0--h031d066_5
$ module help quay.io/biocontainers/collect_mgf/1.0--h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### collect_mgf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### collect_mgf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### collect_mgf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### collect_mgf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### collect_mgf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### collect_mgf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### collect_mgf

```bash
$ singularity exec <container> /usr/local/bin/collect_mgf
$ podman run --it --rm --entrypoint /usr/local/bin/collect_mgf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/collect_mgf   -v ${PWD} -w ${PWD} <container> -c " $@"
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