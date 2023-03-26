---
layout: container
name:  "quay.io/biocontainers/perl-http-daemon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-http-daemon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-http-daemon/container.yaml"
updated_at: "2023-03-26 03:18:49.426173"
latest: "6.15--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-http-daemon"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "6.14--pl5321hdfd78af_0"
 - "6.15--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-http-daemon"
config: {"url": "https://biocontainers.pro/tools/perl-http-daemon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-http-daemon", "latest": {"6.15--pl5321hdfd78af_0": "sha256:1f5a2c62f264fc53c9777b86a435c4bb0e30428034a02b8b487fecf420c25faf"}, "tags": {"6.14--pl5321hdfd78af_0": "sha256:ee79adb1b2dd319cb5e14c6a91253e5ea28b7e6385f23fc3464b2722e84c4183", "6.15--pl5321hdfd78af_0": "sha256:1f5a2c62f264fc53c9777b86a435c4bb0e30428034a02b8b487fecf420c25faf"}, "docker": "quay.io/biocontainers/perl-http-daemon", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-http-daemon.
shpc-registry automated BioContainers addition for perl-http-daemon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-http-daemon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-http-daemon:6.15--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-http-daemon/6.15--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-http-daemon/6.15--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-http-daemon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-http-daemon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-http-daemon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-http-daemon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-http-daemon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-http-daemon-inspect-deffile:

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