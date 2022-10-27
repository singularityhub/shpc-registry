---
layout: container
name:  "quay.io/biocontainers/variant_tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/variant_tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/variant_tools/container.yaml"
updated_at: "2022-10-27 00:24:52.607295"
latest: "3.1.3--py36ha7febfa_2"
container_url: "https://biocontainers.pro/tools/variant_tools"
aliases:
 - "vtools"
 - "vtools_report"
 - "worker_run"
versions:
 - "3.1.3--py36ha7febfa_2"
description: "shpc-registry automated BioContainers addition for variant_tools"
config: {"url": "https://biocontainers.pro/tools/variant_tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for variant_tools", "latest": {"3.1.3--py36ha7febfa_2": "sha256:4b20ba746976b8ddb3c36d7df5c6177a0aa6706ac1789db3171d3db8c4935a91"}, "tags": {"3.1.3--py36ha7febfa_2": "sha256:4b20ba746976b8ddb3c36d7df5c6177a0aa6706ac1789db3171d3db8c4935a91"}, "docker": "quay.io/biocontainers/variant_tools", "aliases": {"vtools": "/usr/local/bin/vtools", "vtools_report": "/usr/local/bin/vtools_report", "worker_run": "/usr/local/bin/worker_run"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/variant_tools.
shpc-registry automated BioContainers addition for variant_tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/variant_tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/variant_tools:3.1.3--py36ha7febfa_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/variant_tools/3.1.3--py36ha7febfa_2
$ module help quay.io/biocontainers/variant_tools/3.1.3--py36ha7febfa_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### variant_tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### variant_tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### variant_tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### variant_tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### variant_tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### variant_tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vtools

```bash
$ singularity exec <container> /usr/local/bin/vtools
$ podman run --it --rm --entrypoint /usr/local/bin/vtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtools_report

```bash
$ singularity exec <container> /usr/local/bin/vtools_report
$ podman run --it --rm --entrypoint /usr/local/bin/vtools_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtools_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### worker_run

```bash
$ singularity exec <container> /usr/local/bin/worker_run
$ podman run --it --rm --entrypoint /usr/local/bin/worker_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/worker_run   -v ${PWD} -w ${PWD} <container> -c " $@"
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