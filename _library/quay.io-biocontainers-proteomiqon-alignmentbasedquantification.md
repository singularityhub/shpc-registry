---
layout: container
name:  "quay.io/biocontainers/proteomiqon-alignmentbasedquantification"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-alignmentbasedquantification/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-alignmentbasedquantification/container.yaml"
updated_at: "2024-07-30 02:38:28.364589"
latest: "0.0.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/proteomiqon-alignmentbasedquantification"
aliases:
 - "proteomiqon-alignmentbasedquantification"
 - "lttng-gen-tp"
versions:
 - "0.0.2--hdfd78af_0"
description: "singularity registry hpc automated addition for proteomiqon-alignmentbasedquantification"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-alignmentbasedquantification", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for proteomiqon-alignmentbasedquantification", "latest": {"0.0.2--hdfd78af_0": "sha256:41cd19739946b004d31ccab6fd867457b3a77facef5de9692f9b49467529f61c"}, "tags": {"0.0.2--hdfd78af_0": "sha256:41cd19739946b004d31ccab6fd867457b3a77facef5de9692f9b49467529f61c"}, "docker": "quay.io/biocontainers/proteomiqon-alignmentbasedquantification", "aliases": {"proteomiqon-alignmentbasedquantification": "/usr/local/bin/proteomiqon-alignmentbasedquantification", "lttng-gen-tp": "/usr/local/bin/lttng-gen-tp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-alignmentbasedquantification.
singularity registry hpc automated addition for proteomiqon-alignmentbasedquantification
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-alignmentbasedquantification
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-alignmentbasedquantification:0.0.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-alignmentbasedquantification/0.0.2--hdfd78af_0
$ module help quay.io/biocontainers/proteomiqon-alignmentbasedquantification/0.0.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-alignmentbasedquantification-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-alignmentbasedquantification-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-alignmentbasedquantification-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-alignmentbasedquantification-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-alignmentbasedquantification-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-alignmentbasedquantification-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proteomiqon-alignmentbasedquantification

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-alignmentbasedquantification
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-alignmentbasedquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-alignmentbasedquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
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