---
layout: container
name:  "quay.io/biocontainers/argparse2tool"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/argparse2tool/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/argparse2tool/container.yaml"
updated_at: "2022-10-27 01:11:42.144199"
latest: "0.4.9--py_0"
container_url: "https://biocontainers.pro/tools/argparse2tool"
aliases:
 - "argparse2tool"
 - "argparse2tool_check_path"
versions:
 - "0.4.9--py_0"
description: "shpc-registry automated BioContainers addition for argparse2tool"
config: {"url": "https://biocontainers.pro/tools/argparse2tool", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for argparse2tool", "latest": {"0.4.9--py_0": "sha256:766e20ed8a92fabd023266fce3eac979381b8536858e94153180c92eb1d044c7"}, "tags": {"0.4.9--py_0": "sha256:766e20ed8a92fabd023266fce3eac979381b8536858e94153180c92eb1d044c7"}, "docker": "quay.io/biocontainers/argparse2tool", "aliases": {"argparse2tool": "/usr/local/bin/argparse2tool", "argparse2tool_check_path": "/usr/local/bin/argparse2tool_check_path"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/argparse2tool.
shpc-registry automated BioContainers addition for argparse2tool
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/argparse2tool
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/argparse2tool:0.4.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/argparse2tool/0.4.9--py_0
$ module help quay.io/biocontainers/argparse2tool/0.4.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### argparse2tool-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### argparse2tool-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### argparse2tool-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### argparse2tool-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### argparse2tool-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### argparse2tool-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### argparse2tool

```bash
$ singularity exec <container> /usr/local/bin/argparse2tool
$ podman run --it --rm --entrypoint /usr/local/bin/argparse2tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/argparse2tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### argparse2tool_check_path

```bash
$ singularity exec <container> /usr/local/bin/argparse2tool_check_path
$ podman run --it --rm --entrypoint /usr/local/bin/argparse2tool_check_path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/argparse2tool_check_path   -v ${PWD} -w ${PWD} <container> -c " $@"
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