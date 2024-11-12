---
layout: container
name:  "ghcr.io/autamus/scons"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/scons/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/scons/container.yaml"
updated_at: "2024-11-12 02:45:55.004731"
latest: "4.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/scons"
aliases:
 - "scons"
 - "scons-3.1.2"
 - "scons-3.1.2.bat"
 - "scons-configure-cache"
 - "scons-configure-cache-3.1.2"
 - "scons-time"
 - "scons-time-3.1.2"
 - "scons.bat"
 - "sconsign"
 - "sconsign-3.1.2"
versions:
 - "3.1.2"
 - "latest"
 - "4.3.0"
description: "SCons is an Open Source software construction tool."
config: {"docker": "ghcr.io/autamus/scons", "url": "https://github.com/orgs/autamus/packages/container/package/scons", "maintainer": "@vsoch", "description": "SCons is an Open Source software construction tool.", "latest": {"4.3.0": "sha256:fe5158258e37b744d27c58cddf50e077b1a17113eb957cf3e8e9305f2a8e2d46"}, "tags": {"3.1.2": "sha256:118047c12783c1d331f8b8a3600994b84b398a79f199cff1d5f8bb02860a599f", "latest": "sha256:fe5158258e37b744d27c58cddf50e077b1a17113eb957cf3e8e9305f2a8e2d46", "4.3.0": "sha256:fe5158258e37b744d27c58cddf50e077b1a17113eb957cf3e8e9305f2a8e2d46"}, "aliases": {"scons": "/opt/view/bin/scons", "scons-3.1.2": "/opt/view/bin/scons-3.1.2", "scons-3.1.2.bat": "/opt/view/bin/scons-3.1.2.bat", "scons-configure-cache": "/opt/view/bin/scons-configure-cache", "scons-configure-cache-3.1.2": "/opt/view/bin/scons-configure-cache-3.1.2", "scons-time": "/opt/view/bin/scons-time", "scons-time-3.1.2": "/opt/view/bin/scons-time-3.1.2", "scons.bat": "/opt/view/bin/scons.bat", "sconsign": "/opt/view/bin/sconsign", "sconsign-3.1.2": "/opt/view/bin/sconsign-3.1.2"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/scons.
SCons is an Open Source software construction tool.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/scons
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/scons:4.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/scons/4.3.0
$ module help ghcr.io/autamus/scons/4.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scons-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scons-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scons-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scons-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scons-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scons-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scons

```bash
$ singularity exec <container> /opt/view/bin/scons
$ podman run --it --rm --entrypoint /opt/view/bin/scons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-3.1.2

```bash
$ singularity exec <container> /opt/view/bin/scons-3.1.2
$ podman run --it --rm --entrypoint /opt/view/bin/scons-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-3.1.2.bat

```bash
$ singularity exec <container> /opt/view/bin/scons-3.1.2.bat
$ podman run --it --rm --entrypoint /opt/view/bin/scons-3.1.2.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-3.1.2.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-configure-cache

```bash
$ singularity exec <container> /opt/view/bin/scons-configure-cache
$ podman run --it --rm --entrypoint /opt/view/bin/scons-configure-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-configure-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-configure-cache-3.1.2

```bash
$ singularity exec <container> /opt/view/bin/scons-configure-cache-3.1.2
$ podman run --it --rm --entrypoint /opt/view/bin/scons-configure-cache-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-configure-cache-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-time

```bash
$ singularity exec <container> /opt/view/bin/scons-time
$ podman run --it --rm --entrypoint /opt/view/bin/scons-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons-time-3.1.2

```bash
$ singularity exec <container> /opt/view/bin/scons-time-3.1.2
$ podman run --it --rm --entrypoint /opt/view/bin/scons-time-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons-time-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scons.bat

```bash
$ singularity exec <container> /opt/view/bin/scons.bat
$ podman run --it --rm --entrypoint /opt/view/bin/scons.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scons.bat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sconsign

```bash
$ singularity exec <container> /opt/view/bin/sconsign
$ podman run --it --rm --entrypoint /opt/view/bin/sconsign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sconsign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sconsign-3.1.2

```bash
$ singularity exec <container> /opt/view/bin/sconsign-3.1.2
$ podman run --it --rm --entrypoint /opt/view/bin/sconsign-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sconsign-3.1.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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