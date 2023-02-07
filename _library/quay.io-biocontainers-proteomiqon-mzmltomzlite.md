---
layout: container
name:  "quay.io/biocontainers/proteomiqon-mzmltomzlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-mzmltomzlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-mzmltomzlite/container.yaml"
updated_at: "2023-02-07 02:42:00.905171"
latest: "0.0.8--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/proteomiqon-mzmltomzlite"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-mzmltomzlite"
versions:
 - "0.0.8--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for proteomiqon-mzmltomzlite"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-mzmltomzlite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-mzmltomzlite", "latest": {"0.0.8--hdfd78af_0": "sha256:68b6ce8e185c253b5f5365fb5b6ca104bfc8a53bcd4055eb1e213622411bded5"}, "tags": {"0.0.8--hdfd78af_0": "sha256:68b6ce8e185c253b5f5365fb5b6ca104bfc8a53bcd4055eb1e213622411bded5"}, "docker": "quay.io/biocontainers/proteomiqon-mzmltomzlite", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-mzmltomzlite": "/usr/local/bin/proteomiqon-mzmltomzlite"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-mzmltomzlite.
shpc-registry automated BioContainers addition for proteomiqon-mzmltomzlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-mzmltomzlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-mzmltomzlite:0.0.8--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-mzmltomzlite/0.0.8--hdfd78af_0
$ module help quay.io/biocontainers/proteomiqon-mzmltomzlite/0.0.8--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-mzmltomzlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-mzmltomzlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-mzmltomzlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-mzmltomzlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-mzmltomzlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-mzmltomzlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-mzmltomzlite

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-mzmltomzlite
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-mzmltomzlite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-mzmltomzlite   -v ${PWD} -w ${PWD} <container> -c " $@"
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