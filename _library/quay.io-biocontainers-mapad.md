---
layout: container
name:  "quay.io/biocontainers/mapad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mapad/container.yaml"
updated_at: "2025-12-05 03:58:32.692394"
latest: "0.45.0--ha96b9cd_1"
container_url: "https://biocontainers.pro/tools/mapad"
aliases:
 - "mapad"
versions:
 - "0.41.0--h21d3286_0"
 - "0.42.1--h21d3286_0"
 - "0.42.1--hc9368f3_2"
 - "0.43.0--hc9368f3_0"
 - "0.43.0--ha96b9cd_1"
 - "0.44.1--ha96b9cd_0"
 - "0.45.0--ha96b9cd_1"
description: "singularity registry hpc automated addition for mapad"
config: {"url": "https://biocontainers.pro/tools/mapad", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mapad", "latest": {"0.45.0--ha96b9cd_1": "sha256:3e580afd07f82d65f494bfe1961bf4a70582ca224df1a2f0eaaf73a0c366448b"}, "tags": {"0.41.0--h21d3286_0": "sha256:56e55958c6d4c8c2d71e5ee50d57031efc20ea6a056d729d8d52f1fc9f45636d", "0.42.1--h21d3286_0": "sha256:4b768302a111ee3b7a4c627ef356d1162f82e09ba7408d66190d9368a8f49ff2", "0.42.1--hc9368f3_2": "sha256:33f09242d5bfb7899ea44cc67efbf628cef64cecb4b116de52eb66e10998cbf6", "0.43.0--hc9368f3_0": "sha256:a28ebe78522dc05a1e17d8a3c027f08f72f4f114a5bc07be56f3cebaef96bbe3", "0.43.0--ha96b9cd_1": "sha256:b37d4017610742eb03af3ef82348e227b0a75832a74b85f9414a035347ee2473", "0.44.1--ha96b9cd_0": "sha256:4d668ca759d5c44bff906b29a6eb5a5695459203ff8e6c7cb2a203abb5a2adf0", "0.45.0--ha96b9cd_1": "sha256:3e580afd07f82d65f494bfe1961bf4a70582ca224df1a2f0eaaf73a0c366448b"}, "docker": "quay.io/biocontainers/mapad", "aliases": {"mapad": "/usr/local/bin/mapad"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapad.
singularity registry hpc automated addition for mapad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapad:0.45.0--ha96b9cd_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapad/0.45.0--ha96b9cd_1
$ module help quay.io/biocontainers/mapad/0.45.0--ha96b9cd_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mapad

```bash
$ singularity exec <container> /usr/local/bin/mapad
$ podman run --it --rm --entrypoint /usr/local/bin/mapad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapad   -v ${PWD} -w ${PWD} <container> -c " $@"
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