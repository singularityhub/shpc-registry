---
layout: container
name:  "ghcr.io/autamus/turbine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/turbine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/turbine/container.yaml"
updated_at: "2025-01-23 02:45:36.094732"
latest: "1.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/turbine"
aliases:
 - "turbine"
 - "turbine-pilot"
 - "turbine-read-doubles"
 - "turbine-write-doubles"
versions:
 - "1.3.0"
 - "latest"
description: "Turbine is the Swift/T runtime"
config: {"docker": "ghcr.io/autamus/turbine", "url": "https://github.com/orgs/autamus/packages/container/package/turbine", "maintainer": "@vsoch", "description": "Turbine is the Swift/T runtime", "latest": {"1.3.0": "sha256:239733cb5509d486647f2c9ac9a1e4e446e258051c0b03a92bd66a8ba1e79fc8"}, "tags": {"1.3.0": "sha256:239733cb5509d486647f2c9ac9a1e4e446e258051c0b03a92bd66a8ba1e79fc8", "latest": "sha256:239733cb5509d486647f2c9ac9a1e4e446e258051c0b03a92bd66a8ba1e79fc8"}, "aliases": {"turbine": "/opt/view/bin/turbine", "turbine-pilot": "/opt/view/bin/turbine-pilot", "turbine-read-doubles": "/opt/view/bin/turbine-read-doubles", "turbine-write-doubles": "/opt/view/bin/turbine-write-doubles"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/turbine.
Turbine is the Swift/T runtime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/turbine
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/turbine:1.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/turbine/1.3.0
$ module help ghcr.io/autamus/turbine/1.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### turbine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### turbine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### turbine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### turbine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### turbine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### turbine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### turbine

```bash
$ singularity exec <container> /opt/view/bin/turbine
$ podman run --it --rm --entrypoint /opt/view/bin/turbine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/turbine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### turbine-pilot

```bash
$ singularity exec <container> /opt/view/bin/turbine-pilot
$ podman run --it --rm --entrypoint /opt/view/bin/turbine-pilot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/turbine-pilot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### turbine-read-doubles

```bash
$ singularity exec <container> /opt/view/bin/turbine-read-doubles
$ podman run --it --rm --entrypoint /opt/view/bin/turbine-read-doubles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/turbine-read-doubles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### turbine-write-doubles

```bash
$ singularity exec <container> /opt/view/bin/turbine-write-doubles
$ podman run --it --rm --entrypoint /opt/view/bin/turbine-write-doubles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/turbine-write-doubles   -v ${PWD} -w ${PWD} <container> -c " $@"
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