---
layout: container
name:  "quay.io/biocontainers/perl-json-xs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-json-xs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-json-xs/container.yaml"
updated_at: "2024-11-09 02:50:30.814207"
latest: "4.03--pl5321h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/perl-json-xs"
aliases:
 - "json_xs"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "4.03--pl5321h9f5acd7_1"
 - "4.03--pl5321h4ac6f70_2"
 - "4.03--pl5321h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for perl-json-xs"
config: {"url": "https://biocontainers.pro/tools/perl-json-xs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-json-xs", "latest": {"4.03--pl5321h4ac6f70_3": "sha256:adf68d1b5f052c71345b48a71b8b58f7a2a51b9757abced3200324129ebc1d82"}, "tags": {"4.03--pl5321h9f5acd7_1": "sha256:54a3acc7cdf5176b7234038fd8fc5d988fb2810e462672f45918a6c2e28c8f6f", "4.03--pl5321h4ac6f70_2": "sha256:72fd88e5c509397a8576577b64be367cf75925abe290c9c5046b1a96dd737e81", "4.03--pl5321h4ac6f70_3": "sha256:adf68d1b5f052c71345b48a71b8b58f7a2a51b9757abced3200324129ebc1d82"}, "docker": "quay.io/biocontainers/perl-json-xs", "aliases": {"json_xs": "/usr/local/bin/json_xs", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-json-xs.
shpc-registry automated BioContainers addition for perl-json-xs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-json-xs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-json-xs:4.03--pl5321h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-json-xs/4.03--pl5321h4ac6f70_3
$ module help quay.io/biocontainers/perl-json-xs/4.03--pl5321h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-json-xs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-xs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-xs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-json-xs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-json-xs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-json-xs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### json_xs

```bash
$ singularity exec <container> /usr/local/bin/json_xs
$ podman run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
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