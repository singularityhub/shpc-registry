---
layout: container
name:  "quay.io/biocontainers/bioconductor-rarr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rarr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rarr/container.yaml"
updated_at: "2024-01-05 02:39:18.922686"
latest: "1.2.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rarr"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hf17093f_0"
 - "1.2.0--r43hf17093f_0"
description: "singularity registry hpc automated addition for bioconductor-rarr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rarr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-rarr", "latest": {"1.2.0--r43hf17093f_0": "sha256:7602913bf1dd5ff6119d7bb45487aa01b475433cf7f097d28790e2447b2a5c10"}, "tags": {"1.0.0--r43hf17093f_0": "sha256:add263d330bf0983495202368585b3e4a3d57050cc266dc03e9c2acc009438d5", "1.2.0--r43hf17093f_0": "sha256:7602913bf1dd5ff6119d7bb45487aa01b475433cf7f097d28790e2447b2a5c10"}, "docker": "quay.io/biocontainers/bioconductor-rarr", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rarr.
singularity registry hpc automated addition for bioconductor-rarr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rarr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rarr:1.2.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rarr/1.2.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rarr/1.2.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rarr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rarr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rarr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rarr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rarr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rarr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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