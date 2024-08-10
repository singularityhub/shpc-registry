---
layout: container
name:  "quay.io/biocontainers/tssar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tssar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tssar/container.yaml"
updated_at: "2024-08-10 02:53:27.314433"
latest: "1.0.1--r43h031d066_8"
container_url: "https://biocontainers.pro/tools/tssar"
aliases:
 - "TSSAR"
 - "TSSAR.bak"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.0.1--r41hec16e2b_4"
 - "1.0.1--r42hec16e2b_5"
 - "1.0.1--r42h031d066_7"
 - "1.0.1--r43h031d066_8"
description: "shpc-registry automated BioContainers addition for tssar"
config: {"url": "https://biocontainers.pro/tools/tssar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tssar", "latest": {"1.0.1--r43h031d066_8": "sha256:41254e9bbf607a9fe2b5832da6ec5980e8f70f588ca3d69cdd2eb216b4273a8e"}, "tags": {"1.0.1--r41hec16e2b_4": "sha256:57c20ce056beb17bae4200b20fd596885faf5674102e6d52fc429cc939dae191", "1.0.1--r42hec16e2b_5": "sha256:d21503a49ea1d486a43a3e4455a52aac1d6c71efb3aded30e7b045e8f68146e2", "1.0.1--r42h031d066_7": "sha256:643de6fe5484f7ba66b91ad3031b0ceed2fb3176e84e6d9bd1015e5f73fe7857", "1.0.1--r43h031d066_8": "sha256:41254e9bbf607a9fe2b5832da6ec5980e8f70f588ca3d69cdd2eb216b4273a8e"}, "docker": "quay.io/biocontainers/tssar", "aliases": {"TSSAR": "/usr/local/bin/TSSAR", "TSSAR.bak": "/usr/local/bin/TSSAR.bak", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tssar.
shpc-registry automated BioContainers addition for tssar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tssar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tssar:1.0.1--r43h031d066_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tssar/1.0.1--r43h031d066_8
$ module help quay.io/biocontainers/tssar/1.0.1--r43h031d066_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tssar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tssar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tssar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tssar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tssar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tssar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TSSAR

```bash
$ singularity exec <container> /usr/local/bin/TSSAR
$ podman run --it --rm --entrypoint /usr/local/bin/TSSAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TSSAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TSSAR.bak

```bash
$ singularity exec <container> /usr/local/bin/TSSAR.bak
$ podman run --it --rm --entrypoint /usr/local/bin/TSSAR.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TSSAR.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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