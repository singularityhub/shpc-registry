---
layout: container
name:  "amdih/namd3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amdih/namd3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amdih/namd3/container.yaml"
updated_at: "2023-11-01 02:26:36.219414"
latest: "3.0a9"
container_url: "https://www.amd.com/en/technologies/infinity-hub/namd"
aliases:
 - "charmrun"
 - "namd3"
versions:
 - "3.0a9"
description: "NAMD is a molecular dynamics package designed for simulating the movement of biomolecules over time."
config: {"docker": "amdih/namd3", "url": "https://www.amd.com/en/technologies/infinity-hub/namd", "description": "NAMD is a molecular dynamics package designed for simulating the movement of biomolecules over time.", "maintainer": "@cristiandipietrantonio", "latest": {"3.0a9": "sha256:d6fcadbfb948b2e92285cd12ce8e06c184c370a370fdc6aec52e3099da64d66b"}, "tags": {"3.0a9": "sha256:d6fcadbfb948b2e92285cd12ce8e06c184c370a370fdc6aec52e3099da64d66b"}, "aliases": [{"name": "charmrun", "command": "/opt/namd/bin/charmrun"}, {"name": "namd3", "command": "/opt/namd/bin/namd3"}]}
---

This module is a singularity container wrapper for amdih/namd3.
NAMD is a molecular dynamics package designed for simulating the movement of biomolecules over time.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amdih/namd3
```

Or a specific version:

```bash
$ shpc install amdih/namd3:3.0a9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amdih/namd3/3.0a9
$ module help amdih/namd3/3.0a9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### namd3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### namd3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### namd3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### namd3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### namd3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### namd3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### charmrun

```bash
$ singularity exec <container> /opt/namd/bin/charmrun
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### namd3

```bash
$ singularity exec <container> /opt/namd/bin/namd3
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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