---
layout: container
name:  "quay.io/biocontainers/pb-cpg-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pb-cpg-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pb-cpg-tools/container.yaml"
updated_at: "2025-11-07 04:06:32.498345"
latest: "3.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pb-cpg-tools"
aliases:
 - "aligned_bam_to_cpg_scores"
versions:
 - "3.0.0--h9ee0642_0"
description: "singularity registry hpc automated addition for pb-cpg-tools"
config: {"url": "https://biocontainers.pro/tools/pb-cpg-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pb-cpg-tools", "latest": {"3.0.0--h9ee0642_0": "sha256:c7d4f999b747e4d5c356669086b929e6eda34249d3e8752ede100cb45faaefb4"}, "tags": {"3.0.0--h9ee0642_0": "sha256:c7d4f999b747e4d5c356669086b929e6eda34249d3e8752ede100cb45faaefb4"}, "docker": "quay.io/biocontainers/pb-cpg-tools", "aliases": {"aligned_bam_to_cpg_scores": "/usr/local/bin/aligned_bam_to_cpg_scores"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pb-cpg-tools.
singularity registry hpc automated addition for pb-cpg-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pb-cpg-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pb-cpg-tools:3.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pb-cpg-tools/3.0.0--h9ee0642_0
$ module help quay.io/biocontainers/pb-cpg-tools/3.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pb-cpg-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pb-cpg-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pb-cpg-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pb-cpg-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pb-cpg-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pb-cpg-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aligned_bam_to_cpg_scores

```bash
$ singularity exec <container> /usr/local/bin/aligned_bam_to_cpg_scores
$ podman run --it --rm --entrypoint /usr/local/bin/aligned_bam_to_cpg_scores   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aligned_bam_to_cpg_scores   -v ${PWD} -w ${PWD} <container> -c " $@"
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