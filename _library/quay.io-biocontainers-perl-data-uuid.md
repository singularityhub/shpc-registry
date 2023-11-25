---
layout: container
name:  "quay.io/biocontainers/perl-data-uuid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-data-uuid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-data-uuid/container.yaml"
updated_at: "2023-11-25 02:47:36.423422"
latest: "1.226--pl5321h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/perl-data-uuid"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.226--pl5321h9f5acd7_1"
 - "1.226--pl5321h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for perl-data-uuid"
config: {"url": "https://biocontainers.pro/tools/perl-data-uuid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-data-uuid", "latest": {"1.226--pl5321h4ac6f70_3": "sha256:04eb2de23ef92e6b3dcc138bc8b851becd6950bba73ea68acd8aa80f1ca991e9"}, "tags": {"1.226--pl5321h9f5acd7_1": "sha256:2c982bcbdda65deeb9b521818babb613cedf20939d318c4731e4adbaeced7c29", "1.226--pl5321h4ac6f70_3": "sha256:04eb2de23ef92e6b3dcc138bc8b851becd6950bba73ea68acd8aa80f1ca991e9"}, "docker": "quay.io/biocontainers/perl-data-uuid", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-data-uuid.
shpc-registry automated BioContainers addition for perl-data-uuid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-data-uuid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-data-uuid:1.226--pl5321h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-data-uuid/1.226--pl5321h4ac6f70_3
$ module help quay.io/biocontainers/perl-data-uuid/1.226--pl5321h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-data-uuid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-data-uuid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-data-uuid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-data-uuid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-data-uuid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-data-uuid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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