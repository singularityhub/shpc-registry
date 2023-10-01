---
layout: container
name:  "quay.io/biocontainers/r-consensustme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-consensustme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-consensustme/container.yaml"
updated_at: "2023-10-01 03:17:25.971446"
latest: "0.0.1.9000--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-consensustme"

versions:
 - "0.0.1.9000--r41hdfd78af_0"
 - "0.0.1.9000--r42hdfd78af_1"
 - "0.0.1.9000--r43hdfd78af_2"
description: "shpc-registry automated BioContainers addition for r-consensustme"
config: {"url": "https://biocontainers.pro/tools/r-consensustme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-consensustme", "latest": {"0.0.1.9000--r43hdfd78af_2": "sha256:b9517baef001d6a72c6ab539b7c8236cd759cd2be64867196440bdaa0f7295e0"}, "tags": {"0.0.1.9000--r41hdfd78af_0": "sha256:5d420e05b149e5c169b6508157f02f478f38a4f2e6fa79341c3e959e3f0561b1", "0.0.1.9000--r42hdfd78af_1": "sha256:8329d045667c2faff49a96e6b408e673e9c5821c59860297049604189616cab4", "0.0.1.9000--r43hdfd78af_2": "sha256:b9517baef001d6a72c6ab539b7c8236cd759cd2be64867196440bdaa0f7295e0"}, "docker": "quay.io/biocontainers/r-consensustme"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-consensustme.
shpc-registry automated BioContainers addition for r-consensustme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-consensustme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-consensustme:0.0.1.9000--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-consensustme/0.0.1.9000--r43hdfd78af_2
$ module help quay.io/biocontainers/r-consensustme/0.0.1.9000--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-consensustme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-consensustme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-consensustme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-consensustme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-consensustme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-consensustme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-consensustme

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