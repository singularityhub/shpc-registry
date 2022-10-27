---
layout: container
name:  "quay.io/biocontainers/jolytree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jolytree/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/jolytree/container.yaml"
updated_at: "2022-10-27 00:18:54.593976"
latest: "1.1b--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/jolytree"
aliases:
 - "JolyTree.sh"
 - "REQ"
versions:
 - "1.1b--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for jolytree"
config: {"url": "https://biocontainers.pro/tools/jolytree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jolytree", "latest": {"1.1b--hdfd78af_1": "sha256:9b88f1e6a6f4e2750946c88ae752f37b646eb7caf5c793298ac1b696d46df5d8"}, "tags": {"1.1b--hdfd78af_1": "sha256:9b88f1e6a6f4e2750946c88ae752f37b646eb7caf5c793298ac1b696d46df5d8"}, "docker": "quay.io/biocontainers/jolytree", "aliases": {"JolyTree.sh": "/usr/local/bin/JolyTree.sh", "REQ": "/usr/local/bin/REQ"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jolytree.
shpc-registry automated BioContainers addition for jolytree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jolytree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jolytree:1.1b--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jolytree/1.1b--hdfd78af_1
$ module help quay.io/biocontainers/jolytree/1.1b--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jolytree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jolytree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jolytree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jolytree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jolytree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jolytree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### JolyTree.sh

```bash
$ singularity exec <container> /usr/local/bin/JolyTree.sh
$ podman run --it --rm --entrypoint /usr/local/bin/JolyTree.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JolyTree.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REQ

```bash
$ singularity exec <container> /usr/local/bin/REQ
$ podman run --it --rm --entrypoint /usr/local/bin/REQ   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REQ   -v ${PWD} -w ${PWD} <container> -c " $@"
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