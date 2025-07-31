---
layout: container
name:  "quay.io/biocontainers/dnp-diprofile"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnp-diprofile/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnp-diprofile/container.yaml"
updated_at: "2025-07-31 11:45:17.100123"
latest: "1.0--hd6d6fdc_7"
container_url: "https://biocontainers.pro/tools/dnp-diprofile"
aliases:
 - "dnp-diprofile"
versions:
 - "1.0--hf1761c0_4"
 - "1.0--h6a68c12_6"
 - "1.0--hd6d6fdc_7"
description: "shpc-registry automated BioContainers addition for dnp-diprofile"
config: {"url": "https://biocontainers.pro/tools/dnp-diprofile", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnp-diprofile", "latest": {"1.0--hd6d6fdc_7": "sha256:10431d7b95ac2fbdf6dac7035511c6bd9227d31051c1ad0fd1bd6c01264b4e3f"}, "tags": {"1.0--hf1761c0_4": "sha256:e4001a753e2fa9eac53e20e98a4c3c486271a2ffcae7f1ec629ddbeff6b89386", "1.0--h6a68c12_6": "sha256:1d93362e2e79e586c3df34f5f6ca0a52890812694823132a57b199548e3b1339", "1.0--hd6d6fdc_7": "sha256:10431d7b95ac2fbdf6dac7035511c6bd9227d31051c1ad0fd1bd6c01264b4e3f"}, "docker": "quay.io/biocontainers/dnp-diprofile", "aliases": {"dnp-diprofile": "/usr/local/bin/dnp-diprofile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnp-diprofile.
shpc-registry automated BioContainers addition for dnp-diprofile
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnp-diprofile
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnp-diprofile:1.0--hd6d6fdc_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnp-diprofile/1.0--hd6d6fdc_7
$ module help quay.io/biocontainers/dnp-diprofile/1.0--hd6d6fdc_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnp-diprofile-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnp-diprofile-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnp-diprofile-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnp-diprofile-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnp-diprofile-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnp-diprofile-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnp-diprofile

```bash
$ singularity exec <container> /usr/local/bin/dnp-diprofile
$ podman run --it --rm --entrypoint /usr/local/bin/dnp-diprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnp-diprofile   -v ${PWD} -w ${PWD} <container> -c " $@"
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