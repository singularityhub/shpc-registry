---
layout: container
name:  "quay.io/biocontainers/seqcomplexity"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqcomplexity/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqcomplexity/container.yaml"
updated_at: "2024-02-20 02:25:23.953258"
latest: "0.1.2--he9f29cb_0"
container_url: "https://biocontainers.pro/tools/seqcomplexity"
aliases:
 - "seqcomplexity"
versions:
 - "0.1.2--he9f29cb_0"
 - "0.1.2"
description: "singularity registry hpc automated addition for seqcomplexity"
config: {"url": "https://biocontainers.pro/tools/seqcomplexity", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seqcomplexity", "latest": {"0.1.2--he9f29cb_0": "sha256:acecac06c0b33fcfa38b9053dc19f217e88f939f0499d4e9e88515447c496d20"}, "tags": {"0.1.2--he9f29cb_0": "sha256:acecac06c0b33fcfa38b9053dc19f217e88f939f0499d4e9e88515447c496d20", "0.1.2": "sha256:e04769b948f69a299573f3d793df950bbc44da54789db89db6b559ccce440d69"}, "docker": "quay.io/biocontainers/seqcomplexity", "aliases": {"seqcomplexity": "/usr/local/bin/seqcomplexity"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqcomplexity.
singularity registry hpc automated addition for seqcomplexity
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqcomplexity
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqcomplexity:0.1.2--he9f29cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqcomplexity/0.1.2--he9f29cb_0
$ module help quay.io/biocontainers/seqcomplexity/0.1.2--he9f29cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqcomplexity-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqcomplexity-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqcomplexity-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqcomplexity-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqcomplexity-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqcomplexity-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqcomplexity

```bash
$ singularity exec <container> /usr/local/bin/seqcomplexity
$ podman run --it --rm --entrypoint /usr/local/bin/seqcomplexity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqcomplexity   -v ${PWD} -w ${PWD} <container> -c " $@"
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