---
layout: container
name:  "quay.io/biocontainers/ephemeris"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ephemeris/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ephemeris/container.yaml"
updated_at: "2022-10-27 00:37:22.344625"
latest: "0.9.0--py_0"
container_url: "https://biocontainers.pro/tools/ephemeris"
aliases:
 - "bioblend-galaxy-tests"
 - "galaxy-wait"
 - "get-tool-list"
 - "run-data-managers"
 - "setup-data-libraries"
 - "shed-tools"
 - "workflow-install"
 - "workflow-to-tools"
versions:
 - "0.9.0--py_0"
description: "shpc-registry automated BioContainers addition for ephemeris"
config: {"url": "https://biocontainers.pro/tools/ephemeris", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ephemeris", "latest": {"0.9.0--py_0": "sha256:7377ee47f373a1cf566ff3f8431132c79818f3904e76a1fcb9b2c64b00e401d2"}, "tags": {"0.9.0--py_0": "sha256:7377ee47f373a1cf566ff3f8431132c79818f3904e76a1fcb9b2c64b00e401d2"}, "docker": "quay.io/biocontainers/ephemeris", "aliases": {"bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "galaxy-wait": "/usr/local/bin/galaxy-wait", "get-tool-list": "/usr/local/bin/get-tool-list", "run-data-managers": "/usr/local/bin/run-data-managers", "setup-data-libraries": "/usr/local/bin/setup-data-libraries", "shed-tools": "/usr/local/bin/shed-tools", "workflow-install": "/usr/local/bin/workflow-install", "workflow-to-tools": "/usr/local/bin/workflow-to-tools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ephemeris.
shpc-registry automated BioContainers addition for ephemeris
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ephemeris
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ephemeris:0.9.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ephemeris/0.9.0--py_0
$ module help quay.io/biocontainers/ephemeris/0.9.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ephemeris-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ephemeris-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ephemeris-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ephemeris-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ephemeris-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ephemeris-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioblend-galaxy-tests

```bash
$ singularity exec <container> /usr/local/bin/bioblend-galaxy-tests
$ podman run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-wait

```bash
$ singularity exec <container> /usr/local/bin/galaxy-wait
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-wait   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-wait   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-tool-list

```bash
$ singularity exec <container> /usr/local/bin/get-tool-list
$ podman run --it --rm --entrypoint /usr/local/bin/get-tool-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-tool-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-data-managers

```bash
$ singularity exec <container> /usr/local/bin/run-data-managers
$ podman run --it --rm --entrypoint /usr/local/bin/run-data-managers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-data-managers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-data-libraries

```bash
$ singularity exec <container> /usr/local/bin/setup-data-libraries
$ podman run --it --rm --entrypoint /usr/local/bin/setup-data-libraries   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-data-libraries   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shed-tools

```bash
$ singularity exec <container> /usr/local/bin/shed-tools
$ podman run --it --rm --entrypoint /usr/local/bin/shed-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shed-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### workflow-install

```bash
$ singularity exec <container> /usr/local/bin/workflow-install
$ podman run --it --rm --entrypoint /usr/local/bin/workflow-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/workflow-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### workflow-to-tools

```bash
$ singularity exec <container> /usr/local/bin/workflow-to-tools
$ podman run --it --rm --entrypoint /usr/local/bin/workflow-to-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/workflow-to-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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