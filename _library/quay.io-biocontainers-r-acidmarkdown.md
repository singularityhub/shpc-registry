---
layout: container
name:  "quay.io/biocontainers/r-acidmarkdown"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidmarkdown/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidmarkdown/container.yaml"
updated_at: "2024-01-19 03:03:44.134397"
latest: "0.3.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidmarkdown"

versions:
 - "0.1.6--r41hdfd78af_0"
 - "0.2.5--r42hdfd78af_0"
 - "0.1.6--r42hdfd78af_1"
 - "0.2.5--r42hdfd78af_1"
 - "0.2.5--r43hdfd78af_2"
 - "0.2.6--r43hdfd78af_0"
 - "0.3.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidmarkdown"
config: {"url": "https://biocontainers.pro/tools/r-acidmarkdown", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidmarkdown", "latest": {"0.3.0--r43hdfd78af_0": "sha256:9f5b93b40c09560bf802db64039c83a97b8f5a884db4bf76df971bda7536beea"}, "tags": {"0.1.6--r41hdfd78af_0": "sha256:a7edbdc9be1f818ec92106cac309a6119de65fa0ff7c06e725a969eecdce043a", "0.2.5--r42hdfd78af_0": "sha256:19bc880273d27f37932f70c9d55a4224b9d948ced3d063ad549baaaea95d91e1", "0.1.6--r42hdfd78af_1": "sha256:70d982865584d6722aa58f54622f550c31eea31ffe136819c42dcece6af67fff", "0.2.5--r42hdfd78af_1": "sha256:a7ea1e1c54497cdd8fc79724ae77f535f37bca715be800ba9b8f52aae4e71a55", "0.2.5--r43hdfd78af_2": "sha256:e3405c7b2bc9c78172c68b067ae8d1860867cba14f8738f58d9ba24f4b05b2fb", "0.2.6--r43hdfd78af_0": "sha256:ecdde3e4939d5e3abf3cdded41f60136ad46330785ef9b51d71a6cf4f080c852", "0.3.0--r43hdfd78af_0": "sha256:9f5b93b40c09560bf802db64039c83a97b8f5a884db4bf76df971bda7536beea"}, "docker": "quay.io/biocontainers/r-acidmarkdown"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidmarkdown.
shpc-registry automated BioContainers addition for r-acidmarkdown
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidmarkdown
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidmarkdown:0.3.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidmarkdown/0.3.0--r43hdfd78af_0
$ module help quay.io/biocontainers/r-acidmarkdown/0.3.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidmarkdown-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidmarkdown-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidmarkdown-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidmarkdown-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidmarkdown-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidmarkdown-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidmarkdown

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