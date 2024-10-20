---
layout: container
name:  "quay.io/biocontainers/tidehunter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tidehunter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tidehunter/container.yaml"
updated_at: "2024-10-20 03:21:58.484268"
latest: "1.5.5--h43eeafb_2"
container_url: "https://biocontainers.pro/tools/tidehunter"
aliases:
 - "TideHunter"
versions:
 - "1.5.3--h5b5514e_1"
 - "1.5.4--h5b5514e_1"
 - "1.5.4--h43eeafb_2"
 - "1.5.5--h43eeafb_2"
description: "shpc-registry automated BioContainers addition for tidehunter"
config: {"url": "https://biocontainers.pro/tools/tidehunter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tidehunter", "latest": {"1.5.5--h43eeafb_2": "sha256:255e741b889053c919e863bc0528eccc5a535f45e91b121e635827211ef48114"}, "tags": {"1.5.3--h5b5514e_1": "sha256:31584417a87d80a58d58623648ad5ae8f9c383769fbc92e8a2c4a503d85754a4", "1.5.4--h5b5514e_1": "sha256:1f9928318d48d21ab70dc89dad4c6c5a92367f5574b46bd7a9361e3e2519119e", "1.5.4--h43eeafb_2": "sha256:40284799af7cc88d4a03acfc5a6fda67e483ba40a432c1357f4e187674600013", "1.5.5--h43eeafb_2": "sha256:255e741b889053c919e863bc0528eccc5a535f45e91b121e635827211ef48114"}, "docker": "quay.io/biocontainers/tidehunter", "aliases": {"TideHunter": "/usr/local/bin/TideHunter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tidehunter.
shpc-registry automated BioContainers addition for tidehunter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tidehunter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tidehunter:1.5.5--h43eeafb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tidehunter/1.5.5--h43eeafb_2
$ module help quay.io/biocontainers/tidehunter/1.5.5--h43eeafb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tidehunter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tidehunter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tidehunter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tidehunter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tidehunter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tidehunter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TideHunter

```bash
$ singularity exec <container> /usr/local/bin/TideHunter
$ podman run --it --rm --entrypoint /usr/local/bin/TideHunter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TideHunter   -v ${PWD} -w ${PWD} <container> -c " $@"
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