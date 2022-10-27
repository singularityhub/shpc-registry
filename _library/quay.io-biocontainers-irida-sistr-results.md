---
layout: container
name:  "quay.io/biocontainers/irida-sistr-results"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/irida-sistr-results/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/irida-sistr-results/container.yaml"
updated_at: "2022-10-27 00:46:04.196026"
latest: "0.6.0--py_1"
container_url: "https://biocontainers.pro/tools/irida-sistr-results"
aliases:
 - "irida-sistr-results"
versions:
 - "0.6.0--py_1"
description: "shpc-registry automated BioContainers addition for irida-sistr-results"
config: {"url": "https://biocontainers.pro/tools/irida-sistr-results", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for irida-sistr-results", "latest": {"0.6.0--py_1": "sha256:1a4ab2f36aa3b449803acca2d50aea9040b15332fc987b4197ef22faaca6fa20"}, "tags": {"0.6.0--py_1": "sha256:1a4ab2f36aa3b449803acca2d50aea9040b15332fc987b4197ef22faaca6fa20"}, "docker": "quay.io/biocontainers/irida-sistr-results", "aliases": {"irida-sistr-results": "/usr/local/bin/irida-sistr-results"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/irida-sistr-results.
shpc-registry automated BioContainers addition for irida-sistr-results
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/irida-sistr-results
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/irida-sistr-results:0.6.0--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/irida-sistr-results/0.6.0--py_1
$ module help quay.io/biocontainers/irida-sistr-results/0.6.0--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### irida-sistr-results-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### irida-sistr-results-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### irida-sistr-results-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### irida-sistr-results-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### irida-sistr-results-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### irida-sistr-results-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### irida-sistr-results

```bash
$ singularity exec <container> /usr/local/bin/irida-sistr-results
$ podman run --it --rm --entrypoint /usr/local/bin/irida-sistr-results   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irida-sistr-results   -v ${PWD} -w ${PWD} <container> -c " $@"
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