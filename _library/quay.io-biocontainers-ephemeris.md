---
layout: container
name:  "quay.io/biocontainers/ephemeris"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ephemeris/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ephemeris/container.yaml"
updated_at: "2023-07-01 03:33:04.679719"
latest: "0.10.8--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/ephemeris"
aliases:
 - "bioblend-galaxy-tests"
 - "galaxy-tool-test"
 - "galaxy-wait"
 - "get-tool-list"
 - "mulled-build"
 - "mulled-build-channel"
 - "mulled-build-files"
 - "mulled-build-tool"
 - "mulled-search"
 - "run-data-managers"
 - "setup-data-libraries"
 - "shed-tools"
 - "workflow-install"
 - "workflow-to-tools"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
 - "glacier"
versions:
 - "0.9.0--py_0"
 - "0.10.7--pyh5e36f6f_0"
 - "0.10.8--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for ephemeris"
config: {"url": "https://biocontainers.pro/tools/ephemeris", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ephemeris", "latest": {"0.10.8--pyh7cba7a3_0": "sha256:4da1f8be8965e0f4f5d28d982ea0875fd22d24fb1efdeae0fa8f53962b3b202d"}, "tags": {"0.9.0--py_0": "sha256:7377ee47f373a1cf566ff3f8431132c79818f3904e76a1fcb9b2c64b00e401d2", "0.10.7--pyh5e36f6f_0": "sha256:54fc2ba1267c338a7450d7dc195fde19a2a7d061f209833aaed3c79431ce2a82", "0.10.8--pyh7cba7a3_0": "sha256:4da1f8be8965e0f4f5d28d982ea0875fd22d24fb1efdeae0fa8f53962b3b202d"}, "docker": "quay.io/biocontainers/ephemeris", "aliases": {"bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "galaxy-tool-test": "/usr/local/bin/galaxy-tool-test", "galaxy-wait": "/usr/local/bin/galaxy-wait", "get-tool-list": "/usr/local/bin/get-tool-list", "mulled-build": "/usr/local/bin/mulled-build", "mulled-build-channel": "/usr/local/bin/mulled-build-channel", "mulled-build-files": "/usr/local/bin/mulled-build-files", "mulled-build-tool": "/usr/local/bin/mulled-build-tool", "mulled-search": "/usr/local/bin/mulled-search", "run-data-managers": "/usr/local/bin/run-data-managers", "setup-data-libraries": "/usr/local/bin/setup-data-libraries", "shed-tools": "/usr/local/bin/shed-tools", "workflow-install": "/usr/local/bin/workflow-install", "workflow-to-tools": "/usr/local/bin/workflow-to-tools", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ephemeris.
shpc-registry automated BioContainers addition for ephemeris
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ephemeris
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ephemeris:0.10.8--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ephemeris/0.10.8--pyh7cba7a3_0
$ module help quay.io/biocontainers/ephemeris/0.10.8--pyh7cba7a3_0
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


#### galaxy-tool-test

```bash
$ singularity exec <container> /usr/local/bin/galaxy-tool-test
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mulled-build

```bash
$ singularity exec <container> /usr/local/bin/mulled-build
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-channel

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-channel
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-files

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-files
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-tool

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-tool
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-search

```bash
$ singularity exec <container> /usr/local/bin/mulled-search
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glacier

```bash
$ singularity exec <container> /usr/local/bin/glacier
$ podman run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
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