---
layout: container
name:  "quay.io/biocontainers/jbrowse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jbrowse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jbrowse/container.yaml"
updated_at: "2024-02-27 02:55:08.167240"
latest: "1.16.11--pl5321h9f5acd7_5"
container_url: "https://biocontainers.pro/tools/jbrowse"

versions:
 - "1.16.9--pl526hc9558a2_0"
 - "1.16.11--pl5321h9f5acd7_5"
description: "shpc-registry automated BioContainers addition for jbrowse"
config: {"url": "https://biocontainers.pro/tools/jbrowse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jbrowse", "latest": {"1.16.11--pl5321h9f5acd7_5": "sha256:3e45dc608e245eb93abd89df7f0df52d6573befc13209bcbf4dd5b1cbbeded4f"}, "tags": {"1.16.9--pl526hc9558a2_0": "sha256:7890bc0143ec06310503467138bce243105c8c699a0d02ffb2903ac75f44601c", "1.16.11--pl5321h9f5acd7_5": "sha256:3e45dc608e245eb93abd89df7f0df52d6573befc13209bcbf4dd5b1cbbeded4f"}, "docker": "quay.io/biocontainers/jbrowse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/jbrowse.
shpc-registry automated BioContainers addition for jbrowse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jbrowse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jbrowse:1.16.11--pl5321h9f5acd7_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jbrowse/1.16.11--pl5321h9f5acd7_5
$ module help quay.io/biocontainers/jbrowse/1.16.11--pl5321h9f5acd7_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jbrowse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jbrowse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jbrowse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jbrowse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jbrowse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jbrowse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### jbrowse

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