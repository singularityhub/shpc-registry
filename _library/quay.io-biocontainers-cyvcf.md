---
layout: container
name:  "quay.io/biocontainers/cyvcf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cyvcf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cyvcf/container.yaml"
updated_at: "2024-10-14 17:35:02.688822"
latest: "0.8.0--py27_0"
container_url: "https://biocontainers.pro/tools/cyvcf"

versions:
 - "0.8.0--py27_0"
 - "0.8.0--py35_0"
description: "shpc-registry automated BioContainers addition for cyvcf"
config: {"url": "https://biocontainers.pro/tools/cyvcf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cyvcf", "latest": {"0.8.0--py27_0": "sha256:49f9f3cd8149bda1953901ec9ee3ac1357fb02325e4bc4aff69ebf853400f5cf"}, "tags": {"0.8.0--py27_0": "sha256:49f9f3cd8149bda1953901ec9ee3ac1357fb02325e4bc4aff69ebf853400f5cf", "0.8.0--py35_0": "sha256:3c2631fa48746a884364161b13342b3f8d9ec0aa7654cda89ef90ce33c073633"}, "docker": "quay.io/biocontainers/cyvcf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/cyvcf.
shpc-registry automated BioContainers addition for cyvcf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cyvcf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cyvcf:0.8.0--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cyvcf/0.8.0--py27_0
$ module help quay.io/biocontainers/cyvcf/0.8.0--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cyvcf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cyvcf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cyvcf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cyvcf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cyvcf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cyvcf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cyvcf

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