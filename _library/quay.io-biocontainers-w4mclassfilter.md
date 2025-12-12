---
layout: container
name:  "quay.io/biocontainers/w4mclassfilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/w4mclassfilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/w4mclassfilter/container.yaml"
updated_at: "2025-12-12 04:11:17.429139"
latest: "0.98.19--r42hdfd78af_3"
container_url: "https://biocontainers.pro/tools/w4mclassfilter"

versions:
 - "0.98.9--r351_0"
 - "0.98.19--r40hdfd78af_1"
 - "0.98.19--r42hdfd78af_3"
description: "shpc-registry automated BioContainers addition for w4mclassfilter"
config: {"url": "https://biocontainers.pro/tools/w4mclassfilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for w4mclassfilter", "latest": {"0.98.19--r42hdfd78af_3": "sha256:e17c09bc6646efcbab5da7b9bf9f216839bee218e91892dff36ea14f8a49caa8"}, "tags": {"0.98.9--r351_0": "sha256:4544d0ad3cfd578b6ba2894d06964de77b141c2fbd2bb79203fee1706d364ad9", "0.98.19--r40hdfd78af_1": "sha256:4d0b344a53ef50e7f86c8aa83b62be7005892dea3ba502cdba1a284bd410229f", "0.98.19--r42hdfd78af_3": "sha256:e17c09bc6646efcbab5da7b9bf9f216839bee218e91892dff36ea14f8a49caa8"}, "docker": "quay.io/biocontainers/w4mclassfilter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/w4mclassfilter.
shpc-registry automated BioContainers addition for w4mclassfilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/w4mclassfilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/w4mclassfilter:0.98.19--r42hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/w4mclassfilter/0.98.19--r42hdfd78af_3
$ module help quay.io/biocontainers/w4mclassfilter/0.98.19--r42hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### w4mclassfilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### w4mclassfilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### w4mclassfilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### w4mclassfilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### w4mclassfilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### w4mclassfilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### w4mclassfilter

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