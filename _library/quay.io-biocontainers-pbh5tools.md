---
layout: container
name:  "quay.io/biocontainers/pbh5tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbh5tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pbh5tools/container.yaml"
updated_at: "2022-10-27 00:57:04.715287"
latest: "0.8.0--py27h9801fc8_6"
container_url: "https://biocontainers.pro/tools/pbh5tools"
aliases:
 - ".open"
 - ".pbcore-post-link.sh"
 - "bash5tools.py"
 - "cmph5tools.py"
versions:
 - "0.8.0--py27h9801fc8_6"
description: "shpc-registry automated BioContainers addition for pbh5tools"
config: {"url": "https://biocontainers.pro/tools/pbh5tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbh5tools", "latest": {"0.8.0--py27h9801fc8_6": "sha256:6378fbf6e7b7986199f041902c30fd0fbe4afad110aec784b7175611ea629736"}, "tags": {"0.8.0--py27h9801fc8_6": "sha256:6378fbf6e7b7986199f041902c30fd0fbe4afad110aec784b7175611ea629736"}, "docker": "quay.io/biocontainers/pbh5tools", "aliases": {".open": "/usr/local/bin/.open", ".pbcore-post-link.sh": "/usr/local/bin/.pbcore-post-link.sh", "bash5tools.py": "/usr/local/bin/bash5tools.py", "cmph5tools.py": "/usr/local/bin/cmph5tools.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbh5tools.
shpc-registry automated BioContainers addition for pbh5tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbh5tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbh5tools:0.8.0--py27h9801fc8_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbh5tools/0.8.0--py27h9801fc8_6
$ module help quay.io/biocontainers/pbh5tools/0.8.0--py27h9801fc8_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbh5tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbh5tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbh5tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbh5tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbh5tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbh5tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .open

```bash
$ singularity exec <container> /usr/local/bin/.open
$ podman run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcore-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcore-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash5tools.py

```bash
$ singularity exec <container> /usr/local/bin/bash5tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/bash5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmph5tools.py

```bash
$ singularity exec <container> /usr/local/bin/cmph5tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/cmph5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmph5tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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