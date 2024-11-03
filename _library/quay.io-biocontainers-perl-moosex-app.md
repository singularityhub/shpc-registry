---
layout: container
name:  "quay.io/biocontainers/perl-moosex-app"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-moosex-app/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-moosex-app/container.yaml"
updated_at: "2024-11-03 03:04:59.894236"
latest: "1.3701--pl526_2"
container_url: "https://biocontainers.pro/tools/perl-moosex-app"

versions:
 - "1.42--pl5321hdfd78af_0"
 - "1.3701--pl526_2"
description: "shpc-registry automated BioContainers addition for perl-moosex-app"
config: {"url": "https://biocontainers.pro/tools/perl-moosex-app", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-moosex-app", "latest": {"1.3701--pl526_2": "sha256:3c4609ec6dbe72538b6a6f66efbc1f1631770f0b5a2142f9cce52d34fbe811d3"}, "tags": {"1.42--pl5321hdfd78af_0": "sha256:401759371036b24bf55e455a8e52ff45e261baddab52c7105a91c66af949984b", "1.3701--pl526_2": "sha256:3c4609ec6dbe72538b6a6f66efbc1f1631770f0b5a2142f9cce52d34fbe811d3"}, "docker": "quay.io/biocontainers/perl-moosex-app"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-moosex-app.
shpc-registry automated BioContainers addition for perl-moosex-app
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-moosex-app
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-moosex-app:1.3701--pl526_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-moosex-app/1.3701--pl526_2
$ module help quay.io/biocontainers/perl-moosex-app/1.3701--pl526_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-moosex-app-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-app-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-app-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-moosex-app-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-moosex-app-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-moosex-app-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-moosex-app

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