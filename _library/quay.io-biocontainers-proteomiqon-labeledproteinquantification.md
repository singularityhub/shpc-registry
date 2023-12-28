---
layout: container
name:  "quay.io/biocontainers/proteomiqon-labeledproteinquantification"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-labeledproteinquantification/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-labeledproteinquantification/container.yaml"
updated_at: "2023-12-28 02:58:18.218031"
latest: "0.0.3--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/proteomiqon-labeledproteinquantification"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-labeledproteinquantification"
versions:
 - "0.0.1--hdfd78af_1"
 - "0.0.3--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for proteomiqon-labeledproteinquantification"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-labeledproteinquantification", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-labeledproteinquantification", "latest": {"0.0.3--hdfd78af_1": "sha256:3381039790c9e6fe82b29bb853c1de650e3516c1ec1315c2a8828b4096fc0197"}, "tags": {"0.0.1--hdfd78af_1": "sha256:d9b2943db457eb9d13d1673742821ed9ca04647e79acf005025d7c6aa80be539", "0.0.3--hdfd78af_1": "sha256:3381039790c9e6fe82b29bb853c1de650e3516c1ec1315c2a8828b4096fc0197"}, "docker": "quay.io/biocontainers/proteomiqon-labeledproteinquantification", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-labeledproteinquantification": "/usr/local/bin/proteomiqon-labeledproteinquantification"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-labeledproteinquantification.
shpc-registry automated BioContainers addition for proteomiqon-labeledproteinquantification
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-labeledproteinquantification
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-labeledproteinquantification:0.0.3--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-labeledproteinquantification/0.0.3--hdfd78af_1
$ module help quay.io/biocontainers/proteomiqon-labeledproteinquantification/0.0.3--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-labeledproteinquantification-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-labeledproteinquantification-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-labeledproteinquantification-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-labeledproteinquantification-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-labeledproteinquantification-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-labeledproteinquantification-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-labeledproteinquantification

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-labeledproteinquantification
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-labeledproteinquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-labeledproteinquantification   -v ${PWD} -w ${PWD} <container> -c " $@"
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