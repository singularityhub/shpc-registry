---
layout: container
name:  "quay.io/biocontainers/clinker-py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clinker-py/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clinker-py/container.yaml"
updated_at: "2022-10-27 00:36:25.396425"
latest: "0.0.25--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/clinker-py"
aliases:
 - "clinker"
versions:
 - "0.0.25--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for clinker-py"
config: {"url": "https://biocontainers.pro/tools/clinker-py", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clinker-py", "latest": {"0.0.25--pyh5e36f6f_0": "sha256:a732c3d6103353b4e41d32fd02f4b6d108c29a8b40e411b0c1b62fe1c4d1c08f"}, "tags": {"0.0.25--pyh5e36f6f_0": "sha256:a732c3d6103353b4e41d32fd02f4b6d108c29a8b40e411b0c1b62fe1c4d1c08f"}, "docker": "quay.io/biocontainers/clinker-py", "aliases": {"clinker": "/usr/local/bin/clinker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clinker-py.
shpc-registry automated BioContainers addition for clinker-py
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clinker-py
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clinker-py:0.0.25--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clinker-py/0.0.25--pyh5e36f6f_0
$ module help quay.io/biocontainers/clinker-py/0.0.25--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clinker-py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clinker-py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clinker-py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clinker-py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clinker-py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clinker-py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
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