---
layout: container
name:  "quay.io/biocontainers/tbox-scan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tbox-scan/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tbox-scan/container.yaml"
updated_at: "2022-10-27 00:32:52.655787"
latest: "1.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/tbox-scan"
aliases:
 - "tbox-scan"
versions:
 - "1.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for tbox-scan"
config: {"url": "https://biocontainers.pro/tools/tbox-scan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tbox-scan", "latest": {"1.0.2--hdfd78af_1": "sha256:364b8ebbc21dea4338e7aacab9bd31e356408eece5be275972f3b9576d79712c"}, "tags": {"1.0.2--hdfd78af_1": "sha256:364b8ebbc21dea4338e7aacab9bd31e356408eece5be275972f3b9576d79712c"}, "docker": "quay.io/biocontainers/tbox-scan", "aliases": {"tbox-scan": "/usr/local/bin/tbox-scan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tbox-scan.
shpc-registry automated BioContainers addition for tbox-scan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tbox-scan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tbox-scan:1.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tbox-scan/1.0.2--hdfd78af_1
$ module help quay.io/biocontainers/tbox-scan/1.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tbox-scan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tbox-scan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tbox-scan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tbox-scan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tbox-scan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tbox-scan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tbox-scan

```bash
$ singularity exec <container> /usr/local/bin/tbox-scan
$ podman run --it --rm --entrypoint /usr/local/bin/tbox-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbox-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
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