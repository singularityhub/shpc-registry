---
layout: container
name:  "quay.io/biocontainers/perl-test-file"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-test-file/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-test-file/container.yaml"
updated_at: "2023-12-02 02:42:14.309961"
latest: "1.993--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-test-file"

versions:
 - "1.992--pl5321hdfd78af_0"
 - "1.993--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-test-file"
config: {"url": "https://biocontainers.pro/tools/perl-test-file", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-test-file", "latest": {"1.993--pl5321hdfd78af_0": "sha256:1c9329a36819751dfd48a4a0e9b6b3bcf5a402d4a56edcdc2a3f1a84605e58aa"}, "tags": {"1.992--pl5321hdfd78af_0": "sha256:aaaf6ef4e1247ca8df429135a8fbacd68e623c8330d60b5379aa0dfc88b3283d", "1.993--pl5321hdfd78af_0": "sha256:1c9329a36819751dfd48a4a0e9b6b3bcf5a402d4a56edcdc2a3f1a84605e58aa"}, "docker": "quay.io/biocontainers/perl-test-file"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-test-file.
shpc-registry automated BioContainers addition for perl-test-file
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-test-file
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-test-file:1.993--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-test-file/1.993--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-test-file/1.993--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-test-file-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-test-file-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-test-file-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-test-file-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-test-file-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-test-file-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-test-file

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