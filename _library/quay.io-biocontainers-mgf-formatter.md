---
layout: container
name:  "quay.io/biocontainers/mgf-formatter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgf-formatter/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mgf-formatter/container.yaml"
updated_at: "2022-10-27 00:27:45.421832"
latest: "1.0.0--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/mgf-formatter"
aliases:
 - "mgf-formatter"
versions:
 - "1.0.0--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for mgf-formatter"
config: {"url": "https://biocontainers.pro/tools/mgf-formatter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mgf-formatter", "latest": {"1.0.0--hdfd78af_3": "sha256:50f2d2d1f002a3404117ac7fb1a9741205c7e432578620d54bf1df456b4b7f34"}, "tags": {"1.0.0--hdfd78af_3": "sha256:50f2d2d1f002a3404117ac7fb1a9741205c7e432578620d54bf1df456b4b7f34"}, "docker": "quay.io/biocontainers/mgf-formatter", "aliases": {"mgf-formatter": "/usr/local/bin/mgf-formatter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgf-formatter.
shpc-registry automated BioContainers addition for mgf-formatter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgf-formatter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgf-formatter:1.0.0--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgf-formatter/1.0.0--hdfd78af_3
$ module help quay.io/biocontainers/mgf-formatter/1.0.0--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgf-formatter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgf-formatter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgf-formatter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgf-formatter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgf-formatter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgf-formatter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mgf-formatter

```bash
$ singularity exec <container> /usr/local/bin/mgf-formatter
$ podman run --it --rm --entrypoint /usr/local/bin/mgf-formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgf-formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
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