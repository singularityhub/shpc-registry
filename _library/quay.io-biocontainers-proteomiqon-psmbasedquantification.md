---
layout: container
name:  "quay.io/biocontainers/proteomiqon-psmbasedquantification"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-psmbasedquantification/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-psmbasedquantification/container.yaml"
updated_at: "2023-10-05 03:28:59.281869"
latest: "0.0.9--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/proteomiqon-psmbasedquantification"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-psmbasedquantification"
versions:
 - "0.0.8--hdfd78af_0"
 - "0.0.9--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for proteomiqon-psmbasedquantification"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-psmbasedquantification", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-psmbasedquantification", "latest": {"0.0.9--hdfd78af_0": "sha256:58238f0706e842a9bac4f718d7e2690a230534768752d471aee8fd9828faeb6f"}, "tags": {"0.0.8--hdfd78af_0": "sha256:2f21ad635d6e79e65dbbe5263a628ce51bf931d0b5bb504a483e0919278fe67b", "0.0.9--hdfd78af_0": "sha256:58238f0706e842a9bac4f718d7e2690a230534768752d471aee8fd9828faeb6f"}, "docker": "quay.io/biocontainers/proteomiqon-psmbasedquantification", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-psmbasedquantification": "/usr/local/bin/proteomiqon-psmbasedquantification"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-psmbasedquantification.
shpc-registry automated BioContainers addition for proteomiqon-psmbasedquantification
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-psmbasedquantification
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-psmbasedquantification:0.0.9--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-psmbasedquantification/0.0.9--hdfd78af_0
$ module help quay.io/biocontainers/proteomiqon-psmbasedquantification/0.0.9--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-psmbasedquantification-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-psmbasedquantification-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-psmbasedquantification-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-psmbasedquantification-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-psmbasedquantification-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-psmbasedquantification-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-psmbasedquantification

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-psmbasedquantification
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-psmbasedquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-psmbasedquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
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