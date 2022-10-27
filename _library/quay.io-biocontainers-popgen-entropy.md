---
layout: container
name:  "quay.io/biocontainers/popgen-entropy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/popgen-entropy/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/popgen-entropy/container.yaml"
updated_at: "2022-10-27 01:16:08.217163"
latest: "2.0--hc73b757_6"
container_url: "https://biocontainers.pro/tools/popgen-entropy"
aliases:
 - "entropy"
 - "estpost.entropy"
 - "acountry"
 - "adig"
 - "ahost"
 - "c_rehash"
 - "captoinfo"
 - "clear"
 - "compile_et"
 - "curl-config"
 - "gif2h5"
 - "gsl-config"
 - "gsl-histogram"
 - "gsl-randist"
 - "gss-client"
 - "h2load"
 - "h52gif"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5dump"
 - "h5fc"
 - "h5format_convert"
 - "h5import"
versions:
 - "2.0--hc73b757_6"
description: "shpc-registry automated BioContainers addition for popgen-entropy"
config: {"url": "https://biocontainers.pro/tools/popgen-entropy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for popgen-entropy", "latest": {"2.0--hc73b757_6": "sha256:a33eabe9f3d808b95f540c19038eb00db7427490200a8bfc73517eb0da919bc2"}, "tags": {"2.0--hc73b757_6": "sha256:a33eabe9f3d808b95f540c19038eb00db7427490200a8bfc73517eb0da919bc2"}, "docker": "quay.io/biocontainers/popgen-entropy", "aliases": {"entropy": "/usr/local/bin/entropy", "estpost.entropy": "/usr/local/bin/estpost.entropy", "acountry": "/usr/local/bin/acountry", "adig": "/usr/local/bin/adig", "ahost": "/usr/local/bin/ahost", "c_rehash": "/usr/local/bin/c_rehash", "captoinfo": "/usr/local/bin/captoinfo", "clear": "/usr/local/bin/clear", "compile_et": "/usr/local/bin/compile_et", "curl-config": "/usr/local/bin/curl-config", "gif2h5": "/usr/local/bin/gif2h5", "gsl-config": "/usr/local/bin/gsl-config", "gsl-histogram": "/usr/local/bin/gsl-histogram", "gsl-randist": "/usr/local/bin/gsl-randist", "gss-client": "/usr/local/bin/gss-client", "h2load": "/usr/local/bin/h2load", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5dump": "/usr/local/bin/h5dump", "h5fc": "/usr/local/bin/h5fc", "h5format_convert": "/usr/local/bin/h5format_convert", "h5import": "/usr/local/bin/h5import"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/popgen-entropy.
shpc-registry automated BioContainers addition for popgen-entropy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/popgen-entropy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/popgen-entropy:2.0--hc73b757_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/popgen-entropy/2.0--hc73b757_6
$ module help quay.io/biocontainers/popgen-entropy/2.0--hc73b757_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### popgen-entropy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### popgen-entropy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### popgen-entropy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### popgen-entropy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### popgen-entropy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### popgen-entropy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### entropy

```bash
$ singularity exec <container> /usr/local/bin/entropy
$ podman run --it --rm --entrypoint /usr/local/bin/entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estpost.entropy

```bash
$ singularity exec <container> /usr/local/bin/estpost.entropy
$ podman run --it --rm --entrypoint /usr/local/bin/estpost.entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estpost.entropy   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### curl-config

```bash
$ singularity exec <container> /usr/local/bin/curl-config
$ podman run --it --rm --entrypoint /usr/local/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-config

```bash
$ singularity exec <container> /usr/local/bin/gsl-config
$ podman run --it --rm --entrypoint /usr/local/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-histogram

```bash
$ singularity exec <container> /usr/local/bin/gsl-histogram
$ podman run --it --rm --entrypoint /usr/local/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-randist

```bash
$ singularity exec <container> /usr/local/bin/gsl-randist
$ podman run --it --rm --entrypoint /usr/local/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gss-client

```bash
$ singularity exec <container> /usr/local/bin/gss-client
$ podman run --it --rm --entrypoint /usr/local/bin/gss-client   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gss-client   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2load

```bash
$ singularity exec <container> /usr/local/bin/h2load
$ podman run --it --rm --entrypoint /usr/local/bin/h2load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5dump

```bash
$ singularity exec <container> /usr/local/bin/h5dump
$ podman run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
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