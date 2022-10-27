---
layout: container
name:  "quay.io/biocontainers/taco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taco/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/taco/container.yaml"
updated_at: "2022-10-27 01:08:12.484859"
latest: "v0.7.0--py27_0"
container_url: "https://biocontainers.pro/tools/taco"
aliases:
 - "pyi-archive_viewer"
 - "pyi-bindepend"
 - "pyi-grab_version"
 - "pyi-makespec"
 - "pyi-set_version"
 - "pyinstaller"
 - "taco_refcomp"
 - "taco_run"
versions:
 - "v0.7.0--py27_0"
description: "shpc-registry automated BioContainers addition for taco"
config: {"url": "https://biocontainers.pro/tools/taco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taco", "latest": {"v0.7.0--py27_0": "sha256:413c880fd6d29f84293cca1d4f3e0f7ecb883d700445ee31d319da078df09820"}, "tags": {"v0.7.0--py27_0": "sha256:413c880fd6d29f84293cca1d4f3e0f7ecb883d700445ee31d319da078df09820"}, "docker": "quay.io/biocontainers/taco", "aliases": {"pyi-archive_viewer": "/usr/local/bin/pyi-archive_viewer", "pyi-bindepend": "/usr/local/bin/pyi-bindepend", "pyi-grab_version": "/usr/local/bin/pyi-grab_version", "pyi-makespec": "/usr/local/bin/pyi-makespec", "pyi-set_version": "/usr/local/bin/pyi-set_version", "pyinstaller": "/usr/local/bin/pyinstaller", "taco_refcomp": "/usr/local/bin/taco_refcomp", "taco_run": "/usr/local/bin/taco_run"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taco.
shpc-registry automated BioContainers addition for taco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taco:v0.7.0--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taco/v0.7.0--py27_0
$ module help quay.io/biocontainers/taco/v0.7.0--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyi-archive_viewer

```bash
$ singularity exec <container> /usr/local/bin/pyi-archive_viewer
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-archive_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-archive_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-bindepend

```bash
$ singularity exec <container> /usr/local/bin/pyi-bindepend
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-bindepend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-bindepend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-grab_version

```bash
$ singularity exec <container> /usr/local/bin/pyi-grab_version
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-grab_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-grab_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-makespec

```bash
$ singularity exec <container> /usr/local/bin/pyi-makespec
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-makespec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-makespec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyi-set_version

```bash
$ singularity exec <container> /usr/local/bin/pyi-set_version
$ podman run --it --rm --entrypoint /usr/local/bin/pyi-set_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyi-set_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyinstaller

```bash
$ singularity exec <container> /usr/local/bin/pyinstaller
$ podman run --it --rm --entrypoint /usr/local/bin/pyinstaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyinstaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taco_refcomp

```bash
$ singularity exec <container> /usr/local/bin/taco_refcomp
$ podman run --it --rm --entrypoint /usr/local/bin/taco_refcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taco_refcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taco_run

```bash
$ singularity exec <container> /usr/local/bin/taco_run
$ podman run --it --rm --entrypoint /usr/local/bin/taco_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taco_run   -v ${PWD} -w ${PWD} <container> -c " $@"
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