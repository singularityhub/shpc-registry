---
layout: container
name:  "quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins/container.yaml"
updated_at: "2025-08-04 04:26:57.369233"
latest: "0.0.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/proteomiqon-joinquantpepionswithproteins"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-joinquantpepionswithproteins"
versions:
 - "0.0.1--hdfd78af_1"
 - "0.0.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for proteomiqon-joinquantpepionswithproteins"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-joinquantpepionswithproteins", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-joinquantpepionswithproteins", "latest": {"0.0.2--hdfd78af_1": "sha256:ca57e95b0d02065521215cfb307c596430dfb8438996916247292cfbcf5ee2f9"}, "tags": {"0.0.1--hdfd78af_1": "sha256:ab87dbd5b9e39b2f378c6ae456b39a9e293c8fdfb1d47b26cc2d35aa6003f1d2", "0.0.2--hdfd78af_1": "sha256:ca57e95b0d02065521215cfb307c596430dfb8438996916247292cfbcf5ee2f9"}, "docker": "quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-joinquantpepionswithproteins": "/usr/local/bin/proteomiqon-joinquantpepionswithproteins"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins.
shpc-registry automated BioContainers addition for proteomiqon-joinquantpepionswithproteins
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins:0.0.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins/0.0.2--hdfd78af_1
$ module help quay.io/biocontainers/proteomiqon-joinquantpepionswithproteins/0.0.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-joinquantpepionswithproteins-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-joinquantpepionswithproteins-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-joinquantpepionswithproteins-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-joinquantpepionswithproteins-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-joinquantpepionswithproteins-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-joinquantpepionswithproteins-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-joinquantpepionswithproteins

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-joinquantpepionswithproteins
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-joinquantpepionswithproteins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-joinquantpepionswithproteins   -v ${PWD} -w ${PWD} <container> -c " $@"
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