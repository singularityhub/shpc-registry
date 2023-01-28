---
layout: container
name:  "quay.io/biocontainers/lissero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lissero/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lissero/container.yaml"
updated_at: "2023-01-28 03:47:13.813151"
latest: "0.4.9--py_0"
container_url: "https://biocontainers.pro/tools/lissero"
aliases:
 - "gfPcr"
 - "gfServer"
 - "isPcr"
 - "lissero"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
versions:
 - "0.4.9--py_0"
description: "shpc-registry automated BioContainers addition for lissero"
config: {"url": "https://biocontainers.pro/tools/lissero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lissero", "latest": {"0.4.9--py_0": "sha256:d209fcec504828bfb4338764d476032d9d7fa213fbeaf3d6c8656f25532abf3d"}, "tags": {"0.4.9--py_0": "sha256:d209fcec504828bfb4338764d476032d9d7fa213fbeaf3d6c8656f25532abf3d"}, "docker": "quay.io/biocontainers/lissero", "aliases": {"gfPcr": "/usr/local/bin/gfPcr", "gfServer": "/usr/local/bin/gfServer", "isPcr": "/usr/local/bin/isPcr", "lissero": "/usr/local/bin/lissero", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lissero.
shpc-registry automated BioContainers addition for lissero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lissero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lissero:0.4.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lissero/0.4.9--py_0
$ module help quay.io/biocontainers/lissero/0.4.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lissero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lissero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lissero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lissero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lissero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lissero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfPcr

```bash
$ singularity exec <container> /usr/local/bin/gfPcr
$ podman run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfServer

```bash
$ singularity exec <container> /usr/local/bin/gfServer
$ podman run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfServer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPcr

```bash
$ singularity exec <container> /usr/local/bin/isPcr
$ podman run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPcr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lissero

```bash
$ singularity exec <container> /usr/local/bin/lissero
$ podman run --it --rm --entrypoint /usr/local/bin/lissero   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lissero   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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