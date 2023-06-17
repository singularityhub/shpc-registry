---
layout: container
name:  "quay.io/biocontainers/ngs-disambiguate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngs-disambiguate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngs-disambiguate/container.yaml"
updated_at: "2023-06-17 02:39:21.256244"
latest: "2018.05.03--hf393df8_7"
container_url: "https://biocontainers.pro/tools/ngs-disambiguate"
aliases:
 - "ngs_disambiguate"
 - "bamtools"
versions:
 - "2018.05.03--ha7703dc_6"
 - "2018.05.03--hf393df8_7"
description: "shpc-registry automated BioContainers addition for ngs-disambiguate"
config: {"url": "https://biocontainers.pro/tools/ngs-disambiguate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngs-disambiguate", "latest": {"2018.05.03--hf393df8_7": "sha256:a86e59107e0f758435d2fd9d1fc81eeed7fa7c2dd66401fcafb400e52736dea7"}, "tags": {"2018.05.03--ha7703dc_6": "sha256:8695e9f3bb10a56736234c0ec3c83da6249575cdbdbbe1160857c212c27ab657", "2018.05.03--hf393df8_7": "sha256:a86e59107e0f758435d2fd9d1fc81eeed7fa7c2dd66401fcafb400e52736dea7"}, "docker": "quay.io/biocontainers/ngs-disambiguate", "aliases": {"ngs_disambiguate": "/usr/local/bin/ngs_disambiguate", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngs-disambiguate.
shpc-registry automated BioContainers addition for ngs-disambiguate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngs-disambiguate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngs-disambiguate:2018.05.03--hf393df8_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngs-disambiguate/2018.05.03--hf393df8_7
$ module help quay.io/biocontainers/ngs-disambiguate/2018.05.03--hf393df8_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngs-disambiguate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngs-disambiguate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngs-disambiguate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngs-disambiguate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngs-disambiguate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngs-disambiguate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngs_disambiguate

```bash
$ singularity exec <container> /usr/local/bin/ngs_disambiguate
$ podman run --it --rm --entrypoint /usr/local/bin/ngs_disambiguate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngs_disambiguate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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