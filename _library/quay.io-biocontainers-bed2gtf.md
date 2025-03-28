---
layout: container
name:  "quay.io/biocontainers/bed2gtf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bed2gtf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bed2gtf/container.yaml"
updated_at: "2025-03-28 03:46:20.873024"
latest: "1.9.3--h9948957_2"
container_url: "https://biocontainers.pro/tools/bed2gtf"
aliases:
 - "bed2gtf"
versions:
 - "1.9.0--h4ac6f70_0"
 - "1.9.1--h4ac6f70_0"
 - "1.9.2--h4ac6f70_0"
 - "1.9.3--h4ac6f70_1"
 - "1.9.3--h9948957_2"
description: "singularity registry hpc automated addition for bed2gtf"
config: {"url": "https://biocontainers.pro/tools/bed2gtf", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bed2gtf", "latest": {"1.9.3--h9948957_2": "sha256:dc1615cb73fca82db7f65e9d1441e0875a412996ad97cb56ec264ced805dee17"}, "tags": {"1.9.0--h4ac6f70_0": "sha256:32ffd1516d1fc28bb763366e2f428c0708cfa6b26c117aa9d22170babfd92fbd", "1.9.1--h4ac6f70_0": "sha256:c2f4594e68bc2c493a7ceca7701e676a890db6f275e692a6d65f07be3503ba67", "1.9.2--h4ac6f70_0": "sha256:73fdd4dc638f666542f78ec0dcf04bcc3a80b04ec0ffad2e3afe258d3139793e", "1.9.3--h4ac6f70_1": "sha256:b6dedb2465f42f7da7097abf073c739925a241f74d23467d99f582629191826b", "1.9.3--h9948957_2": "sha256:dc1615cb73fca82db7f65e9d1441e0875a412996ad97cb56ec264ced805dee17"}, "docker": "quay.io/biocontainers/bed2gtf", "aliases": {"bed2gtf": "/usr/local/bin/bed2gtf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bed2gtf.
singularity registry hpc automated addition for bed2gtf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bed2gtf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bed2gtf:1.9.3--h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bed2gtf/1.9.3--h9948957_2
$ module help quay.io/biocontainers/bed2gtf/1.9.3--h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bed2gtf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bed2gtf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bed2gtf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bed2gtf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bed2gtf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bed2gtf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bed2gtf

```bash
$ singularity exec <container> /usr/local/bin/bed2gtf
$ podman run --it --rm --entrypoint /usr/local/bin/bed2gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
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