---
layout: container
name:  "quay.io/biocontainers/r-biodb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-biodb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-biodb/container.yaml"
updated_at: "2024-11-15 02:25:56.557947"
latest: "1.2.2--r43h4ac6f70_9"
container_url: "https://biocontainers.pro/tools/r-biodb"

versions:
 - "1.2.2--r41h9f5acd7_4"
 - "1.2.2--r42h9f5acd7_5"
 - "1.2.2--r42h4ac6f70_7"
 - "1.2.2--r43h4ac6f70_8"
 - "1.2.2--r43h4ac6f70_9"
description: "shpc-registry automated BioContainers addition for r-biodb"
config: {"url": "https://biocontainers.pro/tools/r-biodb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-biodb", "latest": {"1.2.2--r43h4ac6f70_9": "sha256:1cfcab01adb9e8ca22987175fd5136eb2b727c44a10f7625bff392f7743de12d"}, "tags": {"1.2.2--r41h9f5acd7_4": "sha256:9394e9103a7e7c0ae08468d52bc782c888493609a115eacb827bd29a6f6337f7", "1.2.2--r42h9f5acd7_5": "sha256:a32b53a855ca20e028ffae798cc3b2d1823221779c94a8674156deb89a673f87", "1.2.2--r42h4ac6f70_7": "sha256:cf016ebb32b9a6d52160eaaa468e712849b195fbc13498c164aa66fe0864f4a0", "1.2.2--r43h4ac6f70_8": "sha256:3e936fc1a72dd7695e8bb1e4a43e81b94ec4615190741666428267f4de2135d7", "1.2.2--r43h4ac6f70_9": "sha256:1cfcab01adb9e8ca22987175fd5136eb2b727c44a10f7625bff392f7743de12d"}, "docker": "quay.io/biocontainers/r-biodb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-biodb.
shpc-registry automated BioContainers addition for r-biodb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-biodb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-biodb:1.2.2--r43h4ac6f70_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-biodb/1.2.2--r43h4ac6f70_9
$ module help quay.io/biocontainers/r-biodb/1.2.2--r43h4ac6f70_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-biodb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-biodb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-biodb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-biodb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-biodb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-biodb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-biodb

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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