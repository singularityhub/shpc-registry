---
layout: container
name:  "quay.io/biocontainers/r-workflowscriptscommon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-workflowscriptscommon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-workflowscriptscommon/container.yaml"
updated_at: "2023-08-06 03:08:07.696892"
latest: "0.0.8--r41hdfd78af_4"
container_url: "https://biocontainers.pro/tools/r-workflowscriptscommon"

versions:
 - "0.0.8--r40hdfd78af_1"
 - "0.0.8--r41hdfd78af_2"
 - "0.0.8--r41hdfd78af_3"
 - "0.0.8--r41hdfd78af_4"
description: "shpc-registry automated BioContainers addition for r-workflowscriptscommon"
config: {"url": "https://biocontainers.pro/tools/r-workflowscriptscommon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-workflowscriptscommon", "latest": {"0.0.8--r41hdfd78af_4": "sha256:1fff5e9c605b5878e70511ed386b035e8b676e81217cdb92ed6ffc051393dce7"}, "tags": {"0.0.8--r40hdfd78af_1": "sha256:a19006b0836a2870b1657441e06d9481f278bb8bcc961a3031f76f0c7fef130a", "0.0.8--r41hdfd78af_2": "sha256:9dbca7fcdb0568d0bfa11cbd109177a06a2566735493c5cbbc9d118100b6b20e", "0.0.8--r41hdfd78af_3": "sha256:276583635ecd8275390a5f063cba913d56cc0f02c30f1b2b1e0e76370470bb01", "0.0.8--r41hdfd78af_4": "sha256:1fff5e9c605b5878e70511ed386b035e8b676e81217cdb92ed6ffc051393dce7"}, "docker": "quay.io/biocontainers/r-workflowscriptscommon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-workflowscriptscommon.
shpc-registry automated BioContainers addition for r-workflowscriptscommon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-workflowscriptscommon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-workflowscriptscommon:0.0.8--r41hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-workflowscriptscommon/0.0.8--r41hdfd78af_4
$ module help quay.io/biocontainers/r-workflowscriptscommon/0.0.8--r41hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-workflowscriptscommon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-workflowscriptscommon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-workflowscriptscommon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-workflowscriptscommon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-workflowscriptscommon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-workflowscriptscommon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-workflowscriptscommon

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