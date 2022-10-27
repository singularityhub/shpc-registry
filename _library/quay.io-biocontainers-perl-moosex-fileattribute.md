---
layout: container
name:  "quay.io/biocontainers/perl-moosex-fileattribute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-moosex-fileattribute/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-moosex-fileattribute/container.yaml"
updated_at: "2022-10-27 00:42:46.271406"
latest: "0.03--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-moosex-fileattribute"

versions:
 - "0.03--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-moosex-fileattribute"
config: {"url": "https://biocontainers.pro/tools/perl-moosex-fileattribute", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-moosex-fileattribute", "latest": {"0.03--pl5321hdfd78af_1": "sha256:f9981f94e01004d65eea4614ac905dcc26e5ffa47b14cdf147995cc3dea82522"}, "tags": {"0.03--pl5321hdfd78af_1": "sha256:f9981f94e01004d65eea4614ac905dcc26e5ffa47b14cdf147995cc3dea82522"}, "docker": "quay.io/biocontainers/perl-moosex-fileattribute"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-moosex-fileattribute.
shpc-registry automated BioContainers addition for perl-moosex-fileattribute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-moosex-fileattribute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-moosex-fileattribute:0.03--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-moosex-fileattribute/0.03--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-moosex-fileattribute/0.03--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-moosex-fileattribute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-fileattribute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-fileattribute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-moosex-fileattribute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-moosex-fileattribute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-moosex-fileattribute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-moosex-fileattribute

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