---
layout: container
name:  "quay.io/biocontainers/gseapy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gseapy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gseapy/container.yaml"
updated_at: "2023-04-09 03:23:10.443088"
latest: "0.10.3--py_0"
container_url: "https://biocontainers.pro/tools/gseapy"

versions:
 - "0.9.9--py_0"
 - "0.10.3--py_0"
 - "0.9.19--py_0"
description: "shpc-registry automated BioContainers addition for gseapy"
config: {"url": "https://biocontainers.pro/tools/gseapy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gseapy", "latest": {"0.10.3--py_0": "sha256:cf64de5b410f92683a319199a544b52f364c15263d996660b9c5dd703725e72e"}, "tags": {"0.9.9--py_0": "sha256:4d88852d9640ca767c2c9d5964c96ebae19414f96f2ad0c074dacba5acaa410c", "0.10.3--py_0": "sha256:cf64de5b410f92683a319199a544b52f364c15263d996660b9c5dd703725e72e", "0.9.19--py_0": "sha256:dfc12e9063073cc1feecb68f06a3537f6d5f8fab06a2e099690f9d4540a9d395"}, "docker": "quay.io/biocontainers/gseapy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gseapy.
shpc-registry automated BioContainers addition for gseapy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gseapy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gseapy:0.10.3--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gseapy/0.10.3--py_0
$ module help quay.io/biocontainers/gseapy/0.10.3--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gseapy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gseapy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gseapy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gseapy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gseapy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gseapy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gseapy

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