---
layout: container
name:  "ghcr.io/autamus/pdt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/pdt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/pdt/container.yaml"
updated_at: "2024-12-29 02:56:58.076966"
latest: "3.25.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/pdt"

versions:
 - "3.25.1"
 - "latest"
description: "Program Database Toolkit (PDT) is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools."
config: {"docker": "ghcr.io/autamus/pdt", "url": "https://github.com/orgs/autamus/packages/container/package/pdt", "maintainer": "@vsoch", "description": "Program Database Toolkit (PDT) is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools.", "latest": {"3.25.1": "sha256:b8147515318a2b0800afb52c0309d83e90a34fdb27c02e64c71023d30585cf16"}, "tags": {"3.25.1": "sha256:b8147515318a2b0800afb52c0309d83e90a34fdb27c02e64c71023d30585cf16", "latest": "sha256:b8147515318a2b0800afb52c0309d83e90a34fdb27c02e64c71023d30585cf16"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/pdt.
Program Database Toolkit (PDT) is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/pdt
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/pdt:3.25.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/pdt/3.25.1
$ module help ghcr.io/autamus/pdt/3.25.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pdt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pdt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pdt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pdt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pdt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pdt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pdt

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