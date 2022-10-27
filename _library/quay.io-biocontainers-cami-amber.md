---
layout: container
name:  "quay.io/biocontainers/cami-amber"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cami-amber/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cami-amber/container.yaml"
updated_at: "2022-10-27 00:48:09.278775"
latest: "2.0.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cami-amber"
aliases:
 - "amber.py"
 - "setup.py"
 - "version.py"
versions:
 - "2.0.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cami-amber"
config: {"url": "https://biocontainers.pro/tools/cami-amber", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cami-amber", "latest": {"2.0.3--pyhdfd78af_0": "sha256:6a8dd7db0c43e57440bc1c0ced91a7f74ae25605150709de0fb5b173dc36e9bf"}, "tags": {"2.0.3--pyhdfd78af_0": "sha256:6a8dd7db0c43e57440bc1c0ced91a7f74ae25605150709de0fb5b173dc36e9bf"}, "docker": "quay.io/biocontainers/cami-amber", "aliases": {"amber.py": "/usr/local/bin/amber.py", "setup.py": "/usr/local/bin/setup.py", "version.py": "/usr/local/bin/version.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cami-amber.
shpc-registry automated BioContainers addition for cami-amber
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cami-amber
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cami-amber:2.0.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cami-amber/2.0.3--pyhdfd78af_0
$ module help quay.io/biocontainers/cami-amber/2.0.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cami-amber-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cami-amber-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cami-amber-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cami-amber-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cami-amber-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cami-amber-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amber.py

```bash
$ singularity exec <container> /usr/local/bin/amber.py
$ podman run --it --rm --entrypoint /usr/local/bin/amber.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amber.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.py

```bash
$ singularity exec <container> /usr/local/bin/setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### version.py

```bash
$ singularity exec <container> /usr/local/bin/version.py
$ podman run --it --rm --entrypoint /usr/local/bin/version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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