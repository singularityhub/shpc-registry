---
layout: container
name:  "quay.io/biocontainers/curl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/curl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/curl/container.yaml"
updated_at: "2022-10-29 05:46:05.613395"
latest: "7.80.0"
container_url: "https://biocontainers.pro/tools/curl"
aliases:
 - "acountry"
 - "adig"
 - "ahost"
 - "c_rehash"
 - "captoinfo"
 - "clear"
 - "compile_et"
 - "curl"
 - "curl-config"
 - "gss-client"
versions:
 - "7.80.0"
description: "shpc-registry automated BioContainers addition for curl"
config: {"url": "https://biocontainers.pro/tools/curl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for curl", "latest": {"7.80.0": "sha256:02612444381847547416743657819f1d360fd3ac49bcff68faaf100db77ae597"}, "tags": {"7.80.0": "sha256:02612444381847547416743657819f1d360fd3ac49bcff68faaf100db77ae597"}, "docker": "quay.io/biocontainers/curl", "aliases": {"acountry": "/usr/local/bin/acountry", "adig": "/usr/local/bin/adig", "ahost": "/usr/local/bin/ahost", "c_rehash": "/usr/local/bin/c_rehash", "captoinfo": "/usr/local/bin/captoinfo", "clear": "/usr/local/bin/clear", "compile_et": "/usr/local/bin/compile_et", "curl": "/usr/local/bin/curl", "curl-config": "/usr/local/bin/curl-config", "gss-client": "/usr/local/bin/gss-client"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/curl.
shpc-registry automated BioContainers addition for curl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/curl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/curl:7.80.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/curl/7.80.0
$ module help quay.io/biocontainers/curl/7.80.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### curl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### curl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### curl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### curl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### curl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### curl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### acountry

```bash
$ singularity exec <container> /usr/local/bin/acountry
$ podman run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acountry   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adig

```bash
$ singularity exec <container> /usr/local/bin/adig
$ podman run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ahost

```bash
$ singularity exec <container> /usr/local/bin/ahost
$ podman run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ahost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c_rehash

```bash
$ singularity exec <container> /usr/local/bin/c_rehash
$ podman run --it --rm --entrypoint /usr/local/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### captoinfo

```bash
$ singularity exec <container> /usr/local/bin/captoinfo
$ podman run --it --rm --entrypoint /usr/local/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clear

```bash
$ singularity exec <container> /usr/local/bin/clear
$ podman run --it --rm --entrypoint /usr/local/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile_et

```bash
$ singularity exec <container> /usr/local/bin/compile_et
$ podman run --it --rm --entrypoint /usr/local/bin/compile_et   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile_et   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curl

```bash
$ singularity exec <container> /usr/local/bin/curl
$ podman run --it --rm --entrypoint /usr/local/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curl-config

```bash
$ singularity exec <container> /usr/local/bin/curl-config
$ podman run --it --rm --entrypoint /usr/local/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gss-client

```bash
$ singularity exec <container> /usr/local/bin/gss-client
$ podman run --it --rm --entrypoint /usr/local/bin/gss-client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gss-client   -v ${PWD} -w ${PWD} <container> -c " $@"
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